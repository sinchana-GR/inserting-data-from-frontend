from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')
def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')
    
    return render(request,'insert_topic.html')

def insert_webpage(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    if request.method=='POST':
       topic=request.POST['topic']
       n=request.POST['n']
       u=request.POST['u']
       TO=Topic.objects.get(topic_name=topic)
       TO.save()
       WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
       WO.save()
       return HttpResponse('insertion of webpage is done')
    
    return render(request,'insert_webpage.html',d)
def insert_access(request):
    n=WebPage.objects.all()
    d={'n':n}
    if request.method=='POST':
        n=request.POST['n']
        d=request.POST['d']
        a=request.POST['a']
        WO=WebPage.objects.get(name=n)
        WO.save()
        AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AO.save()
        return HttpResponse('data inserted to accessrecord')
        
    
    return render(request,'insert_access.html',d)



def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=WebPage.objects.none()
        for i in MSTS:
            RWOS=RWOS|WebPage.objects.filter(topic_name=i)
        d1={'RWOS':RWOS}
        return render(request,'display_webpages.html',d1)
    return render(request,'retrive_webpage.html',d)         

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)
def radio(request):
    RTO=Topic.objects.all()
    d={'RTO':RTO}
    return render(request,'radio.html',d)



