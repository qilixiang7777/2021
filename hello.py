hello world!

from django.http import HttpResponse

def index(request):
    return HttpResponse("CSDN读者你好啊！")

def login(request):
    return redirect("/index")

hello boys!
