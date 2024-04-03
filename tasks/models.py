from django.db import models
from django.contrib.auth.models import User

# Modelo/tabla task
class Task(models.Model):
    titulo = models.CharField(max_length=100)
    #Blank, que puede estar vacío
    descripcion = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#Mostrar titulo y usuario en el panel de admin 
    def __str__(self):
        return self.titulo + ' -by: ' + self.user.username