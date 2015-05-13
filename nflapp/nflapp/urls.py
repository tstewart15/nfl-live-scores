from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mainapp.views.index'),
    url(r'^week/(?P<year>[\w]+)/(?P<week_type>[\w]+)/(?P<week_num>[\d]+)$',
        'mainapp.views.week_selection',
        name='week_selection'),
    url(r'^game/(?P<gsis>[\w]{10})$', 'mainapp.views.game')
)
