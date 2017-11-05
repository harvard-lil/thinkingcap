from django.conf.urls import url, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='docs.html'), name='docs'),
]