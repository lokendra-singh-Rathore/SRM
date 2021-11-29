from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import image

def index(request):
    return render(request,'website/index.html')

def About(request):
    return render(request,'website/about.html')


def duplo(request):
    return render(request,'website/duplo.html')

def wedo(request):
    return render(request,'website/wedo.html')

def nxt(request):
    return render(request,'website/nxt.html')

def ev3(request):
    return render(request,'website/ev3.html')

def electronics(request):
    return render(request,'website/electronics.html')

def arduino(request):
    return render(request,'website/arduino.html')

def pi(request):
    return render(request,'website/pi.html')



def gallery(request):
    img=image.objects.all()
    context={'img':img}
    return render(request,'website/gallery.html',context)


