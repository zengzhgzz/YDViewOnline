import os
from django.conf import settings

from django.db import models
import django.utils.timezone as timezone
# Create your models here.

from django.contrib import admin
from django.utils.html import format_html

#BEGIN Test

"""
扩展Admin原有的User类
测试一，需要signals.py文件，并将setting.py中的CUSTOM_USER_MODEL
"""
# from django.contrib.auth.models import User, UserManager
# from mysite.signals import *
#
#
# class CustomUser(User):
#     description = models.TextField(max_length=256, default="", blank=True)
#     headImage = models.FileField(upload_to='./static/users/', null=True, blank=True)
#     scope = models.IntegerField(default=100)
#
#     objects = UserManager()

""""
#扩展USER类方法二，
# 采用继承源码方式，具体参见：https://blog.csdn.net/SVALBARDKSY/article/details/51199707
"""
#from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# import datetime
# class ProfileBase(type):
#     def __new__(cls, name, bases, attrs):
#         module = attrs.pop('__module__')
#         parents = [b for b in bases if isinstance(b, ProfileBase)]
#         if parents:
#             fields = []
#             for obj_name, obj in attrs.items():
#                 if isinstance(obj, models.Field): fields.append(obj_name)
#                 User.add_to_class(obj_name, obj)
#             UserAdmin.fieldsets = list(UserAdmin.fieldsets)
#             UserAdmin.fieldsets.append((name, {'fields': fields}))
#         return super(ProfileBase, cls).__new__(cls, name, bases, attrs)
#
# class Profile(object):
#     __metaclass__ = ProfileBase
#
# class MyProfile(Profile):
#     nickname = models.CharField(max_length = 255)
#     birthday = models.DateTimeField(null = True, blank = True)
#     city = models.CharField(max_length = 30, blank = True)
#     university = models.CharField(max_length = 255, blank = True)
#
#     def is_today_birthday(self):
#         return self.birthday.date() == datetime.date.today()




""""
#扩展USER类方法三，
# 官网曾给出的例子 参见https://docs.djangoproject.com/en/dev/topics/auth/customizing/
"""
#
# from django.contrib.auth.models import User, UserManager
# from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
#
#
# # class MyUserManager(BaseUserManager):
# #     # def create_user(self, email, date_of_birth, password=None):
# #     def create_user(self,username, password=None):
# #         """
# #         Creates and saves a User with the given email, date of
# #         birth and password.
# #         """
# #         # if not email:
# #         #     raise ValueError('Users must have an email address')
# #         if not username:
# #             raise  ValueError("请填写用户名")
# #         # user = self.model(
# #         #     email=self.normalize_email(email),
# #         #     date_of_birth=date_of_birth,
# #         # )
# #         user = username
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user
# #
# #     # def create_superuser(self, email, date_of_birth, password):
# #     def create_superuser(self, username, password):
# #         """
# #         Creates and saves a superuser with the given email, date of
# #         birth and password.
# #         """
# #         # user = self.create_user(
# #         #     email,
# #         #     password=password,
# #         #     date_of_birth=date_of_birth,
# #         # )
# #         user = self.create_user(username=username,password=password)
# #         user.is_admin = True
# #         user.save(using=self._db)
# #         return user
#
#
# class MyUser(AbstractBaseUser):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#        # unique=True,
#     )
#     #date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     is_super = models.BooleanField(default=False)
#     last_login = models.DateTimeField(verbose_name='上次登录',)
#     #date_joined = models.DateField(verbose_name='注册日期',)
#     def get_short_name():
#         return  '用户信息'
#     # objects = MyUserManager()
#     objects = UserManager()
#
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['date_of_birth']
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         # return self.email
#         return self.username

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True
    #
    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
#

#
# class UserInfo (models.Model):
#     user = models.CharField('用户名',max_length=64)
#     pwd = models.CharField(max_length=16)
#     memo = models.CharField(max_length=16)
#     #memo = models.TextField()
#     #file = models.ImageField(upload_to='upload')
#     headImg = models.FileField(upload_to='./static/upload/')
#     mytime =  models.DateTimeField('保存日期',default = timezone.now,max_length=8)
#     user_type = models.ForeignKey("UserType", null=True, blank=True,on_delete=models.CASCADE,)
#     def __str__(self):
#         return self.user
#
# class UserType(models.Model):
#     name = models.CharField(max_length=8)
#     def __str__(self):
#         return self.name


#
# class PageLink(models.Model):
#     url=models.CharField(max_length=16)
#     page=models.CharField(max_length=16)
#     added=models.CharField(max_length=16)
#     displayInList=models.CharField(max_length=16)
#     category=models.CharField(max_length=16)
#     rank=models.CharField(max_length=16)
#END Test



