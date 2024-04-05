# creating the form for sharing user post
from django import forms

class EmailPostForm(forms.form):
    # adding the different field
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea)