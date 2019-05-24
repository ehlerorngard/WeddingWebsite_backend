from django.db import models

class Rsvp(models.Model):
	attending = models.BooleanField(default=False, null=True, blank=True)
	lodging = models.CharField(max_length=56, null=True, blank=True)
	numInviteesAlotted = models.IntegerField(null=True, blank=True)
	numAdults = models.IntegerField(null=True, blank=True)
	numChildren = models.IntegerField(null=True, blank=True)
	arrivalDay = models.CharField(max_length=10, null=True, blank=True)
	departureDay = models.CharField(max_length=10, null=True, blank=True)
	volunteeringToHelp = models.BooleanField(default=False, null=True, blank=True)
	numVeg = models.IntegerField(null=True, blank=True)
	numNoDairy = models.IntegerField(null=True, blank=True)
	numNoGluten = models.IntegerField(null=True, blank=True)
	FridayDinner = models.BooleanField(default=False, null=True, blank=True)
	SaturdayBreakfast = models.BooleanField(default=False, null=True, blank=True)
	SaturdayLunch = models.BooleanField(default=False, null=True, blank=True)
	SaturdayDinner = models.BooleanField(default=False, null=True, blank=True)
	SundayBrunch = models.BooleanField(default=False, null=True, blank=True)
	additionalNotes = models.CharField(max_length=600, null=True, blank=True)
	submitted = models.BooleanField(default=False, null=True, blank=True)
	dateCreated = models.DateTimeField(auto_now_add=True)
	lastUpdated = models.DateTimeField(auto_now=True)

	def _str_(self):
		going = "willAttend#" if attending else "willNotAttend#"
		return going + self.id

class Invitee(models.Model):
	firstName = models.CharField(max_length=28, blank=True, null=True)
	lastName = models.CharField(max_length=30, null=True, blank=True)
	email = models.CharField(max_length=60, null=True, blank=True)
	mobileNumber = models.CharField(max_length=14, null=True, blank=True)
	zipCode = models.CharField(max_length=10, null=True, blank=True)
	attending = models.BooleanField(default=False, null=True, blank=True)
	rsvpSubmitted = models.BooleanField(default=False, null=True, blank=True)
	rsvp = models.ForeignKey(Rsvp, default=None, null=True, blank=True, on_delete=models.CASCADE)

	def _str_(self):
		return self.firstName

class Message(models.Model):
	firstName = models.CharField(max_length=80)
	lastName = models.CharField(max_length=30, null=True, blank=True)
	email = models.CharField(max_length=60, null=True, blank=True)
	message = models.CharField(max_length=800, null=True, blank=True)
	dateCreated = models.DateTimeField(auto_now_add=True)

	def _str_(self):
		return self.message


