from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('<int:pk>/',views.home1),
]
