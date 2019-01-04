from django import forms
from .models import Projects

class ProjectForm(forms.ModelForm):
    class Meta:
        # Model to use
        model = Projects
        # User editable fields from the model Project
        fields = ('title', 'user', 'content', 'tag', 'published_date')
        # Remove fields
        exclude = ['user', 'image', 'published_date']