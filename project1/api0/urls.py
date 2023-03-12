from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
    # path('',views.home),
    # path('<int:pk>',views.home1),
    # path('create_student/',views.create_student),
    # path('update_student/',views.update_student),
    # path('delete_student/',views.delete_student),
]