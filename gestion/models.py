from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal'),
    )

    rol = models.CharField(max_length=7, choices=ROLES, default='normal')


class Eventos(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField()
    ubicacion = models.CharField(max_length=250)
    inscritos = models.ManyToManyField(Usuario, related_name='eventos inscritos', blank=True)

    def __str__(self):
        return self.nombre