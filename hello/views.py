from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Newthing


def hello(request):
    newthing = Newthing.objects
    return render(request,'hello.html',{'newthing':newthing})


def create(request):
    return render(request, 'create.html')

def send(request):
    newthing = Newthing()
    newthing.title = request.GET['titletitle']
    newthing.pubdate = timezone.datetime.now()
    newthing.body = request.GET['body']
    newthing.save()
    return redirect('hello')

def detail(request, post_pk):
    post = get_object_or_404(Newthing, pk=post_pk)
    return render(request, 'detail.html',{'postnumb':post})

def home(request):
    return render(request,'home.html')