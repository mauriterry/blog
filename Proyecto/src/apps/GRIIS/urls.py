from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^GRIIS',TemplateView.as_view(template_name='griis/griis.html'),name='griis'),
]