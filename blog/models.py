from django.db import models


class Post(models.Model):

    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.titulo)

    class Meta:
        ordering = ['-data_publicacao']
