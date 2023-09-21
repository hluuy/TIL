from django.shortcuts import render
import random

# Create your views here.
def certification1(request):
    name = 'Kim happy'
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : random.choice(age),
        'grade' : random.choice(grade)
    }
    return render(request, 'certifications/certification1.html', context)

def certification2(request):
    name = 'Park happy'
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : random.choice(age),
        'grade' : random.choice(grade)
    }
    return render(request, 'certifications/certification2.html', context)

def certification3(request):
    name = 'Lee happy'
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'name' : name,
        'age' : random.choice(age),
        'grade' : random.choice(grade)
    }
    return render(request, 'certifications/certification3.html', context)