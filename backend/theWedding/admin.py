from django.contrib import admin
from .models import Invitee, Rsvp, Task

class InviteeAdmin(admin.ModelAdmin): 
	list_display = ('firstName', 'lastName', 'email', 'mobileNumber', 'rsvpSubmitted', 'rsvp')

class RsvpAdmin(admin.ModelAdmin): 
	list_display = ('attending', 'lodging', 'numInviteesAlotted', 'numAdults', 'numChildren', 'othersNames', 'arrivalDay', 'departureDay', 'volunteeringToHelp', 'numVeg', 'numNoDairy', 'numNoGluten', 'additionalNotes', 'needTent', 'needPad', 'needSleepingBag', 'submitted', 'lastUpdated')

class TaskAdmin(admin.ModelAdmin): 
	list_display = ('summary', 'description', 'category', 'day', 'duration', 'startTime', 'endTime', 'idealTotalNumWorkers', 'numWorkersNeeded')

# Register models here:
admin.site.register(Invitee, InviteeAdmin)
admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Task, TaskAdmin)
