from django import forms
from .models import Projects

class ProjectForm(forms.ModelForm):
    class Meta:
        # Model to use
        model = Projects
        # User editable fields from the model Project
        fields = ('title', 'content', 'image', 'tag', 'published_date')