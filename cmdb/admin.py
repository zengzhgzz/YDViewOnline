import os
import time
import subprocess
from django.contrib import admin
from django.db.models import Count

import shutil
# Register your models here.
#from cmdb.models import UserInfo
#from cmdb.models import UserType
from django.template import RequestContext

from cmdb.models import FileInfo
from cmdb.models import FileType
#from cmdb.models import CustomUser
#from cmdb.models import MyProfile

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.core import serializers

"""扩展三：官网实现自定义USER例子"""
# from django import forms
# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
#
# from cmdb.models import MyUser
#
#
# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = MyUser
#         fields = ('username',)
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = MyUser
#         fields = ('username', 'password', 'is_super')
#
#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]
#
#
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     # list_display = ('email', 'date_of_birth', 'is_admin')
#     list_display = ('username','is_super')
#     list_filter = ('is_super',)
#     # fieldsets = (
#     #     (None, {'fields': ('email', 'password')}),
#     #     ('Personal info', {'fields': ('date_of_birth',)}),
#     #     ('Permissions', {'fields': ('is_admin',)}),
#     # )
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         # ('Personal info', {'fields': ('date_of_birth',)}),
#         ('Permissions', {'fields': ('is_super',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     # add_fieldsets = (
#     #     (None, {
#     #         'classes': ('wide',),
#     #         'fields': ('email', 'date_of_birth', 'password1', 'password2')}
#     #     ),
#     # )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2')}
#          ),
#     )
#     search_fields = ('username',)
#     ordering = ('username',)
#     filter_horizontal = ()
#
# # Now register the new UserAdmin...
# admin.site.register(MyUser, UserAdmin)
# # ... and, since we're not using Django's built-in permissions,
# # unregister the Group model from admin.
# admin.site.unregister(Group)
"""扩展三：End"""


#BEGINE TEST!!!!!!
# from cmdb.models import PageLink
from django.shortcuts import render_to_response
# import django.forms as forms
# from django.http import HttpResponseRedirect
# from  django.template import Template, Context
#
# hideSuccess = Template('Hid {{ count }} link{{ count|pluralize }}')
# @admin.register(PageLink)
# class PageLinkAdmin(admin.ModelAdmin):
#     list_display = ['url', 'page', 'added', 'displayInList', 'category', 'rank']
#     list_filter = ['displayInList']
#     search_fields = ['page__title', 'url__title']
#     ordering = ['-added']
#
#     actions = ['changeCategory']
#     #categorySuccess = Template(
#      #   '{% load humanize %}Categorized {{ count|apnumber }} link{{ count|pluralize }} as {{ category.key }}')
#
#     class CategoryForm(forms.Form):
#         _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
#         category = forms.ModelChoiceField(PageLink.objects)
#
#     def changeCategory(self, request, queryset):
#         form = None
#         if 'cancel' in request.POST:
#             self.message_user(request, 'Canceled link categorization')
#             return
#         elif 'categorize' in request.POST:
#             # do the categorization
#             form = self.CategoryForm(request.POST)
#             if form.is_valid():
#                 category = form.cleaned_data['category']
#                 for link in queryset:
#                     link.category = category
#                     link.save()
#                 self.message_user(request, hideSuccess.render(Context({'count': queryset.count()})))
#                 #self.message_user(request, self.categorySuccess.render(
#                  #   Context({'count': queryset.count(), 'category': category})))
#                 return HttpResponseRedirect(request.get_full_path())
#
#         if not form:
#             form = self.CategoryForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
#
#         return render_to_response('cms/categorize.html',
#                                   {'links': queryset, 'form': form, 'path': request.get_full_path()})
#
#     changeCategory.short_description = 'Set category'

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     actions_on_top = True


# @admin.register(MyProfile)
# class MyProfileAdmin(admin.ModelAdmin):
#     actions_on_top = True

