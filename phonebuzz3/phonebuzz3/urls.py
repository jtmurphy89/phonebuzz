from django.conf.urls import include, url
from django.contrib import admin
from celerycallapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^voice/$', views.voice, name='voice'),
    url(r'^respond/$', views.respond, name='respond'),
]
