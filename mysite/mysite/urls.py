from django.conf.urls import patterns, include, url
from hackv5.views import *
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hackv5/', include('hackv5.urls')),
    url(r'^hackv5/attendence/', attendence, name='attendence'),
    url(r'^hackv5/mess/', mess, name='mess'),
)
