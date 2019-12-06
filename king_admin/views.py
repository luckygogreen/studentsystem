from django.shortcuts import render
from king_admin import king_admin
from studentsystemAPP import models
# Create your views here.

def index(request):
    print()
    return render(request, 'king_admin/table_index.html',{'table_list':king_admin.enabled_admins,})

def display_table_objs(request,app_name,table_name):
    print('-->',app_name,table_name)

    admin_class = king_admin.enabled_admins[app_name][table_name]
    # models_module = importlib.import_module('{}.models'.format(app_name))
    # model_obj = getattr(models_module,table_name)
    # return render(request,'king_admin/table_objs.html')
    return render(request,'king_admin/table_objs.html',{'admin_class':admin_class,'app_name':app_name,'table_name':table_name})
