from django.shortcuts import render

# Create your views here.
def food(request):
    context ={
        '피자' : '피자',
        '치킨' : '치킨',
        '국밥' : '국밥',
        '초밥' : '초밥',
        '민초흑당로제마라탕' : '민초흑당로제마라탕'
    }
    return render(request, 'menus/food.html', context)

def drink(request):
    context ={
        'Cider' : 'Cider',
        'Coke' : 'Coke',
        'Miranda' : 'Miranda',
        'Fanta' : 'Fanta',
        'Eye_of_finetree' : 'Eye of finetree',
    }
    return render(request, 'menus/drink.html', context)

def receipt(request):
    order = request.GET.get('message')
    context ={
        'order' : order,
        'lst' : ['피자',
        '치킨',
        '국밥',
        '초밥',
        '민초흑당로제마라탕',
        'Cider',
        'Coke',
        'Miranda',
        'Fanta',
        'Eye of finetree']
    }
    return render(request, 'menus/receipt.html', context)