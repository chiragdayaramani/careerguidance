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
    return render(request, 'after10.html')
