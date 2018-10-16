from django.conf import url
from .views import get_projects, project_details, create_or_edit_project

urlpatterns= [
    # root dir for the projects app
    url(r'^$', get_projects, name='get_projects'),
    # If url passed with ID, open project_details
    url(r'^(?P<pk>\d+)$', project_details, name='project_details'),
    # If creating a new project
    url(r'^new/$', create_or_edit_project, name='new_project'),
    # Id editing a project
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_project, name='edit_project'),
]