from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'phonebuzz2.views.home', name='home'),
    url(r'^voice/$', 'phonebuzz2.views.voice'),
    url(r'^respond/$', 'phonebuzz2.views.respond'),
]
