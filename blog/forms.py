from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'intro_text', 'text', 'type', 'category', 'update_date',)
