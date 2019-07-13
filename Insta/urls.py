from django.contrib import admin
from django.urls import path, include

from Insta.views import HelloDjango

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('/', include('Insta.urls')),
    path('', HelloDjango.as_view(), name = 'home')
]