"""扩展四：增加auth.user的字段"""
# #from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import Group
#
# from cmdb.models import Employee
#
# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = 'employee'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (EmployeeInline,)
#     # def has_add_permission(self, request):
#     # 去掉增加按钮
#     #     return False
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# #admin.site.unregister(Group)
# admin.site.register(User, UserAdmin)
"""扩展四 end"""

"""扩展五：Begin"""
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
#
# admin.site.register(User, UserAdmin)


#from django.contrib import admin
from cmdb import models
from django.contrib.auth.models import Permission, User
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import UserAdmin  # 从django继承过来后进行定制
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # admin中涉及到的两个表单
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.conf import settings
from django.shortcuts import get_object_or_404
from django import forms
# class User_exAdmin(admin.ModelAdmin):  # 验证码部分展示
#     list_display = ('valid_code', 'valid_time', 'email')


# custom user admin
class MyUserCreationForm(UserCreationForm):  # 增加用户表单重新定义，继承自UserCreationForm
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        #self.fields['email'].required = True   # 为了让此字段在admin中为必选项，自定义一个form
        #self.fields['name'].required = False  # 其实这个name字段可以不用设定required，因为在models中的MyUser类中已经设定了blank=False，但email字段在系统自带User的models中已经设定为
        # email = models.EmailField(_('email address'), blank=True)，除非直接改源码的django（不建议这么做），不然还是自定义一个表单做一下继承吧。


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active=True
        user.is_staff=True #默认为活跃的可登录该后台用户

        #增加FileInfo的可读权限
        content_type = ContentType.objects.get_for_model(FileInfo)
        permission = Permission.objects.get(
            codename='change_fileinfo',
            content_type=content_type,
        )
        # perm = Permission.objects.get(codename='read_fileinfo')  # 首先你需要添加"权限管理"这项权限
        # User = get_user_model()
        # print(User.objects.all())
        # userTmp = User.objects.get(username=user.username)
        # print(perm)
        # userTmp.user_permissions.add(perm)
        commit=True
        if commit:
            print('commit')
            user.save()
            try:
                user.user_permissions.add(permission)
                user.save() #增加默认权限
                print(user.get_all_permissions())
            except User.DoesNotExist:
                print("error")
        else:
            print('no commit')
        return user

