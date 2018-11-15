from django import forms
from apps.Mascotas.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota


		fields = [
		'nombre',
		'sexo',
		'edad_aproximada',
		'fecha_rescate',
		'imagen',
		'persona',
		'vacuna',
		]

		labels = {
		'nombre': 'Nombre',
		'sexo': 'Sexo',
		'edad_aproximada': 'Edad Aproximada',
		'fecha_rescate': 'Fecha de Rescate' ,
		'imagen': 'Imagen',
		'persona': 'Adoptante' ,
		'vacuna': 'Vacunas',
		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control'}) ,
		'sexo': forms.TextInput(attrs={'class': 'form-control'}),
		'edad_aproximada':forms.TextInput(attrs={'class': 'form-control'}),
		'fecha_rescate': forms.TextInput(attrs={'class': 'form-control'}),
		'imagen': forms.FileInput(attrs={'class':'form-control', 'name': 'imagen' }),
		'persona': forms.Select(attrs={'class': 'form-control'}),
		'vacuna': forms.CheckboxSelectMultiple() ,

		}