from django import forms

from .models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text', 'point', 'nick_name']
