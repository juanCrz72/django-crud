from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        # Campos que agregaré al formulario
        fields = ['titulo', 'descripcion', 'important']
        
        #Se agregan detalles de html-boostrap con la funcion attrs
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escribe aquí tu título'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Escribe aquí tu descripción'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
