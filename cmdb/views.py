from django.shortcuts import render
import json
from django.shortcuts import  HttpResponse
from cmdb import models
# Create your views here.

user_list = [
    {"user":"zz", "pwd":"1023"},
    {"user":"zy", "pwd":"0822"},
]
def index(request):
    # request.POST
    if(request.method == "POST"):

        username = request.POST.get("username", None)
        passwd = request.POST.get("passwd", None)
        #1、打印用户输入
        print(username,passwd)

        #2、将用户输入添加列表并通过render返回给用户页面
        temp={"user":username,"pwd":passwd}
        user_list.append(temp)

        #3、a将用户输入添加数据库
        models.UserInfo.objects.create(user=username,pwd=passwd)

    # b从数据中读取所有数据
    test_user_list = models.UserInfo.objects.all()
    # request.GET
    #return HttpResponse("Hello World!")
    #return render(request, "test.html", {"data":test_user_list})
    return render(request,"testPaper.html",)
    #return render(request, "testNewPage.html", )


#处理flexpaper页面
def flexpaper(request):
    # request.POST
    fileId = request.GET.get('id')

    # 从数据中读取指定数据
    count = models.FileInfo.objects.filter(id=fileId).count()

    if(count==0):
        return HttpResponse("文件不存在", status=404)

    fileObj = models.FileInfo.objects.filter(id=fileId).first()
    swfPath = fileObj.swfPath
    print (swfPath, type(swfPath))
    List = [swfPath,]
    return render(request,"flexpaper.html",{"data":json.dumps(List)})
    #return render(request,"flexpaper.html",{"data": swfPath})





