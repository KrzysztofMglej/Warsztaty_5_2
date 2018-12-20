from django import forms
from .models import Photo, Comments


class PhotoAddForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['content', 'path']


class CommentAddForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['content']
