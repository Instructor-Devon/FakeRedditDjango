from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^post/create$', views.create),
    url(r'^post/delete/(?P<post_id>\d+)$', views.delete),
    url(r'^posts/vote/(?P<post_id>\d+)/(?P<is_upvote>[0-1]{1})$', views.vote)
]