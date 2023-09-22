from throw_catch import views
from django.urls import path

urlpatterns = [
    path('first/', views.first),
    path('second/', views.second)
]