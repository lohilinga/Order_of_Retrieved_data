from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topic(request):
    
    QSTO=topic.objects.all()
    QSTO=topic.objects.filter(Topic_name='cricket')
    QSTO=topic.objects.exclude(Topic_name='cricket')

    
    


    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
     
     QSWO=Website.objects.all()
     QSWO=Website.objects.filter(Topic_name='cricket')
     QSWO=Website.objects.exclude(Topic_name='cricket')
     QSWO=Website.objects.all().order_by('Topic_name')
     QSWO=Website.objects.all().order_by('url')
     QSWO=Website.objects.all().order_by('-name')
     QSWO=Website.objects.all().order_by('url')
     QSWO=Website.objects.all()[2::1]
     
     QSWO= Website.objects.order_by(Length('Topic_name').desc())
     QSWO=Website.objects.order_by(Length('name'))


     d={'QSWO':QSWO}

     return render(request,'display_webpage.html',d)

def display_AccesRecords(request):
     QSAR=Acces_Records.objects.all()
     QSAR=Acces_Records.objects.all().order_by('date')
     QSAR=Acces_Records.objects.all().order_by('author')
     QSAR=Acces_Records.objects.all().order_by('name')
     QSAR=Acces_Records.objects.order_by(Length('name'))
     QSAR=Acces_Records.objects.order_by(Length('author'))



     d={'QSAR':QSAR}
     return render(request,'display_AccesRecords.html',d)





def insert_topic(request):
     Topic_name=input('Enter topic name : ')
     To=topic.objects.get_or_create(Topic_name=Topic_name)[0]
     To.save()
     
     QSTO=topic.objects.all()
     d={'QSTO':QSTO}
     return render(request,'display_topic.html',d)

def insert_Website(request):
     tn=input('Enter topic name : ')
     na=input('Enter Name : ')
     url=input('Enter url : ')
     To=topic.objects.get(Topic_name=tn)
     wo=Website.objects.get_or_create(Topic_name=To,name=na,url=url)[0]
     wo.save()


     QSWO=Website.objects.all()
     d={'QSWO':QSWO}

     return render(request,'display_webpage.html',d)

def insert_Acces_Records(request):
     pk=int(input('Enter topic name with pk : ' ))
     wo=Website.objects.get(pk=pk)
     da=input('Enter date : ')
     au=input('Enter author name : ')
     Asc=Acces_Records.objects.get_or_create(name=wo,date=da,author=au)[0]

     QSAR=Acces_Records.objects.all()
     d={'QSAR':QSAR}
     return render(request,'display_AccesRecords.html',d)
     
     
     


     



     
     
