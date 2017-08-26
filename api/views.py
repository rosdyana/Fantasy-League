from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializer import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class =  GroupSerializer