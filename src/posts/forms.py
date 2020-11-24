from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

#Should be edited to get max length 200 char
class CommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 3
    
    }))
    class Meta:
        model = Comment
        fields = ('content', )