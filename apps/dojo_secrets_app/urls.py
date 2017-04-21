from django.conf.urls import url,include
from django.contrib import admin
import views

app_name = 'dojo_secrets_app'
urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^popular$', views.popular, name='popular' ),
    url(r'^create_secret$', views.create_secret, name='create_secret' ),
    url(r'^dojo_secrets_app/(?P<id>\d+)/delete$', views.delete_secret, name="delete_secret" ),
    url(r'^dojo_secrets_app/(?P<id>\d+)/like$', views.like_secret, name="like_secret" ),
]
