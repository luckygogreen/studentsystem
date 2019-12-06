
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^crm/', include('studentsystemAPP.urls')),
    url(r'^student/', include('studentAPP.urls')),
    url(r'^king_admin/', include('king_admin.urls')),
]
