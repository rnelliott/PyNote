import sweetify
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.template.context_processors import csrf
from home.views import home
from projects.models import Category, Projects
from projects.views import index

from .forms import UserLoginForm, UserRegistrationForm


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    sweetify.success(request, 'You logged out!', timer=1500, toast=True)

    return redirect(reverse('home'))


def login(request):
    if request.user.is_authenticated():
        return redirect(index)
    else:
        """A view that manages the login form"""
        if request.method == 'POST':
            user_form = UserLoginForm(request.POST)
            if user_form.is_valid():
                user = auth.authenticate(request.POST['username_or_email'],
                                        password=request.POST['password'])

                if user:
                    auth.login(request, user)
                    messages.error(request, "You have successfully logged in")
                    sweetify.success(request, 'You logged in!',
                                    timer=1500, toast=True)
                    if request.GET and request.GET['next'] != '':
                        next = request.GET['next']
                        return HttpResponseRedirect(next)
                    else:
                        return redirect(reverse('index'))
                else:
                    user_form.add_error(
                        None, "Your username or password are incorrect")
        else:
            user_form = UserLoginForm()

        args = {'user_form': user_form, 'next': request.GET.get('next', '')}
        return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def register(request):
    if request.user.is_authenticated():
        return redirect(index)
    else:
        """A view that manages the registration form"""
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                user_form.save()

                user = auth.authenticate(request.POST.get('email'),
                                        password=request.POST.get('password1'))

                if user:
                    auth.login(request, user)
                    messages.success(request, "You have successfully registered")
                    return redirect(reverse('index'))

                else:
                    messages.error(request, "unable to log you in at this time!")
                    sweetify.error(
                        request, 'Sorry, you couldn\'t be logged in at this time', timer=2000, toast=True)
        else:
            user_form = UserRegistrationForm()

        args = {'user_form': user_form}
        return render(request, 'register.html', args)
