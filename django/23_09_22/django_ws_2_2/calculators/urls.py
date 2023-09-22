from calculators import views
from django.urls import path

urlpatterns = [
    path('calculator/<int:num1>/<int:num2>/', views.calculator)
]
