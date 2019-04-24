from django.shortcuts import render
from rest_framework import viewsets    
from .serializers import InviteeSerializer, RsvpSerializer#, TaskSerializer
from .models import Invitee, Rsvp#, Task               

class InviteeView(viewsets.ModelViewSet): 
  serializer_class = InviteeSerializer    
  queryset = Invitee.objects.all()

class RsvpView(viewsets.ModelViewSet): 
  serializer_class = RsvpSerializer    
  queryset = Rsvp.objects.all()

# class TaskView(viewsets.ModelViewSet): 
#   serializer_class = TaskSerializer    
#   queryset = Task.objects.all()



# for enabling of CSRF tokens
from django.http import JsonResponse
from django.middleware.csrf import get_token

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})


