from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def customers_list(request):
    for role in request.user.userprofile.role.all():
        for menu in role.menus.all():
            print(menu.name,menu.url_name)
            print(request.path_info)
    return render(request, 'sales/customers.html')