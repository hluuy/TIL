from menus import views
from django.urls import path

urlpatterns = [
    path('food/', views.food),
    path('drink/', views.drink),
    path('receipt/', views.receipt)
]