from django.shortcuts import render
from rest_framework import viewsets    
from .serializers import InviteeSerializer, RsvpSerializer, MessageSerializer
from .models import Invitee, Rsvp, Message               


class RsvpView(viewsets.ModelViewSet): 
	serializer_class = RsvpSerializer    
	queryset = Rsvp.objects.all()

class InviteeView(viewsets.ModelViewSet):
	serializer_class = InviteeSerializer

	def get_queryset(self):
		queryset = Invitee.objects.all()

		# Check to see if "?rsvp=" is included in the query parameters:
		rsvp = self.request.query_params.get('rsvp', None)

		# If an RSVP id is included, filter invitees by their foreign key "rsvp":
		if rsvp is not None:
			queryset = queryset.filter(rsvp=rsvp) # queryset = queryset.filter(rsvp__id=rsvp)
		return queryset

class MessageView(viewsets.ModelViewSet): 
	serializer_class = MessageSerializer    
	queryset = Message.objects.all()



# for enabling requests with CSRF tokens:
from django.http import JsonResponse
from django.middleware.csrf import get_token

def csrf(request):
    return JsonResponse({'csrftoken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})
