from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', include('Landing.urls')),
    url(r'^auth', include('Auth.urls')),
    url(r'^patient', include('Patient.urls'))
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
