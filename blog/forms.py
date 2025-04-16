from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'autor', 'publicado']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }
