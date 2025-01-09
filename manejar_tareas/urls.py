from django.urls import path
from . import views

urlpatterns = [
    #Principal(Index)
    path('', views.index, name='index'),

    #Gestion de Cursos
    path('cursos',views.cursos, name='tabla_cursos'),
    path('cursos/new', views.curso_new, name='curso_new'),
    path('cursos/<int:pk>', views.curso_detalles, name='curso_detalles'),
    path('cursos/<int:pk>/edit', views.curso_edit, name='curso_edit'),
    path('cursos/<int:pk>/delete', views.curso_delete, name='curso_delete'),
    
    #Gestion de Estudiantes
    path('estudiantes',views.estudiantes, name='tabla_estudiantes'),
    path('estudiantes/new', views.estudiante_new, name='estudiante_new'),
    path('estudiantes/<int:pk>', views.estudiante_detalles, name='estudiante_detalles'),
    path('estudiantes/<int:pk>/edit', views.estudiante_edit, name='estudiante_edit'),
    path('estudiantes/<int:pk>/delete', views.estudiante_delete, name='estudiante_delete'),

    #Gestion de Inscripciones
    path('inscripciones',views.inscripciones, name='tabla_inscripciones'),
    path('inscripciones/new', views.inscripcion_new, name='inscripcion_new'),
    path('inscripciones/<int:pk>', views.inscripcion_detalles, name='inscripcion_detalles'),
    path('inscripciones/<int:pk>/delete', views.inscripcion_delete, name='inscripcion_delete'),

]