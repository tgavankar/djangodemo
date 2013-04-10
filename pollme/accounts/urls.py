from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from accounts import views

urlpatterns = patterns('',
    # ex: /accounts/
    url(r'^$', views.index, name='index'),
    # ex: /accounts/register/
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
)