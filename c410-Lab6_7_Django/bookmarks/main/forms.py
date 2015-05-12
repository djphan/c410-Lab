from django import forms
from main.models import Tag, Link

class TagForm(forms.ModelForm):

   # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.Textarea()
        }

class LinkForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Link
        fields = ['title', 'url', 'tags']
        widgets = {
            'body': forms.Textarea(),
            'url': forms.Textarea(),
            'tags': forms.CheckboxSelectMultiple()
        }