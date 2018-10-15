from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        # Model to use
        model = Project
        # User editable fields from the model Project
        fields = ('title', 'content', 'image', 'tag', 'published_date')