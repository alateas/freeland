from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'ajax_portions$', 'food.views.ajax_portions'),
    url(r'$', 'food.views.main'),
)
