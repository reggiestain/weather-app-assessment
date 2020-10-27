from django import forms
from .models import NotesApp


class NoteCreate(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-2 w-75'}))

    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control mb-2 w-75'}))

    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-2 w-75'}))

    class Meta:
        model = NotesApp
        fields = ['title', 'content', 'author']
