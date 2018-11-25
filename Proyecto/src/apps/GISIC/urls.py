from django.conf.urls import url, include
from django.views.generic import TemplateView

from ..GISIC.views import IndexView, EntradaDetailView

urlpatterns = [
    url(r'^GISIC',TemplateView.as_view(template_name='gisic/gisic.html'),name='gisic'),
]