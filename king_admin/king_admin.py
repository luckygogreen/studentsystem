from studentsystemAPP import models

enabled_admins = {}


class BaseAdmin(object):
    list_display = []


class CustomerAdmin(BaseAdmin):
    list_display = ['id', 'name','phone','source','consult_course']
    list_filter = ['source']


class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ['id', 'customers']
    list_filter = ['content']


# {'APP名'：{'model名'}：admin}
def register(model_class, admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {}

    admin_class.model = model_class  # 相当于model = models.Customers，反实例化对象,绑定model 对象和admin类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class


register(models.Customers, CustomerAdmin)
register(models.CustomerFollowUp, CustomerFollowUpAdmin)
