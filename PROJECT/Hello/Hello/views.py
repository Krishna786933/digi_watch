from django.http import HttpResponse
from django.shortcuts import render

def sayHello(request):
    return HttpResponse("Hello world !")

def first(request):
    return HttpResponse("this is a first paragrah.")

def  course(request,coursemd):
    return HttpResponse(coursemd)

def homePage(request):
    # data = {
    #     'title' : 'first Web Page',
    #     'bdata':"hii this is krishna singh baghel",
    #     'lst' : ["krishna","Singh","baghel"],
    #     'number':[23,34,45,623,435,67,345]
    # }
    return render(request,"index.html")