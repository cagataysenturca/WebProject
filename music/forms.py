
from django import forms
from .models import  Comment






class CommentForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputfield'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'class': 'contentClass'}))


    class Meta:
        model = Comment
        fields = [
            'name',
            'content',
        ]
