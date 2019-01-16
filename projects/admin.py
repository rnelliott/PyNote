from django.contrib import admin
from .models import Projects, Category

# Register the Project class in the admin
admin.site.register(Projects)
admin.site.register(Category)
