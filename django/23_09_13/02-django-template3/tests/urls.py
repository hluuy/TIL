from django.urls import path
from . import views

app_name = 'tests'
urlpatterns = [
    path('index/', views.index, name="index"),
]