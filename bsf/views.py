from django.shortcuts import render
from django.http.response import JsonResponse

from users.models import User
from .models import Batch, Net

from .serializer import BatchSerializers, NetSerializers

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/batch/', 
        '/net/', 
    ]
    return Response(routes)

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def Batchs(request):
    user = request.user

    if request.method == 'GET':
        dbData= Batch.objects.all().order_by('id')
        if dbData:
            Serializers = BatchSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = Batch.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = Batch.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = BatchSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    

    
    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = BatchSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = Batch.objects.get(id=request.data["id"])
            if obj:
                # Update the fields dynamically from request.data
                for field, value in request.data.items():
                    if hasattr(obj, field) and value is not None:
                        setattr(obj, field, value)
                        
                for field, file in request.FILES.items():
                    if hasattr(obj, field) and file is not None:
                        setattr(obj, field, file)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            obj.save()  # Save the profile
            msg = {"msg": "Sucessfully Updated!!!"}
            return Response(msg)
        
        else: 
            return JsonResponse(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        Serializers = BatchSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Batch.objects.get(id=data["id"])
            if obj:
                    obj.delete()
                    msg = {"msg" : "Deleted Sucessfully!!!"}
                    return Response(msg)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
 

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def Lays(request):
    user = request.user

    if request.method == 'GET':
        dbData= Batch.objects.all().order_by('id')
        if dbData:
            Serializers = BatchSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = Batch.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = Batch.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = BatchSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    

    
    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = BatchSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = Batch.objects.get(id=request.data["id"])
            if obj:
                # Update the fields dynamically from request.data
                for field, value in request.data.items():
                    if hasattr(obj, field) and value is not None:
                        setattr(obj, field, value)
                        
                for field, file in request.FILES.items():
                    if hasattr(obj, field) and file is not None:
                        setattr(obj, field, file)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            obj.save()  # Save the profile
            msg = {"msg": "Sucessfully Updated!!!"}
            return Response(msg)
        
        else: 
            return JsonResponse(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        Serializers = BatchSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Batch.objects.get(id=data["id"])
            if obj:
                    obj.delete()
                    msg = {"msg" : "Deleted Sucessfully!!!"}
                    return Response(msg)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
 

@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def Nets(request):
    user = request.user

    if request.method == 'GET':
        dbData= Net.objects.all().order_by('id')
        if dbData:
            Serializers = NetSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = Net.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = Net.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = NetSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    

    
    elif request.method == 'PATCH':

        #To Do
            # avoid duplicate netNumbers while editing.
            # netNumber can also be alphabets ???

        #data = JSONParser().parse(request)
        Serializers = NetSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = Net.objects.get(id=request.data["id"])
            if obj:
                # Update the fields dynamically from request.data
                for field, value in request.data.items():
                    if hasattr(obj, field) and value is not None:
                        setattr(obj, field, value)
                        
                for field, file in request.FILES.items():
                    if hasattr(obj, field) and file is not None:
                        setattr(obj, field, file)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            obj.save()  # Save the profile
            msg = {"msg": "Sucessfully Updated!!!"}
            return Response(msg)
        
        else: 
            return JsonResponse(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        Serializers = NetSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Net.objects.get(id=data["id"])
            if obj:
                    obj.delete()
                    msg = {"msg" : "Deleted Sucessfully!!!"}
                    return Response(msg)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)

    
'''
@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def Batchs(request):
    user = request.user

    if request.method == 'GET':
        dbData= Batch.objects.all().order_by('id')
        if dbData:
            Serializers = BatchSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = Batch.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = Batch.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = BatchSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    

    
    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = BatchSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = Batch.objects.get(id=request.data["id"])
            if obj:
                # Update the fields dynamically from request.data
                for field, value in request.data.items():
                    if hasattr(obj, field) and value is not None:
                        setattr(obj, field, value)
                        
                for field, file in request.FILES.items():
                    if hasattr(obj, field) and file is not None:
                        setattr(obj, field, file)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

            obj.save()  # Save the profile
            msg = {"msg": "Sucessfully Updated!!!"}
            return Response(msg)
        
        else: 
            return JsonResponse(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        Serializers = BatchSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Batch.objects.get(id=data["id"])
            if obj:
                    obj.delete()
                    msg = {"msg" : "Deleted Sucessfully!!!"}
                    return Response(msg)
            else:
                msg = {"msg" : "Record Not Found"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
 
'''