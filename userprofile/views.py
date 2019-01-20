from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from projects.views import index
from .models import Profile
from django.db.models import Q
import sweetify

# Create your views here.


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, (
                'Your profile was successfully updated!'))
            sweetify.success(
                request, 'Your profile has been updated', timer=2000, toast=True)
            return redirect(update_profile)
        else:
            messages.error(request, ('Please correct the error below.'))
            sweetify.error(request, 'Please correct the error below.', timer=2000, toast=True)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    premium = Profile.objects.filter(
        Q(premium=True)).filter(user__exact=request.user)
    if premium:
        return render(request, 'userprofile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'profile': premium
        })
    else:
        return render(request, 'userprofile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
