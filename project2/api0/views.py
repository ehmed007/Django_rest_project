from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from .models import student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.
@csrf_exempt
@api_view(["GET","POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    stu = student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer_data.data)
    # return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializer_data.data,safe=False)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST','GET','PUT'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def home1(request, pk):
    print()
    try:
        stu = student.objects.get(pk=pk)
        serializer_data = StudentSerializer(stu)
        # json_data = JSONRenderer().render(serializer_data.data)
        data = serializer_data.data
    except:
        print('hello')
        data = {'error':'no data exist'}
    # return JsonResponse(data, safe=False)
    return Response(data)


@csrf_exempt
@api_view(['POST'])
def create_student(request):    
    # this is deserialization
    print(request.method)
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serialized_data = StudentSerializer(data=pythondata)

        if serialized_data.is_valid():
            serialized_data.save()
            data = {'msg':'student created'}
            return JsonResponse(data, safe=False)
            
        # return JsonResponse(serialized_data.errors,safe=False)
        return Response(serialized_data.errors)
    data = {'msg':'request should be post'}
    # return JsonResponse(data, safe=False)
    return Response(data)


@csrf_exempt
@api_view(['PUT','GET'])
def update_student(request):

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = student.objects.get(id=id)
        # for parital update
        serialized_data = StudentSerializer(stu, data=pythondata, partial=True)

        # for full update
        # serialized_data = StudentSerializer(stu, data=pythondata)

        if serialized_data.is_valid():
            serialized_data.save()
            data = {'msg':'data updated'}
            # return JsonResponse(data, safe=False)
            return Response(data)
            
        # return JsonResponse(serialized_data.errors,safe=False)
        return Response(serialized_data.data)
    data = {'msg':'request should be PUT'}
    # return JsonResponse(data, safe=False)
    return Response(data)

@csrf_exempt
@api_view(['DELETE'])
def delete_student(request):

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        try:
            stu = student.objects.get(id=id)
            stu.delete()
            data = {'msg':'data deleted'}
            # return JsonResponse(data, safe=False)
            return Response(data)
        except:
            data = {'msg':'data not found'}
            # return JsonResponse(data, safe=False)
            return Response(data)
            
    data = {'msg':'request should be DELETE'}
    # return JsonResponse(data, safe=False)
    return Response(data)