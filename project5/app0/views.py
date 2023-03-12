from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes, throttle_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import authentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(['GET','POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAdminUser])
@throttle_classes([AnonRateThrottle, UserRateThrottle])
def home(request):

    # pagination
    # paginator = PageNumberPagination()
    # paginator.page_size = 1
    # person_objects = Student.objects.all()
    # result_page = paginator.paginate_queryset(person_objects, request)
    # serializer = StudentSerializers(result_page, many=True)
    # return paginator.get_paginated_response(serializer.data)
    
    if request.method == 'GET' or request.method == 'POST':
        data = Student.objects.all()
        data = StudentSerializers(data, many=True)
        data = data.data
        return Response(data)
    data = {'msg':'request should be GET'}
    return Response(data)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAdminUser])
def home1(request,pk):
    try:
        data = Student.objects.get(pk=pk)
        data = StudentSerializers(data)
        data = data.data
    except:    
        data = {'msg':'data not found'}
    return Response(data)