from django import forms
from .models import Curso,Estudiante,Inscripcion
from django.core.exceptions import ValidationError
from datetime import date

#Formulario Curso
#########################################################################################################
class curso_form_model(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

    #Comprobar fechas
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio > fecha_fin:
            raise ValidationError('La fecha de inicio debe ser anterior a la fecha de fin')
        return cleaned_data




#Formulario Estudiante
#########################################################################################################
class estudiante_form_model(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
    #Comprobar fecha nacimiento y mayor de edad
    def clean(self):
        cleaned_data = super().clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        correo = cleaned_data.get('email')
        if Estudiante.objects.filter(email=correo).exists():
            raise ValidationError('El correo ya esta registrado.')
        if date.today().year - fecha_nacimiento.year < 18:
            raise ValidationError('El estudiante debe tener al menos 18 años.')
        return cleaned_data
        

        
#Formulario Inscripcion
#########################################################################################################
class inscripcion_form_model(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'
        widgets = {
            'fecha_inscripcion': forms.DateInput(attrs={'type': 'date'}),
        }
    #Comprobar que el estudiante no esta ya inscrito y el curso aun o ha terminado
    def clean(self):
        cleaned_data = super().clean()
        curso = cleaned_data.get('curso')
        fecha_inscripcion = cleaned_data.get('fecha_inscripcion')
        estudiante = cleaned_data.get('estudiante')

        if fecha_inscripcion > curso.fecha_fin:
            raise ValidationError('El curso al que se inscribe ya ha finalizado.')
        if Inscripcion.objects.filter(curso=curso, estudiante=estudiante).exists():
            raise ValidationError('El estudiante ya esta inscrito en el curso.')
        return cleaned_data