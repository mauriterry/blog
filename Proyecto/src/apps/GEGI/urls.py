from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^GEGI',TemplateView.as_view(template_name='gegi/gegi.html'),name='gegi'),
]