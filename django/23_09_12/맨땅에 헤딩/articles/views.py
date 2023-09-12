from django.shortcuts import render

# Create your views here.
# 함수 모음
def index(request):
    print("1")
    return render(request, 'articles/index.html')