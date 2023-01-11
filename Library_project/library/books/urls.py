from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_index, name='book_index'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<author>/', views.book_author, name='book_author'),
]
