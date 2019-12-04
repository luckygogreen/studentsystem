from django.db import models
from django.contrib.auth.models import User  # Django自带的用户验证表


# Create your models here.

class Customers(models.Model):
    # 客户表
    name = models.CharField(max_length=32, blank=True, null=True)  # 32字节，3个是一个汉字,blank=True设置DjangoAdmin的
    phone = models.CharField(max_length=64, unique=True)
    wechatorother = models.CharField(max_length=64, blank=True, null=True)
    source_choices = (
        (0, '转介绍'),
        (1, 'Google'),
        (2, 'Facebook'),
        (3, 'Twitter'),
        (4, '其他互联网'),
        (5, '机构合作')
    )
    source = models.SmallIntegerField(choices=source_choices)  # 占2个字节
    referral_from = models.CharField(verbose_name="转介绍电话", max_length=64, null=True, blank=True)
    consult_course = models.ForeignKey('Course', on_delete='models.CASCADE', verbose_name='所咨询课程')
    cousult_content = models.TextField(verbose_name="咨询详情")
    tags = models.ManyToManyField(to='Tags')
    cunsultant = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='接待销售')
    momo = models.TextField(blank=True, null=True, verbose_name='备注')
    date = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return self.phone


class Tags(models.Model):
    tagname = models.CharField(unique=True, max_length=64, verbose_name='标签名称')

    def __str__(self):
        return self.tagname


class CustomerFollowUp(models.Model):
    # 客户跟进表
    customers = models.ForeignKey(to='Customers', on_delete=models.CASCADE, verbose_name='被跟进客户')
    content = models.TextField(verbose_name='跟进内容')
    consultant = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, verbose_name='跟进人')
    intention_choices = ((0, '2周内报名'),
                         (1, '一个月内报名'),
                         (2, '近期无报名计划'),
                         (3, '已在其他机构报名'),
                         (4, '已拉黑'),
                         (5, '已报名'))
    intention = models.SmallIntegerField(choices=intention_choices, verbose_name='跟进进度')
    date = models.DateTimeField(auto_now_add=True, verbose_name='跟进时间')

    def __str__(self):
        return self.customers, self.intention


class UserProfile(models.Model):
    # 用户表
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 关联Django自带关联表,千万不能加引号
    name = models.CharField(max_length=32)
    role = models.ManyToManyField(to='Role')

    def __str__(self):
        return self.name


class Role(models.Model):
    # 角色表
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name  # #


class Course(models.Model):
    # 课程表
    name = models.CharField(unique=True, max_length=64)
    price = models.PositiveSmallIntegerField()
    period = models.PositiveSmallIntegerField(verbose_name='周期(月)')
    outline = models.TextField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    # 校区
    name = models.CharField(max_length=64, unique=True)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Classlist(models.Model):
    # 班级表

    course = models.ForeignKey(to='Course', on_delete=models.CASCADE, verbose_name='课程')
    semester = models.PositiveSmallIntegerField(verbose_name='学期')
    teacher = models.ManyToManyField(to='UserProfile', verbose_name='授课老师')
    branch = models.ForeignKey(to='Branch', on_delete=models.CASCADE, verbose_name='分校区')
    class_type_choices = ((0, '面授(周末)'),
                          (1, '网络(全天)'),
                          (1, '网络(周末)'),
                          (2, '面授(全天)'))
    class_type = models.PositiveSmallIntegerField(choices=class_type_choices, verbose_name='授课类型')
    startdate = models.DateField(verbose_name='开课日期')
    enddate = models.DateField(verbose_name='结课日期')

    def __str__(self):
        return self.course, self.branch, self.semester

    class Meta:
        unique_together = ('branch', 'course', 'semester')


class Enrollment(models.Model):
    # 学生报名表，存学生报名信息，例如合同，入学日期，课程等
    customer = models.ForeignKey(to='Customers', on_delete=models.CASCADE, verbose_name='对应客户')
    enrolled_class = models.ForeignKey(to='Classlist', on_delete=models.CASCADE, verbose_name='所报课程')
    consultant = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, verbose_name='课程顾问')
    contract_aggrement = models.BooleanField(default=False, verbose_name='学员是否同意学校条款')
    contract_approved = models.BooleanField(default=False, verbose_name='学校是否审核学生申请')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer, self.enrolled_class

    class Meta:
        unique_together = ('customer', 'enrolled_class')


class Payment(models.Model):
    # 缴费记录表
    customer = models.ForeignKey(to='Customers', on_delete=models.CASCADE)
    course = models.ForeignKey(to='Course', on_delete=models.CASCADE, verbose_name='所报课程')
    amount = models.PositiveSmallIntegerField(verbose_name='缴费数额')
    consultant = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer, self.course, self.amount


class CourseRecord(models.Model):
    # 上课记录表
    fromclass = models.ForeignKey(to='Classlist', on_delete=models.CASCADE, verbose_name='关联的班级')
    daynumber = models.PositiveSmallIntegerField(verbose_name='第几天课')
    teacher = models.ForeignKey(to='UserProfile', on_delete=models.CASCADE, verbose_name='授课老师')
    outline = models.TextField(verbose_name='本节课内容')
    homework = models.BooleanField(default=True, verbose_name='是否有作业')
    homework_title = models.CharField(max_length=128, blank=True, null=True, verbose_name='作业标题')
    homework_content = models.TextField(blank=True, null=True, verbose_name='作业内容')
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fromclass, self.daynumber

    class Meta:
        unique_together = ('fromclass', 'daynumber')


class StudyRecord(models.Model):
    # 学习记录表
    student = models.ForeignKey(to='Enrollment', on_delete=models.CASCADE)
    course_record = models.ForeignKey(to='CourseRecord', on_delete=models.CASCADE)
    attendance_choices = ((0, '已签到'),
                          (1, '迟到'),
                          (2, '缺勤'),
                          (3, '早退'))
    attendance = models.SmallIntegerField(choices=attendance_choices, default=0)
    score_choices = (
        (100, 'A+'),
        (90, 'A'),
        (85, 'B+'),
        (80, 'B'),
        (75, 'B-'),
        (70, 'C+'),
        (65, 'C'),
        (60, 'C-'),
        (-10, 'D+'),
        (-20, 'D'),
        (-30, 'D-'),
        (-100, 'Copy'),
        (0, 'N/A'),
    )
    score = models.SmallIntegerField(choices=score_choices)
    memo = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student, self.course_record, self.score, self.attendance
