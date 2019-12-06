from django.urls import path
from django.conf.urls import url, include
from king_admin import views

urlpatterns = [
    # path(r'^$', views.index),
    url(r'^$', views.index, name='table_index'),
    url(r'^(\w+)/(\w+)/$', views.display_table_objs, name='table_objs'),
]
