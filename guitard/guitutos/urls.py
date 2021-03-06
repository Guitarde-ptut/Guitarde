from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tutos/$', views.liste_tutos, name='liste_tutos'),
    url(r'^t/(?P<id_tuto>[0-9]+)/$', views.tuto, name='tuto'),
    url(r'^inscription/$', views.inscription, name='inscription'),
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^ajouter/$', views.ajouter, name='ajouter'),
]
