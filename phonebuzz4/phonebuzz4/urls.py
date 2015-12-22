from django.conf.urls import include, url
from django.contrib import admin
from callreplayapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name='home'),
    url(r'^voice/$', views.voice, name='voice'),
    url(r'^respond/$', views.respond, name='respond'),
    url(r'^replay/(?P<pk>[0-9]+)/$', views.replay, name='replay'),
    url(r'^read/(?P<digits>[0-9]+)/', views.read, name='read')

]
