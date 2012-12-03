from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djnew.views.home', name='home'),
    # url(r'^djnew/', include('djnew.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^food/', include('food.urls')),
    # url(r'^test/', 'food.vie'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
