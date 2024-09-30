from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponse
from users.models import User
from .models import Project, MyProjects, Company, Ponds, Stocking, PondstoDoList, Sales, activityNames, stockSource, Staff, Items, Expense, ExpensesDisbursement

from projects.serializer import ProjectsTemplates, MyProjectsTemplates, CompanySerializersGet, CompanySerializersPost, PondSerializers, stockSourceSerializers, GetStockingSerializers
from projects.serializer import StockingSerializers, PondstoDoListSerializers, SaleSerializers, activityNamesSerializers, createActivityNameSerializers, activityNameIdSerializers
from projects.serializer import staffSerializers, ItemsSerializers, EspensesSerializers, ExpensesDisbursementSerializers

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from rest_framework.parsers import JSONParser

from rest_framework import status

from enum import Enum

# Create your views here.


class test(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        try:
            data = request.data
            password = data['password']

            if password == 'pass':
                return Response(
                                {'success': 'User created successfully'},
                                status=status.HTTP_201_CREATED
                            )
            else:
                return Response(
                                {'Failed': 'Password is Incorrect'},
                                status=status.HTTP_201_CREATED
                            )

        except:
            return Response(
                {'error': 'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


   

@api_view(['GET'])
def getRoutes(request):
    routes = [

        '/projects/Project/', #resturns a list from project table.
        '/projects/addProject/',
        '/projects/createProject/',
        '/projects/editProject/',
        '/projects/deleteProject/',

        '/projects/show_myProjects/', #Shows all of user's projects.
        '/projects/show_myProjects/projectId', #Get details on a specific project by project Id provided in http header.
        '/projects/show_myProjects/projectId/ponds',
        '/projects/show_myProjects/projectId/ponds/create',
        '/projects/show_myProjects/projectId/ponds/pondId/edit',
        '/projects/show_myProjects/projectId/ponds/pondId/waterChange', 
        '/projects/show_allProject_template/',
        '/projects//',
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myProject(request):
    user = request.user
    project = MyProjects.objects.filter(userId=user.id)
    #project = MyProjects.objects.all()
    serializer = MyProjectsTemplates(project, many=True)
        #foreach :
            #projectDetails = Project.objects.filter(projectId=id) 
    return Response(serializer.data) #all return 

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Projec(request):
    project = Project.objects.all()
    serializer = ProjectsTemplates(project, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Pond(request):
    data = JSONParser().parse(request)
    user = request.user

    #Get My Projects
    if request.method == 'GET':
        try:
            checkProject = Project.objects.filter(creatorId=user.id, id=data["projectId"]) 
            
            if checkProject: 
                obj = Ponds.objects.filter(projectId=data["projectId"])
                #*** later need to authorize othe employess to view pond
                if not obj:
                    msg = {"msg" : "You haven't added any Ponds yet to the Farm"}
                    return JsonResponse(msg)   
                else:
                    Pond_Serializers = PondSerializers(obj, many=True)
                    msg = {"msg" : "All Ponds In Above Farm", "data" : Pond_Serializers.data}
                    return Response(msg) 
            else:
                msg = {"msg" : "Not Authorized to View Ponds"}
                return JsonResponse(msg, status=status.HTTP_204_NO_CONTENT) 
        except :
                msg = {"msg" : "You haven't created any project yet"}
                return JsonResponse(Pond_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'POST':
        try:
            checkProject = Project.objects.filter(creatorId=user.id, id=data["projectId"]) 
            
            if checkProject: 
                obj = Ponds.objects.filter(projectId=data["projectId"])
                #*** later need to authorize othe employess to view pond
                if not obj:
                    msg = {"msg" : "You haven't added any Ponds yet to the Farm"}
                    return JsonResponse(msg)   
                else:
                    Pond_Serializers = PondSerializers(obj, many=True)
                    msg = {"msg" : "All Ponds In Above Farm", "data" : Pond_Serializers.data}
                    return Response(msg) 
            else:
                msg = {"msg" : "Not Authorized to View Ponds"}
                return JsonResponse(msg, status=status.HTTP_204_NO_CONTENT) 
        except :
                msg = {"msg" : "You haven't created any project yet"}
                return JsonResponse(Pond_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        Pond_Serializers = PondSerializers(data=data)
        if Pond_Serializers.is_valid():
            #****additional checked needed to ensure user is allowed to create ponds for the specific project specified.
            #check if user is proejct creator.
            obj = Project.objects.filter(creatorId=user.id, id=data["projectId"])
            pondExistCheck = Ponds.objects.filter(name=data["name"], projectId=data["projectId"])
            if obj:
                #check if pond already exists
                if pondExistCheck:
                    msg = {"msg" : "Pond Already Exisits", "data" : Pond_Serializers.data}
                    return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)    
                else:
                    Pond_Serializers.save()
                    msg = {"msg" : "Project Created", "data" : Pond_Serializers.data}
                    return JsonResponse(msg, status=status.HTTP_201_CREATED) 
            else:
                msg = {"msg" : "You do not have the Authority to create Ponds for this Farm", "data" : Pond_Serializers.data}
                return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)  
        else:
            msg = {"msg" : "You haven't created any project yet"}
            return JsonResponse(Pond_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        try:
            obj = Ponds.objects.get(id=data["id"], projectId=data["projectId"])
            checkProject = Project.objects.filter(creatorId=user.id, id=data["projectId"]) 
            if checkProject: 
                obj.delete()
                msg = {"msg" : "Pond  Has been deleted"}
                return Response(msg)
            else :
                msg = {"msg" : "You do not have the Authority to create Ponds for this Farm", "data" : Pond_Serializers.data}
                return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)  
        except Ponds.DoesNotExist:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)   
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Stockings(request):
    user = request.user

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        stockAddData = {
            "pondId" : data["toPondId"],
            'toPondId' : data["toPondId"],
            'fromPondId' : data["fromPondId"],
            'fishId' : data["fishId"],
            'addedQuantity' : data["addedQuantity"],
            'addedWeight' : data["addedWeight"],
            'comments' : data["comments"],
        }
        
        Stocking_Serializers = StockingSerializers(data=stockAddData)
        if Stocking_Serializers.is_valid():
            pondInFarmExist = Ponds.objects.filter(id=stockAddData["pondId"], projectId=data["farmId"])
            if pondInFarmExist:
                checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
                if checkIfAuthorized:
                    #***Need to also check if user had already created simialar/same project.
                    AddStocking_Serializers = StockingSerializers(data=stockAddData)
                    if AddStocking_Serializers.is_valid():
                        AddStocking_Serializers.save()
                        msg = {"msg" : "Project Created", "data" : Stocking_Serializers.data}
                        return JsonResponse(msg, status=status.HTTP_201_CREATED) 
                else:
                    msg = {"msg" : "Something went wrong with form data, Please Try again"}
                    return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST) 
            else:
                msg = {"msg" : "Pond dosen't exisit in Farm slected, select a pond and try again"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(Stocking_Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        pondInFarmExist = Ponds.objects.filter(id=data["pondId"], projectId=data["farmId"])
        if pondInFarmExist:
            checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
            if checkIfAuthorized:
                Stocking_Serializers = StockingSerializers(data=data)
                if Stocking_Serializers.is_valid():
                    Stocking_Serializers.save()
                    msg = {"msg" : "Checking ", "data" : Stocking_Serializers.data}
                    return JsonResponse(msg)
                else:
                    return JsonResponse(Stocking_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            msg = {"msg" : "Pond dosen't exisit in Farm slected, select a pond and try again"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            pondInFarmExist = Ponds.objects.filter(id=data["pondId"], projectId=data["farmId"])
            if pondInFarmExist:
                checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
                if checkIfAuthorized:
                    checkStockingData = Stocking.objects.filter(pondId=data["pondId"]).order_by('id').reverse()
                    if checkStockingData: 
                        Stocking_Serializers = StockingSerializers(checkStockingData, many=True)
                        msg = {"msg" : "All Projects I Cretated", "data" : Stocking_Serializers.data}
                        return JsonResponse(msg, status=status.HTTP_200_OK)
                    else :
                        msg = {"msg" : "No stocking data added to this pond. Add stocking data"}
                        return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
                else:
                    msg = {"msg" : "You are not authorized"}
                    return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            else:
                msg = {"msg" : "Pond dosen't exisit in Farm slected, select a pond and try again"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        except :
                #msg = {"msg" : "You haven't created any project yet", "data" : data["creatorId"]}
                msg = {"msg" : "Hmmm! Something went wrong with server, please try again"}
                return JsonResponse(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Projects(request):
    #data = JSONParser().parse(request)
    user = request.user

    #Get My Projects
    if request.method == 'GET':
        try:
            obj = Project.objects.filter(creatorId=user.id)
            if obj:
                Project_Serializers = ProjectsTemplates(obj, many=True)
                data = {"msg" : "All Projects I Cretated", "data" : Project_Serializers.data}
                return Response(data)
            else:
                data = {"msg" : "You haven't created any project yet",  "data" : ""}
                return Response(data, status= status.HTTP_204_NO_CONTENT)
        except :
                #msg = {"msg" : "You haven't created any project yet", "data" : data["creatorId"]}
                msg = {"msg" : "You haven't created any project yet"}
                return JsonResponse(Project_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Register New Project
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        Project_Serializers = ProjectsTemplates(data=data)
        if Project_Serializers.is_valid():
            if user.id == data["creatorId"]:
                #***Need to also check if user had already created simialar/same project.
                obj = Project.objects.all()
                Project_Serializers.save()
                msg = {"msg" : "Project Created", "data" : Project_Serializers.data}
                return JsonResponse(msg, status=status.HTTP_201_CREATED) 
            else:
                msg = {"msg" : "Something went wrong with form data, Please Try again"}
                return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST) 
        return JsonResponse(Project_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    #update   
    elif request.method == 'POST':
        
        Project_Serializers = ProjectsTemplates(data=data)
        if Project_Serializers.is_valid():
            try:
                #**check if authorized to edit company 
                obj = Company.objects.get(id=data["id"], creatorId=user.id)
                for field, value in data.items():
                    if hasattr(obj, field) and value is not None:
                        setattr(obj, field, value)
                
                obj.save()
                msg = {"msg" : "Found"}
                return Response(msg)
                    
            except Company.DoesNotExist:
                msg = {"msg" : "Company not Found or Not Authorize to edit Company", "data" : data["creatorId"]}
                return Response(msg, status= status.HTTP_404_NOT_FOUND)
        else: 
            return JsonResponse(Project_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = Project.objects.get(id=data["id"], creatorId=user.id)
            obj.delete()
            msg = {"msg" : "Company Info Has been deleted"}
            return Response(msg)
        except Project.DoesNotExist:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def fishSource(request):
    data = JSONParser().parse(request)
    user = request.user

    if request.method == 'POST':
        try:
            checkProject = Project.objects.filter(creatorId=user.id, id=data["farmId"]) 
            
            if checkProject: 
                obj = stockSource.objects.filter(farmId=data["farmId"])
                #*** later need to authorize othe employess to view pond
                if not obj:
                    msg = {"msg" : "You haven't added any Fish Source yet to the Farm"}
                    return JsonResponse(msg)   
                else:
                    fishStock_Serializers = stockSourceSerializers(obj, many=True)
                    msg = {"msg" : "All Fish Source In Above Farm", "data" : fishStock_Serializers.data}
                    return Response(msg) 
            else:
                msg = {"msg" : "Not Authorized to View Fish Source"}
                return JsonResponse(msg, status=status.HTTP_204_NO_CONTENT) 
        except :
                msg = {"msg" : "You haven't created any stocking yet"}
                return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PUT':
        checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
        if checkIfAuthorized:
            fishStock_Serializers = stockSourceSerializers(data=data)
            if fishStock_Serializers.is_valid():
                    fishStock_Serializers.save()
                    msg = {"msg" : "Checking ", "data" : fishStock_Serializers.data}
                    return JsonResponse(msg)
            else:
                    return JsonResponse(fishStock_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
        else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
       
    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Companies(request):
    data = JSONParser().parse(request)
    user = request.user

    if request.method == 'GET':
        if data["id"] > 0:
            #obj = obj.filter(title__icontains=title)
            obj = Company.objects.filter(id=data["id"])
            Company_Serializers = CompanySerializersGet(obj, many=True)
            msg = {"msg" : "Specific Company", "data" : Company_Serializers.data}
            return Response(msg)
        else:
            obj = Company.objects.all()
            Company_Serializers = CompanySerializersGet(obj, many=True)
            msg = {"msg" : "Showing All Com", "data" : Company_Serializers.data}
            return Response(msg)

    #update   
    elif request.method == 'POST':
        
        Company_Serializers = CompanySerializersPost(data=data)
        if Company_Serializers.is_valid():
            try:
                #**check if authorized to edit company 
                obj = Company.objects.get(id=data["id"], creatorId=user.id)
                #turn below to a single array.
                obj.contactName = data["contactName"]
                obj.contactEmail = data["contactEmail"]
                obj.contactPhone = data["contactPhone"]
                obj.instagram = data["instagram"]
                obj.facebook = data["facebook"]
                obj.Address = data["Address"]
                obj.City = data["City"]
                obj.State = data["State"]
                obj.zipCode = data["zipCode"]
                obj.comments = data["comments"]
                obj.save()
                msg = {"msg" : "Found"}
                return Response(msg)
                    
            except Company.DoesNotExist:
                msg = {"msg" : "Company not Found or Not Authorize to edit Company", "data" : data["creatorId"]}
                return Response(msg, status= status.HTTP_404_NOT_FOUND)
        else: 
            return JsonResponse(Company_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    #Register New Company
    elif request.method == 'PUT':
        #**** needs to populate frontend post forn with exsiiting company info first befor user edits.
        Company_Serializers = CompanySerializersPost(data=data)
        if Company_Serializers.is_valid():

            #****Check if company already exist.
            obj = Company.objects.all()
            nameMatches = obj.filter(name__icontains=data["name"]) 

            #Company_Serializers.save()
            #msg = {"msg" : "Company Updated", "data" : Company_Serializers.data}
            msg = {"msg" : "Company Updated", "data" : nameMatches}

            return JsonResponse(msg, status=status.HTTP_201_CREATED) 
        return JsonResponse(Company_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

 
    elif request.method == 'DELETE':
        try:
            obj = Company.objects.get(id=data["id"], creatorId=user.id)
            obj.delete()
            msg = {"msg" : "Company Info Has been deleted"}
            return Response(msg)
        except Company.DoesNotExist:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myPondsToDo(request):
    user = request.user
    taskList = PondstoDoList.objects.filter(requestorId=user.id, status=3).order_by('id')
    taskList_Serializers = PondstoDoListSerializers(taskList, many=True)
    return Response(taskList_Serializers.data)


#staffSerializers
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def StaffData(request):
    user = request.user
    data = JSONParser().parse(request)

    if request.method == 'PUT':
        Staff_Serializers = staffSerializers(data=data)
        if  Staff_Serializers.is_valid():
            if Staff.objects.filter(firstName=data["firstName"], farmId=data["farmId"], lastName=data["lastName"]):
                msg = {"msg" : "Staff Already Exists"}
                return JsonResponse(msg, status=status.HTTP_409_CONFLICT)
            else:
                if  Staff_Serializers.save():
                    msg = {"msg" : "Staff Added"}
                    return JsonResponse(msg, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse(Staff_Serializers.errors, status=status.HTTP_403_FORBIDDEN)  
        else:
            return JsonResponse(Staff_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
        
            
    elif request.method == 'POST':
        if Project.objects.filter(creatorId=user.id, id=data["farmId"]):
            result = Staff.objects.filter(farmId=data["farmId"], status=1).order_by('id')
            if result:
                result_Serializers = staffSerializers(result, many=True)  
                msg = {"msg" : "Staff Data Retrived", "data" : result_Serializers.data}
                return JsonResponse(msg, status=status.HTTP_200_OK)
            else:
                msg = {"msg" : "No Staff Registered to Farm"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    elif request.method == 'DELETE':
        try:
            obj = Staff.objects.get(id=data["id"], farmId=data["farmId"])
            if Project.objects.filter(creatorId=user.id, id=data["farmId"]):
                obj.delete()
                msg = {"msg" : "Task deleted"}
                return Response(msg)
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except Staff.DoesNotExist:
            msg = {"msg" : "Staff do not exist"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def PondToDo(request): 
    user = request.user
    data = JSONParser().parse(request)

    if request.method == 'PUT':
        if Ponds.objects.filter(id=data["pondId"], projectId=data["farmId"]):
            checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
            if checkIfAuthorized:
                #***need to update request.data here before sending too be serialized
                PondTodo_Serializers = PondstoDoListSerializers(data=data)
                if PondTodo_Serializers.is_valid():
                    PondTodo_Serializers.save()
                    msg = {"msg" : "Task Has been sucessfully added ", "data" : PondTodo_Serializers.data}
                    return JsonResponse(msg)
                else:
                    return JsonResponse(PondTodo_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            msg = {"msg" : "Pond dosen't exisit in Farm slected, select a pond and try again"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'POST':
        if Project.objects.filter(creatorId=user.id, id=data["farmId"]):
            taskList = PondstoDoList.objects.filter(farmId=data["farmId"], status=3).order_by('id')
            if taskList:
                taskList_Serializers = PondstoDoListSerializers(taskList, many=True)
                msg = {"msg" : "All Projects I Cretated", "data" : taskList_Serializers.data}
                return JsonResponse(msg, status=status.HTTP_200_OK)
            else:
                msg = {"msg" : "No pending task ecxit for ponds in this farm, That dont seem right"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
    elif request.method == 'DELETE':
        try:
            obj = PondstoDoList.objects.get(id=data["id"])
            if Project.objects.filter(creatorId=user.id, id=data["farmId"]):
                obj.delete()
                msg = {"msg" : "Task deleted"}
                return Response(msg)
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except Company.DoesNotExist:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ActivityNameById(request):
    user = request.user 
    data = JSONParser().parse(request)

    if request.method == 'POST':
        activityN = activityNames.objects.filter(id=data["taskId"])
        if activityN:
            activityNames_Serializers = activityNameIdSerializers(activityN, many=True)
            msg = {"msg" : "All Projects I Cretated", "data" : activityNames_Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "Activity  Do Not Exist"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ActivityName(request):
    
    user = request.user   

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        obj = activityNames.objects.all()
        #***avoid duplicates
        nameMatches = obj.filter(name__icontains=data["name"]).values()
        if(nameMatches):
             msg = {"msg" : "Activity Matches too close to one already existing"}
             return JsonResponse(msg)
        else:
            activityNames_Serializers = activityNamesSerializers(data=data)
            if activityNames_Serializers.is_valid():
                putDATA =  {
                    'name': data['name'],
                    'description': data['description'],
                    'creatorId' : user.id
                } 
                putActivityNames_Serializers = createActivityNameSerializers(data=putDATA) 
                if putActivityNames_Serializers.is_valid(): 
                    if putActivityNames_Serializers.save():
                        msg = {"msg" : "Sucessfully!!. New Activity Name has been created ", "data" : activityNames_Serializers.data}
                        return JsonResponse(msg)
                    else: 
                        return JsonResponse(activityNames_Serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
                else: 
                    return JsonResponse(activityNames_Serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
            else:
                return JsonResponse(activityNames_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
            
    elif request.method == 'POST':

        activityN = activityNames.objects.all().order_by('id')
        if activityN:
            activityNames_Serializers = activityNameIdSerializers(activityN, many=True)
            msg = {"msg" : "All Projects I Cretated", "data" : activityNames_Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No pending task ecxit for ponds in this farm, That dont seem right"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        try:
            obj = activityNames.objects.get(id=data["id"], creatorId=user.id)
            if obj:
                obj.delete()
                msg = {"msg" : "Activity Name has been deleted"}
                return Response(msg)
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Sale(request):
    data = JSONParser().parse(request)
    user = request.user

    if request.method == 'PUT':
        if Ponds.objects.filter(id=data["pondId"], projectId=data["projectId"]):
            if Project.objects.filter(creatorId=user.id, id=data["projectId"]) :
                Sales_Serializers = SaleSerializers(data=data)
                if Sales_Serializers.is_valid():
                    if Sales_Serializers.save():
                        #update stocking.
                        #get where pon
                        msg = {"msg" : "Task Has been sucessfully added ", "data" : Sales_Serializers.data}
                        return JsonResponse(msg)
                    else:
                        return JsonResponse(Sales_Serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
                else:
                    return JsonResponse(Sales_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)  
        else:
            msg = {"msg" : "Pond dosen't exisit in Farm slected, select a pond and try again"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'GET':
        if Project.objects.filter(creatorId=user.id, id=data["projectId"]):
            salesList = Sales.objects.filter(projectId=data["projectId"]).order_by('id')
            if salesList:
                salesList_Serializers = SaleSerializers(salesList, many=True)
                msg = {"msg" : "All Projects I Cretated", "data" : salesList_Serializers.data}
                return JsonResponse(msg, status=status.HTTP_200_OK)
            else:
                msg = {"msg" : "No pending task ecxit for ponds in this farm, That dont seem right"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)    

    elif request.method == 'DELETE':
        try:
            obj = Sales.objects.get(id=data["id"], pondId=data["pondId"])
            if Project.objects.filter(creatorId=user.id, id=data["projectId"]):
                obj.delete()
                msg = {"msg" : "Task deleted"}
                return Response(msg)
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except:
            msg = {"msg" : "Something went wrong"}
            return Response(msg, status= status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Stocks(request):
    user = request.user
    data = JSONParser().parse(request)

    if request.method == 'PUT':
        if Ponds.objects.filter(id=data["pondId"], projectId=data["farmId"]):
            checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
            if checkIfAuthorized:
                #***need to update request.data here before sending too be serialized
                PondTodo_Serializers = PondstoDoListSerializers(data=data)
                if PondTodo_Serializers.is_valid():
                    PondTodo_Serializers.save()
                    msg = {"msg" : "Task Has been sucessfully added ", "data" : PondTodo_Serializers.data}
                    return JsonResponse(msg)
                else:
                    return JsonResponse(PondTodo_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)   
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            msg = {"msg" : "Pond dosen't exisit in Farm slected, select a pond and try again"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def Spends(request):
    user = request.user

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        Espenses_Serializers = EspensesSerializers(data=data)
        if Espenses_Serializers.is_valid():
            checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
            if checkIfAuthorized:
                Espenses_Serializers.save()
                msg = {"msg" : "item group Has been sucessfully added ", "data" : Espenses_Serializers.data}
                return JsonResponse(msg)
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        else:
            return JsonResponse(Espenses_Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
        
        if checkIfAuthorized:
            if (data["id"] > 0):
                expenseData = Expense.objects.filter(id=data["id"]).order_by('id').reverse()
                if expenseData:
                    expense_Serializers = EspensesSerializers(expenseData, many=True)
                    msg = {"msg" : "item group Has been sucessfully added ", "data" : expense_Serializers.data}
                    return JsonResponse(msg)
            else:
                expenseData = Expense.objects.all().order_by('id').reverse()
                if expenseData:
                    expense_Serializers = EspensesSerializers(expenseData, many=True)
                    msg = {"msg" : "item group Has been sucessfully added ", "data" : expense_Serializers.data}
                    return JsonResponse(msg)
                else:
                    msg = {"msg" : "No item group exsits"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
        if (checkIfAuthorized):
            try:
                obj = Expense.objects.get(id=data["id"])
                if obj:
                    obj.delete()
                    msg = {"msg" : "Item Group has been deleted"}
                    return Response(msg)
                else:
                    msg = {"msg" : "You are not authorized"}
                    return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            except:
                msg = {"msg" : "Something went wrong"}
                return Response(msg, status= status.HTTP_404_NOT_FOUND)
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def SpendsDisbursement(request):
    user = request.user

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        ED_Serializers = ExpensesDisbursementSerializers(data=data)
        if ED_Serializers.is_valid():
            checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
            if checkIfAuthorized:
                ED_Serializers.save()
                msg = {"msg" : "item group Has been sucessfully added ", "data" : ED_Serializers.data}
                return JsonResponse(msg)
            else:
                msg = {"msg" : "You are not authorized"}
                return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
        else:
            return JsonResponse(ED_Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


    #Gets disburtment by disbursement id
    elif request.method == 'POST':
        #datatype : 1=byId, 2=byexpenseId, 3=byallocatedToId
        data = JSONParser().parse(request)
        checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
        if checkIfAuthorized:
    

            if(data["dataType"] == 1 & data["id"] > 0):
                expenseData = ExpensesDisbursement.objects.filter(id=data["id"]).order_by('id').reverse()

            elif(data["dataType"] == 2 and data["id"] > 0):
                expenseData = ExpensesDisbursement.objects.filter(expenseId=data["id"]).order_by('id').reverse()

            elif(data["dataType"] == 3 and data["id"] > 0):
                expenseData = ExpensesDisbursement.objects.filter(allocatedToId=data["id"]).order_by('id').reverse()
                
            elif(data["id"] == 0):
                expenseData = ExpensesDisbursement.objects.all().order_by('id')

            if expenseData:
                expense_Serializers = ExpensesDisbursementSerializers(expenseData, many=True)
                msg = {"msg" : "item group Has been sucessfully added ", "data" : expense_Serializers.data}
                return JsonResponse(msg)
            else:
                msg = {"msg" : "Wrong data sent"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    
            
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


    ''' 
    #Gets disburtment by disbursement id
    elif request.method == 'POST':
        #datatype : 1=byId, 2=byexpenseId, 3=byallocatedToId
        data = JSONParser().parse(request)
        checkIfAuthorized = Project.objects.filter(creatorId=user.id, id=data["farmId"])
        if checkIfAuthorized:
            if (data["id"] > 0):
                expenseData = ExpensesDisbursement.objects.filter(id=data["id"]).order_by('id').reverse()
                if expenseData:
                    expense_Serializers = ExpensesDisbursementSerializers(expenseData, many=True)
                    msg = {"msg" : "item group Has been sucessfully added ", "data" : expense_Serializers.data}
                    return JsonResponse(msg)
            else:
                expenseData = ExpensesDisbursement.objects.all().order_by('id')
                if expenseData:
                    expense_Serializers = ExpensesDisbursementSerializers(expenseData, many=True)
                    msg = {"msg" : "item group Has been sucessfully added ", "data" : expense_Serializers.data}
                    return JsonResponse(msg)
                else:
                    msg = {"msg" : "No item group exsits"}
                return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    ''' 


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def ItemsGrouping(request):
    user = request.user
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        if (user.id == 2):
            IG_Serializers = ItemsSerializers(data=data)
            if IG_Serializers.is_valid():
                IG_Serializers.save()
                msg = {"msg" : "item group Has been sucessfully added ", "data" : IG_Serializers.data}
                return JsonResponse(msg)
            else:
                return JsonResponse(IG_Serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        
    elif request.method == 'POST':
        IG_N = Items.objects.all().order_by('id')
        if IG_N:
            IG_Serializers = ItemsSerializers(IG_N, many=True)
            msg = {"msg" : "All Items Group", "data" : IG_Serializers.data}
            return JsonResponse(msg, status=status.HTTP_200_OK)
        else:
            msg = {"msg" : "No item group exsits"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        if (user.id == 2):
            try:
                obj = Items.objects.get(id=data["id"])
                if obj:
                    obj.delete()
                    msg = {"msg" : "Item Group has been deleted"}
                    return Response(msg)
                else:
                    msg = {"msg" : "You are not authorized"}
                    return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
            except:
                msg = {"msg" : "Something went wrong"}
                return Response(msg, status= status.HTTP_404_NOT_FOUND)
        else:
            msg = {"msg" : "You are not authorized"}
            return JsonResponse(msg, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    

    