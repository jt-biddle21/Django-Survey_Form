from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^submitted', views.submitted),
    url(r'^results', views.results),
    url(r'^reset', views.reset)
]
