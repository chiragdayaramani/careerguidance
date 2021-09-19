from core.models import After10, After12Arts, After12Commerce, After12Science
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    count=User.objects.count()
    context={
        'count':count,
    }
    return render(request,'home.html',context)

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=  UserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)

@login_required
def after10(request):
    questions=After10.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after10.html',context)

@login_required
def after12arts(request):
    questions=After12Arts.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12.html',context)

@login_required
def after12commerce(request):
    questions=After12Commerce.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12.html',context)

@login_required
def after12science(request):
    questions=After12Science.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12.html',context)
