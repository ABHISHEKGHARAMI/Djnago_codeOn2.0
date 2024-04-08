# creating the form for sharing user post
from django import forms

# import comments from the model
from .models import Comment

class EmailPostForm(forms.Form):
    # adding the different field
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea)
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        