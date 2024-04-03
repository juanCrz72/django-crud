from django.contrib import admin

#Desde el archivo .models traer el modelo llamado Task
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    #Para mostrar en pantalla campos que son sólo de lecutra
    readonly_fields = ("created",)

admin.site.register(Task, TaskAdmin)

