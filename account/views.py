from django.shortcuts import render,redirect
from account.forms import *
from .serializers import *
from .models import *
from .tests import send_mailer
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as Logout
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


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

        if user is not None:
            login(request, user)
            return redirect('contact')
        # return whatever you want on failure
        else:
            return Response({'Username or password not correct'})


def logout(request):

    Logout(request)

    return redirect('login')


@login_required
def contact(request):

    if request.method == "GET" and request.GET.get('number') and request.GET.get('message'):

        obj = ContacUs.objects.create(user=request.user,
                                      contact_number=request.GET.get('number'),
                                      comment=request.GET.get('message'))
        obj.save()
        if obj:
            print(request.user.email)
            send_mailer(request.user.email)

            return JsonResponse({'success': True})

        else:
            return JsonResponse({'success': False})


    return render(request, "contactus.html")