from django.contrib import admin

# Register your models here.
from studentsystemAPP import models

class CustomAdmin(admin.ModelAdmin):
    list_display = ('id','phone','source','cunsultant','status','date')
    list_filter = ('source','cunsultant','date')
    search_fields = ('phone','name')
    raw_id_fields = ('consult_course',)
    filter_horizontal = ('tagname',)
    list_editable = ('status')

admin.site.register(models.UserProfile)
admin.site.register(models.Customers)
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
