from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^voice/$', 'phonebuzz1.views.voice'),
    url(r'^respond/$', 'phonebuzz1.views.respond'),
]
