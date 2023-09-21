from django.shortcuts import render

# Create your views here.
def food(request):
    return render(request, 'menus/food.html')

def drink(request):
    return render(request, 'menus/drink.html')

def receipt(request):
    return render(request, 'menus/receipt.html')