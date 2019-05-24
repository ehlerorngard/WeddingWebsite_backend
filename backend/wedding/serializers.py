from rest_framework import serializers
from .models import Invitee, Rsvp, Message

# specify fields to be converted to JSON:

class InviteeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invitee
    fields = ('id', 'firstName', 'lastName', 'email', 'mobileNumber', 'zipCode', 'attending', 'rsvpSubmitted', 'rsvp')

class RsvpSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rsvp
    fields = ('id', 'attending', 'lodging', 'numInviteesAlotted', 'numAdults', 'numChildren', 'arrivalDay', 'departureDay', 'volunteeringToHelp', 'numVeg', 'numNoDairy', 'numNoGluten', 'additionalNotes', 'FridayDinner', 'SaturdayBreakfast', 'SaturdayLunch', 'SaturdayDinner', 'SundayBrunch', 'submitted', 'dateCreated','lastUpdated')

class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('id', 'firstName', 'lastName', 'email', 'message', 'dateCreated')