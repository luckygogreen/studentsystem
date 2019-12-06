from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def render_app_name(admin_class):
    return admin_class.model._meta.verbose_name_plural


@register.simple_tag
def get_query_sets(admin_class):
    print('admin_class:', admin_class)
    return admin_class.model.objects.all()


@register.simple_tag
def build_table_row(obj, admin_class):
    row_ele = ""
    # print('admin_class:',admin_class)
    # print('obj:',obj)
    for column in admin_class.list_display:
        # print('colunm:', column)
        column_data = getattr(obj, column)
        row_ele += "<td>%s</td>" % column_data
        # print('column_data:',column_data)
        # print('row_ele:',row_ele)
    return mark_safe(row_ele)

