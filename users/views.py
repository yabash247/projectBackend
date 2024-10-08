from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from users.models import User, Profile, Contacts

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.tokens import default_token_generator

from users.serializer import MyTokenObtainPairSerializer, RegisterSerializer, ProfileViewSerializers, ProfileEditSerializers
from users.serializer import ContactSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes

from rest_framework.parsers import JSONParser


def construct_frontend_url(path):
    return settings.FRONTEND_BASE_URL + path

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

def get_tokens_for_user(user):
   refresh = RefreshToken.for_user(user)

   return {
     'refresh': str(refresh),
     'access': str(refresh.access_token),
   }

@api_view(['POST'])
@permission_classes([AllowAny])
class LoginView(APIView):
   def post(request):
       email= request.data.get["email"]
       password = request.data.get["password"]

       user = authenticate(email=email,password=password)
       if user:
           return Response(get_tokens_for_user(user))
       if email: 
           user_by_email = User.objects.filter(email=email).first()
           if not user_by_email:
                return Response({'detail': 'Email Dose not Exist'}, status=status.HTTP_400_BAD_REQUEST)
       return Response({"error":"email or password isincorrect!"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
   

#Login User with Checks
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    class MyTokenObtainPairView(TokenObtainPairView):
        serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/users/token/',
        '/users/register/',
        '/users/token/refresh/',
        '/users/profile/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    pre = request
    if request.method == 'GET':
        data = f"Congrats {request.user.username}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation to you, your API just responded to POST request with text: {text}'
        return Response({'response': data},  status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        data = f"Congratulations {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get("text")
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def UserProfile(request):
    user = request.user

    if request.method == 'GET':
        try:
            obj = Profile.objects.get(id=user.id)
            if obj:
                Profile_Serializers = ProfileViewSerializers(obj, many=False)
                msg = {"msg" : "Your profile is ready for viewing", "data" : Profile_Serializers.data, "userEmail" : user.email, "isSuperUser" :request.user.is_superuser}
                return JsonResponse(msg, safe=False)
        except:
            msg = {"msg" : "Wow thats Strange!!!, profile not found. Please refresh page and try again"}
            return JsonResponse(ProfileViewSerializers.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)


    elif request.method == 'POST':
        Profile_Serializers = ProfileEditSerializers(user, data=request.data, partial=True)
        if Profile_Serializers.is_valid():
            try:
                # Get the existing profile
                obj = Profile.objects.get(id=user.id)
                
                # Update the fields dynamically from request.data
                for field, value in request.data.items():
                    if hasattr(obj, field) and value is not None:
                        setattr(obj, field, value)
                    
                for field, file in request.FILES.items():
                    if hasattr(obj, field) and file is not None:
                        setattr(obj, field, file)

                obj.save()  # Save the profile
                msg = {"msg": "Your profile has been updated!"}
                return Response(msg)

            except Profile.DoesNotExist:
                msg = {"msg": "Wow thats Strange!!!, profile not found. Please refresh page and try again"}
                return Response(msg, status=status.HTTP_404_NOT_FOUND)

        else: 
            print('error serializing data')
            return JsonResponse(Profile_Serializers.errors, status=status.HTTP_400_BAD_REQUEST)

            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user

    serializer = ProfileEditSerializers(user, data=request.data, partial=True)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data)
        except:
            return Response('Did not update profile')
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    current_password = request.data.get('oldPassword', '').strip()
    new_password = request.data.get('newPassword', '')
    repeat_new_password = request.data.get('repeatNewPassword', '')
    if new_password != repeat_new_password:
        return Response({'detail': 'New passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            if not user.check_password(current_password):
                return Response({'detail': 'Current password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user.set_password(new_password)
                user.save()
                return Response({'detail': 'Password changed successfully.'})
        except Exception as e:
            return Response({'detail': 'Failed to change password. Please try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    email = request.data.get('email')
    username = request.data.get('username')  # Assuming username is also provided in the request

    if not email or not username:
        return JsonResponse({'detail': 'Please provide both email and username'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Fetch user based on email and username
        user = User.objects.get(email=email, username=username)

        # Generate a token using default_token_generator
        token = default_token_generator.make_token(user)

        # Construct reset link with reverse and remove /core/api/
        reset_linkk = construct_frontend_url(reverse('reset_password')) + f'?token={token}&email={email}'
        reset_link = reset_linkk.replace('/users/api', '')

        # Send email with reset link
        send_mail(
            'PASSWORD RESET',
            f'Dear {username}, we have received a request to reset your password. Click the link to reset your password: {reset_link}',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return JsonResponse({'detail': reset_link}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return JsonResponse({'detail': 'User with this email and username combination does not exist'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f'Error sending password reset email: {str(e)}')
        return JsonResponse({'detail': 'An error occurred while sending the password reset link.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def Contact(request):
    user = request.user
    data = JSONParser().parse(request)

    
    if request.method == 'PUT': 
        Serializers = ContactSerializers(data=data)
        if  Serializers.is_valid():
            if  Serializers.save():
                    msg = {"msg" : "sucessfully Added!!!", "data": Serializers.data}
                    return JsonResponse(msg, status=status.HTTP_201_CREATED)
            else:
                msg = {"msg" : "Wired! Could not save. Please try again"}
                return JsonResponse(msg, status=status.HTTP_406_NOT_ACCEPTABLE)  
        else:
            return JsonResponse(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    elif request.method == 'POST':
        dbData = []
        if (data["id"] > 0):
            dbData = Contacts.objects.filter(id=data["id"]).order_by('id').reverse()
        else:
             dbData = Contacts.objects.all().order_by('id').reverse()
        if dbData:
            Serializers = ContactSerializers(dbData, many=True)
            msg = {"msg" : "Successful!!!", "data" : Serializers.data}
            return JsonResponse(msg)
        else:
            msg = {"msg" : "Requested Data dosen't exisit"}
            return JsonResponse(msg, status=status.HTTP_404_NOT_FOUND)    
        
    elif request.method == 'DELETE':
        try:
            obj = Contacts.objects.get(id=data["id"])
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


''' 

    Sample 

    @api_view(['GET', 'POST', 'PUT'])
    @permission_classes([IsAuthenticated])
    def Contact(request):
        user = request.user
        data = JSONParser().parse(request)

        if request.method == 'PUT': 
            #Check if requestor has permission to create new contact 
            #if not data["userId"]:
                #return JsonResponse({'detail': 'Please provide both email and username'}, status=status.HTTP_400_BAD_REQUEST)
            Serializers = ContactSerializers(data=data)
            if  Serializers.is_valid():
                if  Serializers.save():
                        msg = {"msg" : "sucessfully Added!!!", "data": Serializers.data}
                        return JsonResponse(msg, status=status.HTTP_201_CREATED)
                else:
                    msg = {"msg" : "Wired! Could not save. Please try again"}
                    return JsonResponse(msg, status=status.HTTP_406_NOT_ACCEPTABLE)  
            else:
                return JsonResponse(Serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
'''
