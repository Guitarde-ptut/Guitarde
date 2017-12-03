from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^tutos/$', views.index, name='index'),
    url(r'^t/(?P<id_tuto>[0-9]+)/$', views.tuto, name='tuto'),
]
