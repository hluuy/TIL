import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    empty_list = []
    context = {
        'foods' : foods, # 일반적으로 둘의 이름을 맞춰주는게 좋다
        'picked' : picked,
        'empty_list' : empty_list
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')