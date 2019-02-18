from django.shortcuts import redirect, render
from projects.views import index

def home(request):
    if request.user.is_authenticated():
        return redirect(index)
    else:
        return render(request, "home.html")
