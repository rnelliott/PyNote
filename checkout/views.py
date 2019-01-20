import stripe
import sweetify
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils import timezone

from checkout.models import Order
from products.models import Product
from projects.models import Projects, Category
from userprofile.models import Profile

from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                sweetify.error(request, "your card was declined!",
                               timer=2000, toast=True)

            if customer.paid:
                messages.error(request, "You have successfully paid!")
                sweetify.success(
                    request, 'You have successfully paid!', timer=1500, toast=True)
                """
                Find the user profile from request, then,
                set Profile.premium to 'True'
                """
                user_profile_premium = Profile.objects.get(id=request.user.id)
                premium = user_profile_premium
                premium.premium = True  # change field
                premium.save()
                """
                Find the order belonging to this user, then,
                set Order.paid to 'True'
                """
                order_is_paid = Order.objects.get(user=request.user.id)
                paid = order_is_paid
                paid.paid = True
                paid.save()
                request.session['cart'] = {}
                return redirect('update_profile')
            else:
                messages.error(request, "Unable to take payment")
                sweetify.error(request, 'Unabel to take payment',
                               timer=1500, toast=True)
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
            sweetify.error(request, 'We were unable to take a payment with that card!',
                           timer=1500, toast=True)
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form,
                                             'payment_form': payment_form,
                                             'projects': projects,
                                             'categories': categories,
                                             'publishable': settings.STRIPE_PUBLISHABLE})
