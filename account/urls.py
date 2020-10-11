from django.urls import path
from .views import *

urlpatterns = [

    # customer

    path('signup', RegistrationView.as_view()),
    path('', loginView.as_view()),
    path('contact/', contact, name='contact'),

]


