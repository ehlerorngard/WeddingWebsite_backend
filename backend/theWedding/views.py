from django.shortcuts import render
from rest_framework import viewsets    
from .serializers import InviteeSerializer, RsvpSerializer, TaskSerializer
from .models import Invitee, Rsvp, Task               

class InviteeView(viewsets.ModelViewSet): 
  serializer_class = InviteeSerializer    
  queryset = Invitee.objects.all()

class RsvpView(viewsets.ModelViewSet): 
  serializer_class = RsvpSerializer    
  queryset = Rsvp.objects.all()

class TaskView(viewsets.ModelViewSet): 
  serializer_class = TaskSerializer    
  queryset = Task.objects.all()