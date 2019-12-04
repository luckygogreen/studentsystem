from django.db import models


# Create your models here.

class Customers(models.Model):
    # 客户表
    name = models.CharField(max_length=32, blank=True, null=False)  # 32字节，3个是一个汉字,blank=True设置DjangoAdmin的
    phone = models.CharField(max_length=64, unique=True)
    wechat = models.CharField(max_length=64, null=False)
    source_choices = (
        (0, '转介绍'),
        (1, 'Google'),
        (2, 'Facebook'),
        (3, 'Twitter'),
        (4, '其他互联网'),
        (5, '机构合作')
    )
    source = models.SmallIntegerField(choices=source_choices)  # 占2个字节
    referral_from = models.CharField(verbose_name="转介绍电话", max_length=64, null=False, blank=True)
    consult_course = models.ForeignKey(to='Course', verbose_name='所咨询课程')
    cousult_content = models.TextField(verbose_name="咨询详情")
    cunsultant = models.ForeignKey('UserProfile', verbose_name='接待销售')
    date = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    # 用户表
    pass


class Role(models.Model):
    # 角色表
    pass


class CustomerFollowUp(models.Model):
    # 客户跟进表
    pass


class Course(models.Model):
    # 课程表
    pass


class Classlist(models.Model):
    # 班级表
    pass


class Enrollment(models.Model):
    # 学生报名表，存学生报名信息，例如合同，入学日期，课程等
    pass


class CourseRecord(models.Model):
    # 上课记录表
    pass


class StudyRecord(models.Model):
    # 学习记录表
    pass