class MyUserChangeForm(UserChangeForm):  # 编辑用户表单重新定义，继承自UserChangeForm
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        #self.fields['email'].required = True
        #self.fields['name'].required = True


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(CustomUserAdmin, self).__init__(*args, **kwargs)
        self.list_display = ('username','is_active', 'is_staff', 'is_superuser')
        self.search_fields = ('username', )
        self.form = MyUserChangeForm  #  编辑用户表单，使用自定义的表单
        self.add_form = MyUserCreationForm  # 添加用户表单，使用自定义的表单
        # 以上的属性都可以在django源码的UserAdmin类中找到，我们做以覆盖

    filter_horizontal = ('categoryPerm','user_permissions',)
    def changelist_view(self, request, extra_context=None):  # 这个方法在源码的admin/options.py文件的ModelAdmin这个类中定义，我们要重新定义它，以达到不同权限的用户，返回的表单内容不同
        if not request.user.is_superuser:  # 非super用户不能设定编辑是否为super用户
            self.fieldsets = ((None, {'fields': ('username', 'password',)}),
                              #(_('Personal info'), {'fields': ('name', 'email')}),  # _ 将('')里的内容国际化,这样可以让admin里的文字自动随着LANGUAGE_CODE切换中英文
                              (_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups')}),
                             # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                              )  # 这里('Permissions')中没有'is_superuser',此字段定义UserChangeForm表单中的具体显示内容，并可以分类显示
            self.add_fieldsets = ((None, {'classes': ('wide',),
                                          'fields': ('username', 'password1', 'password2', 'is_active',
                                                     'is_staff', 'groups'),
                                          }),
                                  )  #此字段定义UserCreationForm表单中的具体显示内容
        else:  # super账户可以做任何事
            self.fieldsets = ((None, {'fields': ('username', 'password','categoryPerm',)}),
                             # (_('Personal info'), {'fields': ('name', 'email')}),
                              (_('Permissions'), {'fields': ( 'is_superuser',)}),
                                 # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                              )
            self.add_fieldsets = ((None, {'classes': ('wide',),
                                          'fields': ('username', 'password1', 'password2','categoryPerm',
                                                      'is_superuser',),
                                          }),
                                  )
        return super(CustomUserAdmin, self).changelist_view(request, extra_context)

admin.site.unregister(Group)
admin.site.register(models.MyUser, CustomUserAdmin)  # 注册一下
# admin.site.register(models.User_ex, User_exAdmin)
"""扩展五：End"""
#END TEST!!!



# class BookInline(admin.TabularInline):
#     model = UserInfo
# @admin.register(UserInfo)
# class UserInfoAdmin(admin.ModelAdmin):
#
#     # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ( 'user','mytime',)
#
#     # list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 50
#
#     #将action操作框放置在顶部或底部
#     actions_on_top = True
#     actions_on_bottom = False
#
#     # ordering设置默认排序字段，负号表示降序排序
#     #ordering = ('-publish_time',)
#
#     # list_editable 设置默认可编辑字段
#     #list_editable = ['memo']
#
#     # fk_fields 设置显示外键字段
#     fk_fields = ('user_type',)
#
#     list_filter = ('user',)  # 过滤器
#     search_fields = ('user',)  # 搜索字段
#     date_hierarchy = 'mytime'  # 详细时间分层筛选　
#
#     actions = ['make_notify','export_selected_objects','export_as_json']
#
#     #测试action
#     def make_notify(self, request, queryset):
#         message_bit = "my click"
#         self.message_user(request, "%s 被触发了." % message_bit)
#
#     #测试action触发后重定向
#     def export_selected_objects(self, request, queryset):
#         selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
#         ct = ContentType.objects.get_for_model(queryset.model)
#         return HttpResponseRedirect("/index/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
#
#     #测试action触发后响应
#     def export_as_json(self, request, queryset):
#         response = HttpResponse(content_type="application/json")
#         serializers.serialize("json", queryset, stream=response)
#         return response
#
# @admin.register(UserType)
# class UserTypeAdmin(admin.ModelAdmin):
#     inlines = [
#         BookInline,
#     ]



""" 注册文件资源模型 """
@admin.register(FileInfo)
class FileInfoAdmin(admin.ModelAdmin):
    #list_display = ('id','file', 'size', 'category', 'user', 'date','degree','abstract','filePath','swfPath','fileOsPath','swfOsPath','categoryStr',)
    search_fields=['filePath']  # 搜索字段
    ordering = ('-date',)
    actions = ['open_flexpaper','open_directory',]
    inerQuerSet = None

    #打开目录
    def open_cur_directory(self, obj):
        """自定义一个a标签，跳转到实现打开文档的url"""
        dest = "/admin/cmdb/fileinfo/?ac=open_directory&id=" + obj.id.__str__()
        title =obj.categoryStr
        return '<a href="{}">{}</a>'.format(dest, title)

    open_cur_directory.short_description = '目录'
    open_cur_directory.allow_tags = True

    #打开文件
    def open_cur_file(self, obj):
        """自定义一个a标签，跳转到实现打开文档的url"""
        #dest = '{}flexpaper/'.format(obj.pk)
        dest="/flexpaper/?id="+obj.id.__str__()
        title = os.path.basename(obj.filePath.name)
        return '<a href="{}">{}</a>'.format(dest, title)

    open_cur_file.short_description = '文件'
    open_cur_file.allow_tags = True

    # def get_urls(self):
    #     """添加一个url，指向实现复制功能的函数flex_one"""
    #     from django.conf.urls import url
    #     urls = [
    #         url('^(?P<pk>\d+)flexpaper/?$',
    #             self.admin_site.admin_view(self.flex_one),
    #             name='flex_data'),
    #     ]
    #     return urls + super(FileInfoAdmin, self).get_urls()
    #
    # def flex_one(self, request, *args, **kwargs):
    #     return self.open_flexpaper(request,None)


    def general_status_judge(self,request):
        acRes = request.GET.get("ac", None)
        eRes = request.GET.get("e", None)
        qRes = request.GET.get("q",None)
        if ((acRes == "open_directory") | (eRes == "1") | (qRes!=None)):  # open_directory触发打开目录
            return True
        else:
            return False
    #打开flexpaper
    def open_flexpaper(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        return HttpResponseRedirect("/flexpaper/?id=%s" % (",".join(selected)))
        # ct = ContentType.objects.get_for_model(queryset.model)
        # return HttpResponseRedirect("/flexpaper/?ct=%s&id=%s" % (ct.pk, ",".join(selected)))
    open_flexpaper.short_description = "预览文档"

    #重新定义save操作，提交时调用pdf2swf.exe生成swf文件
    def save_model(self, request, obj, form, change):
        swfName = int(time.time())
        def get_pdf_osfile():
            """ 获取上传的pdf相对路径文件"""
            return "static\\upload\\" + obj.category.__str__() + "\\" + obj.file()

        def get_swf_file():
            """ 获取转成的swf Django路径文件"""
            return "/static/swf/" + str(swfName)  +".swf"     #避免出现中文，采用当前时间戳映射为SWF文件

        def get_swf_osfile():
            """ 获取转成的swf相对路径文件"""
            return "static\swf\\" + str(swfName) + ".swf"
        obj.user = request.user
        obj.fileOsPath = get_pdf_osfile()
        obj.swfPath = get_swf_file()
        obj.swfOsPath = get_swf_osfile()
        obj.categoryStr = obj.category.__str__()
        obj.save()
        super(FileInfoAdmin, self).save_model(request, obj, form, change)

        def execue_swf():
            """ 生成转换文件 """
            swfTool = "static\swftools\pdf2swf.exe"                                     # 转换工具相对路径文件
            pdfOsFile = get_pdf_osfile()#"static\\upload\\" + obj.file()                # 上传的pdf相对路径文件
            swfOsFile = get_swf_osfile()#"static\swf\\" + obj.file() + ".swf"           # 转成的swf相对路径文件
            toolArgs = "-f -t -s  storeallcharacters -s linknameurl -G -s poly2bitmap"  # 转换参数
            execueCmd = swfTool + " " + pdfOsFile + " -o " + swfOsFile + " " + toolArgs # 拼接成转换命令
            subprocess.call(execueCmd)                                                  # 调用pdf2swf工具进行转换
            #print("%s" % (execueCmd))
        execue_swf()

    def delete_model(self, request, obj):
        if(os.path.exists(obj.fileOsPath)):
            os.remove(obj.fileOsPath)
        if(os.path.exists(obj.swfOsPath)):
            os.remove(obj.swfOsPath)
        super(FileInfoAdmin, self).delete_model(request, obj)


    #过滤显示每种目录的一条记录
    def get_queryset(self, request):
        """函数作用："""
        if(request.method == "GET"):
            print("get_query:get")
            acRes = request.GET.get("ac", None)
            eRes = request.GET.get("e", None)
            qRes = request.GET.get("q",None)
            if(acRes == "open_directory"):
                """首次进入目录"""
                acId = request.GET.get("id",None)
                if(acId != None):
                    print("acId=",acId,type(acId))
                    categoryStrRes = FileInfo.objects.all().filter(id=int(acId)).values("categoryStr")[0]["categoryStr"]
                    print("1",categoryStrRes)
                    newQrSet = FileInfo.objects.all().filter(categoryStr=categoryStrRes)
                    self.inerQuerSet = newQrSet

            elif(eRes == "1"):
                """再次进入目录,无操作"""
                pass
            elif(qRes!=None):
                """查询"""
                print("fdfafdaf")
            else:
                """目录外"""
                L = []
                curUser = request.user
                if(curUser.is_superuser):
                    #超级用户默认全显示
                    es = FileType.objects.all()
                    for e in es:
                        queryRes = FileInfo.objects.all().filter(categoryStr=e.category)
                        if(queryRes):
                            L += [list(queryRes)[0]]  # 只需要每个类型的第一条
                else:
                    #其他用户只显示所有权目录
                    User = get_user_model()
                    fileTypeIdSet = User.objects.all().filter(username=curUser).values('categoryPerm')# <QuerySet [{'categoryPerm': 1}]>
                    for e in fileTypeIdSet:
                        queryRes =FileInfo.objects.all().filter(category_id=e['categoryPerm'])
                        if (queryRes):
                            L += [list(queryRes)[0]]  # 只需要每个类型的第一条
                newQrSet = FileInfo.objects.filter(pk__in=[x.pk for x in L])  # !!!!!重要：使用pk主键进行filter可以方便将list重新转化为Queryset
                self.inerQuerSet =newQrSet
        print("2",self.inerQuerSet )
        #根据类别得到FileType表的QuerySet
        #< QuerySet[{'category': '技术文档'}, {'category': '评审模板'}] >
        #print(qCateList)
        #tmpL = [x['category'] for x in list(qCateList)]                                 #根据QuerySet得到类别字符串
        #print(tmpL)

        #<QuerySet [<FileInfo: FileInfo object (7)>, <FileInfo: FileInfo object (8)>]>
        #qFiList = [list(FileInfo.objects.all().filter(categoryStr=x)).first() for x in tmpL]  #在FileInfo表中得到每个类别的一条记录
        #print(qFiList,type(qFiList))

        #qrSet =  FileInfo.objects.all().filter(categoryStr='技术文档')#notate(count=Count('category')).values('category', 'count')
        #res = qrSet.filter(id='5')
        #print(res.query)
        return self.inerQuerSet
    #统计每种目录下文件数量
    def get_file_count(self, obj):
        #FileInfo.objects.all().values('categoryStr').notate(count=Count('category')).values('count')
        #print(obj)
        return FileInfo.objects.all().filter(categoryStr = obj.categoryStr).count()
    get_file_count.short_description = u'文件数量'


    #重载，模拟目录结构
    """1、默认为GET方式，但是当触发action后，会将action方法名、选择的对象id等
       以POST的方式传给中间处理程序并回调该方法，然后再GET方式再次回调该方法(?)，
       所以POST判断中的处理，最后会被GET中的覆盖掉；
       2、open_directory触发时，POST->GET->GET，但是只有在第一次触发时会在GET中得到有效参数，
       其他情况，如刷新时，GET到的参数固定为 e=1 """
    def get_list_display(self, request):
        allDisplay = ['id','open_cur_file', 'size', 'category', 'user', 'date','degree','abstract',]
        if(request.user.is_superuser):
           pass
        else:
            del allDisplay[0]
        if (request.method == "POST"):
            print("POST")
            selectedRes = request.POST.get("_selected_action", None) #通过是否为POST且是否为open_directory action
            actionRes = request.POST.get("action", None)
            #print("selectedRes:",selectedRes,type(selectedRes))
            #print("actionRes: " , actionRes,type(actionRes))
            if(actionRes == "open_directory"): #传来的为打开目录操作
                print("open_directory")
                self.list_display =allDisplay
            """
            #测试POST数据
            for key in request.POST:
                print("1:", key)
                valuelist = request.POST.getlist(key)
                print("valuelist:",valuelist)
            """
        else:
            print("GET", len(self.list_display))
            self.list_display = ('open_cur_directory', 'date', 'get_file_count',)
            #acRes = request.GET.get("ac", None)
           # eRes = request.GET.get("e",None)
            #if((acRes == "open_directory") | (eRes =="1")): #open_directory触发打开目录
            statusPage = self.general_status_judge(request)
            if(statusPage):
                self.list_display=allDisplay
                # self.list_display = (
                # 'id','open_cur_file','file', 'size', 'category', 'user', 'date', 'degree', 'abstract', 'filePath', 'swfPath',
                # 'fileOsPath', 'swfOsPath', 'categoryStr',)

        return self.list_display

    #模拟打开目录操作
    def open_directory(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        #print(request.get_full_path())
        #return HttpResponseRedirect(request.get_full_path())       #不可行，这种方式没有参数
        return HttpResponseRedirect("/admin/cmdb/fileinfo/?ac=%s&ct=%s&id=%s" % ("open_directory",ct.pk, ",".join(selected))) #可行，会将参数带入重定向到该页面的GET的URL中
        #return HttpResponseRedirect("%s&ct=%s&ids=%s" % (request.get_full_path(), ct.pk, ",".join(selected))) #不可行，不会再重定向回本页面
        #return render_to_response(request.get_full_path(),
        #                          {'links': queryset, 'path': request.get_full_path()}) #不可行，不会重定向回本页面
    open_directory.short_description = "进入目录"

    def wrap_open_flexpaper(self,WrapSelf,WrapReq,WrapQurey):
        return self.open_flexpaper(WrapReq,WrapQurey)

    #重载，根据是否为打开目录操作调整action
    def get_actions(self, request):
        actions = super().get_actions(request)
        if(request.user.is_superuser):
            pass
        else:
            del actions['delete_selected']
        statusPage = self.general_status_judge(request)
        if (statusPage):
            del actions['open_directory']
            actions['open_flexpaper'] = (self.wrap_open_flexpaper, 'open_flexpaper', '预览文档')
        else:
            del actions['open_flexpaper']
        return actions


    def my_view(self, request):
        return self.admin_my_view(request)

    def get_urls(self):
        from django.conf.urls import url
        urls = super(FileInfoAdmin, self).get_urls()
        my_urls = [
                    url(r'^my_view/$', self.my_view),
                ]

        return my_urls + urls
    #重写该方法，修改显示的字段
    #def changelist_view(self, request, extra_context=None):
    #    self.list_display = [‘field1’]

    def admin_my_view(self,request,model_admin):
        opts = self.model._meta
        admin_site = self.admin_site
        has_perm = request.user.has_perm(FileInfo.app_label /
                                         + '.' + FileInfo.get_change_permission())
        context = {'admin_site': admin_site.name,
                   'title': "My Custom View",
                   'opts': opts,
                   'root_path': '/%s' % admin_site.root_path,
                   'app_label': opts.app_label,
                   'has_change_permission': has_perm}
        template = 'admin/cmdb/admin_my_view.html'
        return render_to_response(template, context,
                              context_instance=RequestContext(request))
    """ 注册文件资源目录模型 """
@admin.register(FileType)
class FileTypeAdmin(admin.ModelAdmin):

    # listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ( 'id','category','date','directoryPath','directoryOsPath',)

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50

    #将action操作框放置在顶部或底部
    actions_on_top = True

    # 重新定义save操作，填充目录路径
    def save_model(self, request, obj, form, change):
        def get_directory_path():
            """ 获取django可识别的目录"""
            return "/static/upload/" + obj.category

        def get_directory_ospath():
             """ 获取系统可识别的目录"""
             return "static\\upload\\" + obj.category

        obj.directoryPath = get_directory_path()
        obj.directoryOsPath = get_directory_ospath()
        obj.save()
        super(FileTypeAdmin, self).save_model(request, obj, form, change)
    # 重新定义save操作，填充目录路径
    def delete_model(self, request, obj):
        shutil.rmtree(obj.directoryOsPath)
        super(FileTypeAdmin, self).delete_model(request, obj)
admin.site.site_header = '移动安全·在线浏览系统'
admin.site.site_title = '在线浏览'
admin.site.site_url = ''


