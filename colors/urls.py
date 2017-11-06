from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^$', color_pixel, name='colors'),
]