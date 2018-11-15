from django.contrib import admin
from django.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from Refugio.Views import index
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'^Mascotas/',include ('apps.Mascotas.urls')),
    re_path(r'^Adopciones/',include ('apps.Adopciones.urls')),
    re_path(r'^accounts/login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    re_path(r'^logout/',auth_views.LogoutView.as_view(template_name=''), name='logout'),
    re_path(r'^$',auth_views.LoginView.as_view(template_name='index.html')),
    re_path(r'^Inicio',index, name='inicio'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
