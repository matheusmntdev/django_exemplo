from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.auth, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('logout/', views.sign_out, name='logout'),
]
