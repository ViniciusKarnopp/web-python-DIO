from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) #pode ser nulo ou branco
    data_evento = models.DateTimeField(verbose_name="Data do evento")
    data_criacao = models.DateTimeField(auto_now=True) #inserindo hora atual
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #models.cascade indica q se excluir o usuario, exclui todos os eventos dele tbm

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_criacao(self):
        return self.data_evento.strftime('%d/%m/%y %H:%M')
    
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        return self.data_evento < datetime.now()