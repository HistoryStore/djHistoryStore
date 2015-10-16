from django.conf.urls import url

from graficos import views

urlpatterns = [
    url(r'^$', views.indice, name='indice'),
]