"""
#扩展USER类方法四，
# 官网曾给出的例子 参见https://docs.djangoproject.com/en/dev/topics/auth/customizing/
# """
# from django.contrib.auth.models import User
#
# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)

"""扩展四：End"""

"""
扩展五：仅继承AbstractUser类进行扩展，不再从AbstractBaseUser开始继承
"""
from django.contrib.auth.models import AbstractUser
#
# class User(AbstractUser):
#     pass
class MyUser(AbstractUser): # 继承AbstractUser类，实际上django的User也是继承他，我们要做的就是用自己的类代替django自己的User
    #name = models.CharField(u'中文名', max_length=32, blank=False, null=False)
    categoryPerm = models.ManyToManyField("FileType",verbose_name="可查看的目录")
    class Meta:
        verbose_name = u'用户管理'
        verbose_name_plural = u"用户管理"
"""扩展五：End"""

#文件模型
class FileInfo (models.Model):
    id = models.AutoField( primary_key=True,max_length=1)

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        #pdfFullFile = './static/upload/{0}'.format(filename)
        pdfFullFile = './static/upload/{0}/{1}'.format(instance.category,filename)
        print(pdfFullFile)
        #swfFullFile = pdfFullFile + ".swf"
        #swfCmd = "/static/swftools/pdf2swf.exe " + pdfFullFile + " -o " + swfFullFile + " -f -T 9 -t -s  storeallcharacters -s linknameurl -G -s poly2bitmap"
        # os.system(r'"pdf2swf.exe C:\Users\zhangz\bitcoin.pdf -o C:\Users\zhangz\bitcoin.pdf.swf -f -T 9 -t -s  storeallcharacters -s linknameurl -G -s poly2bitmap"')
        # os.system(r"%s",swfCmd)
        #print("%s" % (swfCmd))
        return pdfFullFile

    filePath = models.FileField('上传路径', upload_to=user_directory_path)
    #filePath = models.FileField('上传路径', unique=True,upload_to='./static/upload/')
    swfPath = models.CharField(max_length=128,editable=False,default="test",)
    fileOsPath = models.CharField(max_length=128,editable=False,default="test",)
    swfOsPath = models.CharField(max_length=128,editable=False,default="test",)
    SECRET_CHOICE = (
        (u'非密', u'非密'),
        (u'内部', u'内部'),
        (u'秘密', u'秘密'),
    )
    secret = models.CharField('密级',max_length=2, choices=SECRET_CHOICE)
    #user = models.CharField('用户',max_length=128,default="admin",)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,on_delete=models.CASCADE,)
    category = models.ForeignKey("FileType", verbose_name="目录", on_delete=models.CASCADE, )
    categoryStr = models.CharField(max_length=128,editable=False,default="test",)
    date = models.DateTimeField('上传日期',default = timezone.now,max_length=8)
    abstract = models.TextField('简介',blank=True)
    #memo = models.TextField()

    def degree(self):
        if self.secret == '秘密':
            color_code = 'red'
        elif self.secret == '内部':
            color_code = 'blue'
        else:
            color_code = 'green'
        return format_html(
            '<span style="color:{};">{}</span>',
            color_code,
            self.secret,
        )
    degree.short_description = u"密级"

    def file(self):
        if(self.filePath):
            return os.path.basename(self.filePath.name)
        else:
            return "NULL"
    file.short_description = "文件"

    def size(self):
        if(self.filePath):
            return self.filePath.size//1000
        else:
            return 0
    size.short_description = "大小 kB"

    user.short_description = "上传用户"

    class Meta:
        permissions=(
            ("read_fileinfo","可读权限"),
        )
        verbose_name = "文档资源"
        verbose_name_plural = "文档资源"
        #app_label = u"我的应用"

    #def __str__(self):
    #    return self.id
#目录模型
class FileType(models.Model):
    category = models.CharField(max_length=64)
    date = models.DateTimeField('创建日期', default=timezone.now, max_length=8)
    directoryPath = models.CharField(max_length=128,editable=True,default="test")
    directoryOsPath = models.CharField(max_length=128,editable=True,default="test")

    class Meta:
        # permissions = (
        #     ("view_filetype", "Can see available tasks"),
        #     ("change_filetype_status", "Can change the status of tasks"),
        #     ("close_filetype", "Can remove a task by setting its status as closed"),
        # )
        verbose_name = "目录管理"
        verbose_name_plural = "目录管理"
    def __str__(self):
        return self.category




