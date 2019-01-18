from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from products.views import all_products

from .forms import ProjectForm
from .models import Category, Projects


@login_required
def index(request):
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    return render(request, "index.html", {"projects": projects, "categories": categories})


@login_required
def get_projects(request):
    """
    Create view with all existing Projects, which exist before now,
    render them to the projects.html template
    """
    # Filter projects by only those where logged in project user/owner
    # is same as logged in user
    projects = Projects.objects.filter(user__exact=request.user)
    return render(request, "index.html", {"projects": projects})


@login_required
def get_projects_sidenav(request):
    """
    Render all existing Projects to sidebar nav items
    """
    projects = Projects.objects.filter(user__exact=request.user)
    return render(request, "base.html", {"projects": projects})


@login_required
def project_details(request, pk):
    """
    Creat view returning a Project object referenced by its PrimaryKey/ID,
    render the Project details to projectdetails.html.
    Return a 404 if Project is not found.
    """
    # Display details on a given Project
    project = get_object_or_404(Projects, pk=pk)
    project.views += 1
    project.save()
    return render(request, "projectdetails.html", {"project": project})


@login_required
def create_or_edit_project(request, pk=None):
    """
    Create view that can either create or edit a Project,
    edits if exists or creates if not.
    """
    project = get_object_or_404(Projects, pk=pk) if pk else None
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.instance.user = request.user
            project = form.save()
            return redirect(index)
    else:
        """
        Count how many notes a user has,
        if less than 5 -> proceed,
        othrewise -> redirect upgrade page.
        """
        count_users_notes = Projects.objects.all().count()
        if count_users_notes < 5:
            form = ProjectForm(instance=project)
        else:
            return redirect(all_products)
    return render(request, "projectform.html", {"form": form})


# Delete a project/note
@login_required
def delete_project(request, pk):
    """
    Delete the project, return all existing projects
    """
    project = get_object_or_404(Projects, pk=pk)
    project.delete()
    return redirect(index)


# Search
def search_project(request):
    query = request.GET.get('search')
    results = Projects.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).filter(user__exact=request.user)

    return render(request, "search.html", {"projects": results})


# Sharable URLs
def public_url(request, url):
    # project = get_object_or_404(Projects, uuid=url)
    results = Projects.objects.filter(Q(uuid__icontains=url))
    return render(request, "sharedproject.html", {"project": results})
