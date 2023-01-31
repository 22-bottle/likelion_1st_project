from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'body', 'photo']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class':'form-control',
            'placeholder':"제목",
            'rows':20,
            'size':106
        }

        self.fields['body'].widget.attrs = {
            'class':'form-control',
            'placeholder':"본문",
            'rows':15,
            'cols':100
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'secret']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class':'form-control',
            'placeholder':"댓글",
            'rows':1,
            'cols':100,
        }