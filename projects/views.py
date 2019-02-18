import sweetify
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from products.models import Product
from products.views import all_products
from userprofile.models import Profile

from .forms import CategoryForm, ProjectForm
from .models import Category, Projects


# Render index page
@login_required
def index(request):
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    premium = Profile.objects.filter(
        Q(premium=True)).filter(user__exact=request.user)
    return render(request, "index.html", {"projects": projects,
                                          "categories": categories,
                                          "premium": premium})


# ********************
# Categories Views
# ********************
@login_required
def get_categories(request, pk):
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    projects_in_category = Projects.objects.filter(
        Q(category=pk)).filter(user__exact=request.user)
    return render(request, "categorysearch.html", {"projects": projects,
                                                   "categories": categories,
                                                   "projects_in_category": projects_in_category})


# Manage categories
@login_required
def manage_categories(request):
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.user = request.user
        category = form.save()
        form = CategoryForm()
    categories = Category.objects.filter(user__exact=request.user)
    return render(request, "categories.html", {"form": form, "categories": categories})


# Delete a category
@login_required
def delete_category(request, pk):
    """
    Delete the project, return all existing projects
    """
    category = get_object_or_404(Category, pk=pk) if pk else None
    category.delete()
    form = CategoryForm(request.POST, request.FILES)
    categories = Category.objects.filter(user__exact=request.user)
    sweetify.success(request, "You have deleted the category!", timer=1000)
    return redirect(manage_categories)


# ********************
# Projects Views
# ********************

# Display the details of a given project
@login_required
def project_details(request, pk):
    """
    Create view returning a Project object referenced by its PrimaryKey/ID,
    render the Project details to projectdetails.html.
    Return a 404 if Project is not found.
    """
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    project = get_object_or_404(Projects, pk=pk)
    project.views += 1
    project.save()
    return render(request, "projectdetails.html", {"project": project,
                                                   "projects": projects,
                                                   "categories": categories})


# Create project or edit if exists
@login_required
def create_or_edit_project(request, pk=None):
    """
    Create view that can either create or edit a Project,
    edits if exists or creates if not.
    """
    categories = Category.objects.filter(user__exact=request.user)
    projects = Projects.objects.filter(user__exact=request.user)
    project = get_object_or_404(Projects, pk=pk) if pk else None
    projects_count = Projects.objects.filter(user__exact=request.user).count()
    categories_count = Category.objects.all().count()

    if categories.count() < 1:
        return redirect(manage_categories)
    else:
        if projects.count() > 4:
            sweetify.error(request, "To create more than 5 notes ...",
                           html='<button class="btn btn-info btn-lg" id="upgrade-btn">Please upgrade <i class="fa fa-arrow-right"></i></>',
                           timer=7000)
            return redirect(index)
        else:
            if request.method == 'POST':
                form = ProjectForm(request.user, request.POST,
                                   request.FILES, instance=project)
                if form.is_valid():
                    form.instance.user = request.user
                    project = form.save()
                    return redirect(index)
            else:
                form = ProjectForm(request.user, instance=project)
            return render(request, "projectform.html", {"form": form,
                                                        "projects": projects,
                                                        "categories": categories})


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
    categories = Category.objects.filter(user__exact=request.user)
    results = Projects.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).filter(user__exact=request.user)

    return render(request, "search.html", {"projects": results,
                                           "categories": categories})
