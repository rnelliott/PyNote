from django import forms
from .models import Projects, Category

class ProjectForm(forms.ModelForm):
    class Meta:
        # Model to use
        model = Projects
        # User editable fields from the model Project
        fields = ('title', 'user', 'content', 'tag', 'published_date', 'category')
        # Remove fields
        exclude = ['user', 'image', 'published_date']