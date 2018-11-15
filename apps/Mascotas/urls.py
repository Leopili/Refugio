from django.urls import re_path
from apps.Mascotas.views import listado, index, Mascota_view, Mascota_list,Mascota_edit,Mascota_delete,Mascotalist,MascotaCreate,MascotaUpdate,MascotaDelete
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


app_name="Mascotas"
urlpatterns = [
    re_path(r'^$',index, name='index'),
    re_path(r'^nuevo$', login_required(MascotaCreate.as_view()), name='Mascotas_crear'),
    re_path(r'^listar',login_required(Mascotalist.as_view()), name='Mascotas_listar'),
    re_path(r'^editar/(?P<pk>\d+)/$',login_required(MascotaUpdate.as_view()), name='Mascotas_editar'),
    re_path(r'^eliminar/(?P<pk>\d+)/$',login_required(MascotaDelete.as_view()), name='Mascotas_eliminar'),
    re_path(r'^listado/', listado, name="listado"),
    re_path(r'^(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)