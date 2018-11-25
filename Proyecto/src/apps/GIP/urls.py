from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^GIP',TemplateView.as_view(template_name='gip/gip.html'),name='gip'),
]