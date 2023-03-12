from django.shortcuts import render

from django.http import HttpResponse, JsonResponse, response
from .models import student
from .serializers import StudentSerializer
from rest_framework.response import Response

from rest_framework import decorators
from rest_framework import permissions
from rest_framework import authentication
# Create your views here.

@decorators.api_view(['GET'])
@decorators.authentication_classes([authentication.SessionAuthentication])
@decorators.permission_classes([permissions.IsAuthenticated])
def home(request):
    if request.method == 'GET':
        stu = student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    data = {'msg':'request should be GET'}
    return Response()
