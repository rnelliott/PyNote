from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Projects
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def get_projects(request):
    """
    Create view with all existing Projects, which exist before now,
    render them to the projects.html template
    """
    # Filter projects by only those where logged in project user/owner
    # is same as logged in user
    projects = Projects.objects.filter(user__exact=request.user)  
    return render(request, "projects.html", {"projects": projects})

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
            return redirect(project_details, project.pk)            
    else:
        form = ProjectForm(instance=project)
    return render(request, "projectform.html", {"form": form})



