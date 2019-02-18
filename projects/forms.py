from django import forms
from .models import Projects, Category


class ProjectForm(forms.ModelForm):
    class Meta:
        # Model to use
        model = Projects
        # User editable fields from the model Project
        fields = ('title', 'user', 'content', 'category', 'color')
        # Remove fields
        exclude = ['user', 'image', 'published_date']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'color')
