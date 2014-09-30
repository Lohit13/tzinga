from django.conf.urls import patterns, url

from hackv5 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

)
