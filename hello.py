hello world!

from django.http import HttpResponse

def index(request):
    return HttpResponse("CSDN读者你好啊！")

