from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

#Librería de formulario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .form import TaskForm

#Login
from django.contrib.auth import login, logout, authenticate

#Librería para protección de rutas
from django.contrib.auth.decorators import login_required

#Librería para validar usuarios
from django.contrib.auth.models import User

from django.http import HttpResponse

from django.db import IntegrityError

from .models import Task

#Se define función home 
def home (request):
    return render(request, 'home.html')

#Se define función signup/registrar
def signup (request):
    if request.method == 'GET':
       return render(request, 'signup.html', {
        #formulario
         'form': UserCreationForm
     })

    else:
        #Validando las contraseñas 
        if request.POST['password1'] == request.POST['password2']:
           #Cachar posibles errores en la bd con Try y except
            try: 
            #registrando usuario
                user= User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            #Guardando usuario en la BD
                user.save()
                login(request,user)
                return redirect ('task')
            except IntegrityError: 
              return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error':'El usuario ya existe'
                }) 
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error':'Las contraseñas no coinciden'
                }) 

#Se define función task 
@login_required
def task (request):
    #Task.objects.all() para ver todos las consultas
    #Se realiza la consulta sólo del usuario actual 
    task = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'task.html', {
        'tareas' : task
    })

@login_required
def cerrarSesion (request):
    logout(request)
    return redirect('home')

def iniciaeSesion (request):
    if request.method == 'GET':
        return render (request, 'iniciaeSesion.html',{
       'form': AuthenticationForm
        })
    else:   
          user = authenticate(
              request, username=request.POST['username'], password=request.POST ['password'])
          if user is None: 
           return render (request, 'iniciaeSesion.html',{
            'form': AuthenticationForm, 
            'error': 'Usuario o contraseña son incorrectos'
          })
          else: 
             #guarda la sesión mediante cookies
              login(request,user)
              return redirect('task')
          
@login_required              
def create_task  (request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{
        'form':TaskForm
    })
    else: 
        try:
            form = TaskForm (request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect ('task')
        except ValueError: 
             return render(request, 'create_task.html',{
                 'form':TaskForm,
                 'error': 'Introduce un dato válido'
            })

@login_required        
def detalles (request, task_id) :
    if request.method == 'GET':
        #Con get_object_or_404 cachamos el error de entrar a ids que no existe
        #Además de lo anterior, las tareas se filtrarán por su respectivo id -> pk=task_id
        #Con user=request.user es para que el usuario sólo pueda ver sus tareas y no de otros
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        #Se manda a traer nuevamente el formulario, con instance = task, es el objecto del id de esa tarea
        form = TaskForm(instance=task)
        return render(request, 'detalles.html',{'task':task, 'form': form})
    else: 
        try: 
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            #Se actualiza el formulario con los nuevos datos 
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('task')
        except ValueError: 
            return render(request, 'detalles.html',
            {'task':task, 'form': form, 'error': 'Error al actualizar tarea'})

@login_required
def tarea_completada(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('task')
    
@login_required
def eliminar_tarea(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':  
        task.delete()
        return redirect('task')

@login_required
def vista_tarea_Completa (request):
    #datecompleted__isnull=False, muestra los datos que estén rellenados en el campo datecompleted 
    #Se realiza la consulta sólo del usuario actual
    task = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'task.html', {
        'tareas' : task
    })
