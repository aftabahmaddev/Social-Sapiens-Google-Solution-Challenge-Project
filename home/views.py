from django.shortcuts import render, HttpResponse
from .models import post
from .forms import post_form
def home(request):
    
    return render(request,'home/home.html')
def login(request):
    posts=post.objects.all()
    
    if request.method=='POST':
        return
    else:
        
        context={
            'post':posts
        }
        return render(request,'home/all-cases.html',context)
def signup(request):
    Form=post_form(request.POST or None)
    if request.method=='POST':
        if Form.is_valid():
            Form.save()
            return
    else:
        context={
            'form': Form
        }
        return render(request,'home/register.html', context)

def case_deatils(request,name):
    case=post.objects.get(name=name)
    context={
        'case':case
    }
    return render(request,'home/case-des.html', context)