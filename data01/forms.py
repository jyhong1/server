from django import forms
from data01.models import feedback

class CommentForm(forms.ModelForm):

    class Meta:
        model = feedback
        fields = ('name', 'message',)
