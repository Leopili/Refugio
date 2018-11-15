from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from apps.Mascotas.forms import MascotaForm
from apps.Mascotas.models import Mascota
from django.views.generic import ListView, CreateView, UpdateView,DeleteView


def listado(request):
	lista = serializers.serialize('json',Mascota.objects.all())
	return HttpResponse(lista, content_type='application/json')

def index(request):
	return render(request, 'Mascotas/index.html')

def Mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
		return redirect('Mascotas:Mascotas_listar')

	else:
		form = MascotaForm()

	return render(request, 'Mascotas/Mascotas_form.html',{'form': form})

def Mascota_list(request):
	mascota = Mascota.objects.all().order_by("id")
	contexto = {"mascotas": mascota}
	return render(request,"Mascotas/Mascotas_list.html",contexto)


def Mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == "GET":
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect("Mascotas:Mascotas_listar")
	return render(request,"Mascotas/Mascotas_form.html",{"form":form})


def Mascota_delete(request,id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == "POST":
		mascota.delete()
		return redirect("Mascotas:Mascotas_listar")
	return render(request,"Mascotas/Mascotas_delete.html",{"mascota":mascota})


class Mascotalist(ListView):
	model = Mascota
	template_name = "Mascotas/Mascotas_list.html"
	paginate_by = 10

class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = "Mascotas/Mascotas_form.html"
	success_url = reverse_lazy("Mascotas:Mascotas_listar")

class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = "Mascotas/Mascotas_form.html"
	success_url = reverse_lazy("Mascotas:Mascotas_listar")


class MascotaDelete(DeleteView):
	model = Mascota
	template_name = "Mascotas/Mascotas_delete.html"
	success_url = reverse_lazy("Mascotas:Mascotas_listar")

