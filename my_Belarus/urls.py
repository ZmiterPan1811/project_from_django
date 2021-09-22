from django.contrib import admin
from django.conf.urls.static import static

from my_Belarus import settings
from aboutbelarus.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('aboutbelarus.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
