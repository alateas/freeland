from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'ajax$', 'food.views.ajax'),
    url(r'$', 'food.views.test'),
)
