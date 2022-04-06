from django.db import models
from django.contrib.auth.models import User

class Referencia(models.Model):
    arquivo = models.FileField(upload_to='referencias')

    def __str__(self) -> str:
        return self.arquivo.url

class Emprego(models.Model):
    categoria_choices = (('D', 'Design'),
                         ('EV', 'Edição de Vídeo'))

    status_choices = (('C', 'Em criação'),
                      ('AA', 'Aguardando aprovação'),
                      ('F', 'Finalizado'))

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=2, choices=categoria_choices, default="D")
    prazo_entrega = models.DateTimeField()
    preco = models.FloatField()
    referencias = models.ManyToManyField(Referencia)
    profissional = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    reservado = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=status_choices ,default='AA')



    def __str__(self) -> str:
        return self.titulo


