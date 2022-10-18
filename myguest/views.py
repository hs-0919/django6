from django.shortcuts import render, redirect
from myguest.models import Guest
from django.http.response import HttpResponse, HttpResponseRedirect
from datetime import datetime # 파이썬이 지원
from django.utils import timezone # 장고가 지원

# Create your views here.
def MainFunc(request):
    msg = "<h1>홈페이지</h1>"
    return render(request, "main.html", {"msg":msg})

def ListFunc(request):
    #print(gdatas)
    #print(Guest.objects.get(id=1))
    #print(Guest.objects.filter(id=1))
    #print(Guest.objects.filter(title='마음이'))
    #print(Guest.objects.filter(title__contains="선생님"))
    #....
    
    # 동적으로 order_by로 sort하기
    #gdatas = Guest.objects.all().order_by('title') #오름차순 정렬
    #gdatas = Guest.objects.all().order_by('-title') #내림차순 정렬
    #gdatas = Guest.objects.all().order_by('title', '-id') #1차키 2차키
    #gdatas = Guest.objects.all().order_by('-id')[0:2] #갯수
    
    
    gdatas = Guest.objects.all()
    
    return render(request, "list.html", {'gdatas':gdatas})

def InsertFunc(request):
    return render(request, "insert.html")

def InsertOkFunc(request):
    if request.method == "POST":
        # print(request.POST.get('title'))
        # print(request.POST['title'])
        Guest(
            title = request.POST['title'],
            content = request.POST['content'],
            # regdate = datetime.now()
            regdate = timezone.now()
        ).save()
        
    # return HttpResponseRedirect('/guest/') # 추가 후 목록 보기
    return redirect('/guest') # 추가 후 목록 보기
    
    
    
    