from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    # ex: /accounts/
    url(r'^$', views.index, name='index'),
    # ex: /accounts/register/
    url(r'^register/$', views.register, name='register'),
)