from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('more-info/', views.info)
]
