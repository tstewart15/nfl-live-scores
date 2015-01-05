from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mainapp.views.index'),
    url(r'^game/(?P<gsis>[\w]{10})$', 'mainapp.views.game')
)
