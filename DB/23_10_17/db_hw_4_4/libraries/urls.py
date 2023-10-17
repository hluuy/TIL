from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_pk>/', views.book_detail, name='book_detail'),
    path('<int:book_pk>/reviews/', views.review_create, name='review_create'),
    path('<int:book_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
]