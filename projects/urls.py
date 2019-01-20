from django.conf.urls import url
from .views import index, project_details, create_or_edit_project, delete_project, search_project, public_url, get_categories

urlpatterns = [
    
    # root dir for the projects app
    url(r'^$', index, name='index'),
    # If getting all projects
    # url(r'^projects/$', get_projects, name='get_projects'),
    # If url passed with ID, open project_details
    url(r'^(?P<pk>\d+)$', project_details, name='project_details'),
    # If creating a new project
    url(r'^new/$', create_or_edit_project, name='new_project'),
    # Id editing a project
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_project, name='edit_project'),
    # delete a project
    url(r'^(?P<pk>\d+)/delete/$', delete_project, name='delete_project'),
    # search
    url(r'^results/$', search_project, name='search_project'),
    # category search
    url(r'^category-results/(?P<pk>\d+)$', get_categories, name='get_categories'),
    # sharable urls
    url(r'^public/([a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})$',
        public_url, name='public_url'),

]
