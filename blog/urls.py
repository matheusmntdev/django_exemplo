from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('criar/', views.criar_post, name='criar_post'),
    path('criar2/', views.criar_post_2, name='criar_post_2'),
]
