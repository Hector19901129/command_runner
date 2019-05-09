from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from .views import CmdRunner

urlpatterns = [
    path('', include('cmd_runner.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
  urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
