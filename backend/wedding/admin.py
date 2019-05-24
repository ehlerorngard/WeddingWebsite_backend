from django.contrib import admin
from .models import Invitee, Rsvp, Message

class InviteeAdmin(admin.ModelAdmin): 
	list_display = ('firstName', 'lastName', 'email', 'mobileNumber', 'zipCode', 'attending', 'rsvpSubmitted', 'rsvp')

class RsvpAdmin(admin.ModelAdmin): 
	list_display = ('attending', 'lodging', 'numInviteesAlotted', 'numAdults', 'numChildren', 'arrivalDay', 'departureDay', 'volunteeringToHelp', 'numVeg', 'numNoDairy', 'numNoGluten', 'FridayDinner', 'SaturdayBreakfast', 'SaturdayLunch', 'SaturdayDinner', 'SundayBrunch', 'additionalNotes', 'submitted', 'dateCreated','lastUpdated')

class MessageAdmin(admin.ModelAdmin): 
	list_display = ('firstName', 'lastName', 'email', 'message', 'dateCreated')

# Register models here:
admin.site.register(Invitee, InviteeAdmin)
admin.site.register(Rsvp, RsvpAdmin)
admin.site.register(Message, MessageAdmin)
