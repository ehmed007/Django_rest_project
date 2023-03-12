from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# Create your views here.


@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAdminUser])
def home(request):
    if request.method == 'GET':
        data = Student.objects.all()
        data = StudentSerializers(data, many=True)
        data = data.data
        return Response(data)
    data = {'msg':'request should be GET'}
    return Response(data)