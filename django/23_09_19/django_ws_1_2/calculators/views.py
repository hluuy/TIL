from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):

        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        num1 = int(num1)
        num2 = int(num2)

        context = {
            'num1' : num1,
            'num2' : num2
        }
        
        return render(request, 'calculators/result.html', context)