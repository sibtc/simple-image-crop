from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from mysite.album import views


urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
