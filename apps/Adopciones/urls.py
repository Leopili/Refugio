from django.conf.urls import re_path
from django.contrib.auth.views import login_required

from apps.Adopciones.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, \
	SolicitudDelete

app_name="Adopciones"
urlpatterns = [
    re_path(r'^index$', index_adopcion),
    re_path(r'^solicitud/listar$',SolicitudList.as_view(), name='solicitud_listar'),
    re_path(r'^solicitud/nueva$',SolicitudCreate.as_view(), name='solicitud_crear'),
    re_path(r'^solicitud/editar/(?P<pk>\d+)$',SolicitudUpdate.as_view(), name='solicitud_editar'),
    re_path(r'^solicitud/eliminar/(?P<pk>\d+)$',SolicitudDelete.as_view(), name='solicitud_eliminar'),
]