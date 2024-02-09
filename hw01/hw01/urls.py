
from django.contrib import admin
from django.urls import include, path
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
