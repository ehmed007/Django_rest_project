from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('<int:pk>/',views.home1),
    path('create_student/',views.create_student),
    path('update_student/',views.update_student),
    path('delete_student/',views.delete_student),
]