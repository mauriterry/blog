"""proyecto_investigacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from apps.GISIC.views import IndexView, EntradaDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^markdown/', include('django_markdown.urls')),
    #url(r'^$', IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)/$', EntradaDetailView.as_view()),
    url(r'^gegi/', include('apps.GEGI.urls',namespace='GEGI'),name="GEGI"),
    url(r'^gip/', include('apps.GIP.urls',namespace='GIP'),name="GIP"),
    url(r'^gisic/', include('apps.GISIC.urls',namespace='GISIC'),name="GISIC"),
    url(r'^griis/', include('apps.GRIIS.urls',namespace='GRIIS'),name="GRIIS"),
    
    url(r'^$', RedirectView.as_view(url='index')),
    url(r'^index',IndexView.as_view(),name='index'),
    #url(r'^index',login,{'template_name':'index.html'},name='index'),
    url(r'^about',login,{'template_name':'institucional/about.html'},name='about'),
    url(r'^contact',login,{'template_name':'institucional/contact.html'},name='contact'),
    
    url(r'^accounts/login/',login,{'template_name':'index.html'},name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html', 'email_template_name': 'registration/password_reset_email.html'}, name='password_reset'), 
    url(r'^password_reset_done', password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
]
