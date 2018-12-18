from django import forms
from .models import Photo


class PhotoAddForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ['creation_date', 'user', 'path_small']
