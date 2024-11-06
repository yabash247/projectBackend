#from django.shortcuts import render
from django.http.response import JsonResponse

#from users.models import User
from .models import Batch, Net, NetStat, Container, ContainerStat, Authority, StaffCurrent, StaffOrgChart

from .serializer import BatchSerializers, NetSerializers, NetStatSerializers, ContainerSerializers, ContainerStatSerializers, StaffOrgChartSerializers, StaffCurrentSerializers, AuthoritySerializers

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

# Create your views here.

def checkAuthorized (tbName, staffId, requestType):

    #tableName in Authority Table?
    inAutTable = Authority.objects.filter(tableName=tbName)
    if inAutTable:
        #get requestType Level
        #get staff current level
        #if staffLevel => requestLevel
            #return true
        #else
            #return false
        return True
    else :
        #Check if user is company or farm creator, else do not grant premission requested.
        return False




@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/batch/',
        '/net/',
    ]
    return Response(routes)


@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([AllowAny])
def Authorities(request):
    user = request.user

    if request.method == 'GET':

        data = JSONParser().parse(request)
        #get Staff Id using CompanyId, farmId and UserId
        isStaff = StaffCurrent.objects.filter(staffId=data["staffId"])
        if isStaff:

            if checkAuthorized(data["tableName"], data["staffId"], 'GET') == True:
                dbData= Authority.objects.all().order_by('id')
                if dbData:
                    Serializers = AuthoritySerializers(dbData, many=True)
                    msg = {"msg" : "Sucessfull", "data" : Serializers.data}
                    return JsonResponse(msg, status=status.HTTP_200_OK)
                else:
                    msg = {"msg" : "No Data Found"}
                    return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
            else:
                #check if user us valid staff
                msg = {"msg" : "CHECK IS FALSE"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        else:
            #check if user us valid staff
            msg = {"msg" : "Not Authorized, Non-Staff, "}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)



    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = Authority.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = Authority.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = AuthoritySerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)




    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = AuthoritySerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = Authority.objects.get(id=request.data["id"])
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
        Serializers = AuthoritySerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Authority.objects.get(id=data["id"])
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
def StaffCurrents(request):
    user = request.user

    if request.method == 'GET':
        dbData= StaffCurrent.objects.all().order_by('id')
        if dbData:
            Serializers = StaffCurrentSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = StaffCurrent.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = StaffCurrent.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = StaffCurrentSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = StaffCurrentSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = StaffCurrent.objects.get(id=request.data["id"])
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
        Serializers = StaffCurrentSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = StaffCurrent.objects.get(id=data["id"])
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
def StaffOrgCharts(request):
    user = request.user

    if request.method == 'GET':
        dbData= StaffOrgChart.objects.all().order_by('id')
        if dbData:
            Serializers = StaffOrgChartSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = StaffOrgChart.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = StaffOrgChart.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = StaffOrgChartSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = StaffOrgChartSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = StaffOrgChart.objects.get(id=request.data["id"])
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
        Serializers = StaffOrgChartSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = StaffOrgChart.objects.get(id=data["id"])
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
        Serializers = BatchSerializers(user, data=request.data, partial=True) #need too update if serializer is invalid.
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
def NetStatus(request):
    user = request.user

    if request.method == 'GET':
        dbData= NetStat.objects.all().order_by('id')
        if dbData:
            Serializers = NetStatSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = NetStat.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = NetStat.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = NetStatSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = NetStatSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = NetStat.objects.get(id=request.data["id"])
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
        Serializers = NetStatSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = NetStat.objects.get(id=data["id"])
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


@api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
@permission_classes([IsAuthenticated])
def Containers(request):
    user = request.user

    if request.method == 'GET':
        dbData= Container.objects.all().order_by('id')
        if dbData:
            Serializers = ContainerSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = Container.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = Container.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = ContainerSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = ContainerSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = Container.objects.get(id=request.data["id"])
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
        Serializers = ContainerSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Container.objects.get(id=data["id"])
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
def ContainerStats(request):
    user = request.user

    if request.method == 'GET':
        dbData= ContainerStat.objects.all().order_by('id')
        if dbData:
            Serializers = ContainerStatSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfull", "data" : Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No Data Found"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["id"] == 0):
            dbData = ContainerStat.objects.all().order_by('id')
        elif(data["id"] > 0):
            dbData = ContainerStat.objects.filter(id=data["id"]).order_by('id').reverse()

        if dbData:
            Serializers = ContainerStatSerializers(dbData, many=True)
            msg = {"msg" : "Sucessfully Retrived !!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Data not found !!!"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'PATCH':

        #data = JSONParser().parse(request)
        Serializers = ContainerStatSerializers(user, data=request.data, partial=True)
        if Serializers.is_valid():
            obj = ContainerStat.objects.get(id=request.data["id"])
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
        #****batchNumber should be only unique to the particular farm.
        #Flag to manager when removed date is added the same time as when container status is created.
        data = JSONParser().parse(request)
        Serializers = ContainerStatSerializers(data=data)
        if Serializers.is_valid():
            Serializers.save()
            msg = {"msg" : "Created Sucessfully!!! ", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = ContainerStat.objects.get(id=data["id"])
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