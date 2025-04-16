from .forms import PostForm
from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse


def lista_posts(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'lista_posts.html', {'posts': posts})


def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:lista_posts')
    else:
        form = PostForm()
    return render(request, 'criar_post.html', {'form': form})


def criar_post_2(request):
    if request.method == 'GET':
        return render(request, 'criar_post_2.html')

    if request.method == 'POST':
        nome = request.POST['titulo']
        conteudo = request.POST['conteudo']
        autor = request.POST['autor']
        publicado = request.POST['publicado']
        post = Post(titulo=nome, conteudo=conteudo, autor=autor, publicado=True)
        # post.save()
        # return redirect('blog:lista_posts')
