from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.layaway, name='layaway'),
    url(r'^layaway', views.layaway, name='layaway'),
]
