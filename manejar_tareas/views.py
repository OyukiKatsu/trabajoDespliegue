from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
# Create your views here.

#Index con enlaces para la pagina
def index(request):
    return render(request, 'index.html')



#Gestion de vista(Cursos)
#########################################################################################################
#Tabla de cursos
def cursos(request):
    cursos = models.Curso.objects.all()
    return render(request, 'Cursos/cursos.html', {"cursos":cursos})

#Formulario para crear cursos
def curso_new(request):
    if request.method == 'POST':
        form = forms.curso_form_model(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabla_cursos') 
    else:
        form = forms.curso_form_model()
    
    return render(request, 'Cursos/curso_new.html', {"form":form})

#Detalles del curso clikado
def curso_detalles(request, pk):
    curso = get_object_or_404(models.Curso, pk=pk)    
    return render(request, 'Cursos/curso_detalles.html', {"curso":curso})

#Formulario de edicion del curso clikado
def curso_edit(request, pk):
    curso = get_object_or_404(models.Curso, pk=pk)
    if request.method == 'POST':
        form = forms.curso_form_model(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('tabla_cursos') 
    else:
        form = forms.curso_form_model(instance=curso)
    
    return render(request, 'Cursos/curso_edit.html', {"form":form})

#Eliminacion del curso clikado
def curso_delete(request, pk):
    curso = get_object_or_404(models.Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('tabla_cursos') 
    return render(request, 'Cursos/curso_delete.html', {"curso":curso})



#Gestion de vista(Estudiantes)
#########################################################################################################
#Tabla de Estudiantes
def estudiantes(request):
    estudiantes = models.Estudiante.objects.all()
    return render(request, 'Estudiantes/estudiantes.html', {"estudiantes":estudiantes})

#Formulario para crear estudiantes
def estudiante_new(request):
    if request.method == 'POST':
        form = forms.estudiante_form_model(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabla_estudiantes') 
    else:
        form = forms.estudiante_form_model()
    
    return render(request, 'Estudiantes/estudiante_new.html', {"form":form})

#Detalles del estudiante clikado
def estudiante_detalles(request, pk):
    estudiante = get_object_or_404(models.Estudiante, pk=pk)    
    return render(request, 'Estudiantes/estudiante_detalles.html', {"estudiante":estudiante})

#Formulario de edicion del estudiante clikado
def estudiante_edit(request, pk):
    estudiante = get_object_or_404(models.Estudiante, pk=pk)
    if request.method == 'POST':
        form = forms.estudiante_form_model(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('tabla_estudiantes') 
    else:
        form = forms.estudiante_form_model(instance=estudiante)
    
    return render(request, 'Estudiantes/estudiante_edit.html', {"form":form})

#Eliminacion del estudiantes clikado
def estudiante_delete(request, pk):
    estudiante = get_object_or_404(models.Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('tabla_estudiantes') 
    return render(request, 'Estudiantes/estudiante_delete.html', {"estudiante":estudiante})



#Gestion de vista(Inscripciones)
#########################################################################################################
#Tabla de Inscripciones
def inscripciones(request):
    inscripciones = models.Inscripcion.objects.all()
    return render(request, 'Inscripciones/inscripciones.html', {"inscripciones":inscripciones})

#Formulario para crear inscripciones
def inscripcion_new(request):
    if request.method == 'POST':
        form = forms.inscripcion_form_model(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tabla_inscripciones') 
    else:
        form = forms.inscripcion_form_model()
    
    return render(request, 'Inscripciones/inscripcion_new.html', {"form":form})

#Detalles de la inscripcion clikada
def inscripcion_detalles(request, pk):
    inscripcion = get_object_or_404(models.Inscripcion, pk=pk)    
    return render(request, 'Inscripciones/inscripcion_detalles.html', {"inscripcion":inscripcion})

#Eliminacion de la inscripcion clikada
def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(models.Inscripcion, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('tabla_inscripciones') 
    return render(request, 'Inscripciones/inscripcion_delete.html', {"inscripcion":inscripcion})