from django.contrib import admin

# Register your models here.
from studentsystemAPP import models

class CustomAdmin(admin.ModelAdmin):
    '''设置列表可显示的字段'''
    list_display = ('id','name','phone','source','cunsultant','status','date',)
    '''设置过滤选项'''
    list_filter = ('source','cunsultant','date',)
    search_fields = ('phone','name',)
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tags',)
    '''设置可编辑字段'''
    list_editable = ('status','source',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_name', )

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','name',)

admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.Customers,CustomAdmin)
admin.site.register(models.Tags)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Role)
admin.site.register(models.Course)
admin.site.register(models.Branch)
admin.site.register(models.Classlist)
admin.site.register(models.Enrollment)
admin.site.register(models.Payment)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.Menu,MenuAdmin)
