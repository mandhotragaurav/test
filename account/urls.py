from django.urls import path
from .views import *

urlpatterns = [

    # customer


    path('', loginView.as_view(), name='login'),
    path('signup', RegistrationView.as_view(), name='signup'),
    path('logout', logout, name='logout'),
    path('contact/', contact, name='contact'),

]


