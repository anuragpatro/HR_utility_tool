from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    return render(request,'home.html')

def show_data(request):
    people=Person.objects.filter(status='yes')
    return render(request,'person.html',{'employees' : people})

def admin(request):
    return render(request,'base.html')