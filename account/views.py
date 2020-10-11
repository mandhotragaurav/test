from django.shortcuts import render,redirect
from account.forms import *
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import login, authenticate
from rest_framework.response import Response


# Create your views here.
class RegistrationView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class loginView(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password'))
        print(request.data.get('username'),request.data.get('password'))
        if user is not None:
            login(request, user)
            return redirect('contact')
        # return whatever you want on failure
        else:
            return Response({'Username or password not correct'})






def contact(request):


    form =

    return render(request, "contactus.html")