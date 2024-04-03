"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.helloword ),
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('task/',views.task, name='task'),
    path('task_complete/',views.vista_tarea_Completa, name='vista_tarea_Completa'),
    path('logout/',views.cerrarSesion, name='cerrarSesion'),
    path('iniciaeSesion/',views.iniciaeSesion, name='iniciaeSesion'),
    path('task/create/',views.create_task, name='create_task'),
    
    #Se agrega el filtro task_id para mostrar la tarea específica
    path('task/<int:task_id>/',views.detalles, name='detalles'),

    path('task/<int:task_id>/complete',views.tarea_completada, name='tarea_completada'),
      path('task/<int:task_id>/delete',views.eliminar_tarea, name='eliminar_tarea'),
]
