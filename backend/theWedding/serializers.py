from rest_framework import serializers
from .models import Invitee, Rsvp, Task

# specify fields to be converted to JSON:

class InviteeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invitee
    fields = ('id', 'firstName', 'lastName', 'email', 'mobileNumber', 'rsvpSubmitted', 'rsvp')

class RsvpSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rsvp
    fields = ('attending', 'lodging', 'numInviteesAlotted', 'numAdults', 'numChildren', 'otherNames', 'arrivalDay', 'departureDay', 'volunteeringToHelp', 'numVeg', 'numNoDairy', 'numNoGluten', 'additionalNotes', 'needTent', 'needPad', 'needSleepingBag', 'submitted', 'lastUpdated')

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ('summary', 'description', 'category', 'day', 'duration', 'startTime', 'endTime', 'idealTotalNumWorkers', 'numWorkersNeeded', 'volunteers')