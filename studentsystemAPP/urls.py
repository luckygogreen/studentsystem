
from django.urls import path
from django.conf.urls import url,include
from studentsystemAPP import views

urlpatterns = [
    # path(r'^$', views.index),
    url(r'^$',views.index),
]
