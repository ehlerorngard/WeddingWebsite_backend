from django.db import models

class Rsvp(models.Model):
	attending = models.BooleanField(default=False)
	lodging = models.CharField(max_length=56, blank=True)
	numInviteesAlotted = models.IntegerField()
	numAdults = models.IntegerField()
	numChildren = models.IntegerField()
	othersNames = models.CharField(max_length=120)
	arrivalDay = models.CharField(max_length=10)
	departureDay = models.CharField(max_length=10, blank=True)
	volunteeringToHelp = models.BooleanField(default=False)
	numVeg = models.IntegerField()
	numNoDairy = models.IntegerField()
	numNoGluten = models.IntegerField()
	additionalNotes = models.CharField(max_length=600, blank=True)
	needTent = models.BooleanField(default=False)
	needPad = models.BooleanField(default=False)
	needSleepingBag = models.BooleanField(default=False)
	submitted = models.BooleanField(default=False)
	lastUpdated = models.DateTimeField()

	def _str_(self):
		going = "willAttend#" if attending else "willNotAttend#"
		return going + self.id

class Invitee(models.Model):
	firstName = models.CharField(max_length=28)
	lastName = models.CharField(max_length=30)
	email = models.CharField(max_length=60, null=True)
	mobileNumber = models.CharField(max_length=14, null=True)
	rsvpSubmitted = models.BooleanField(default=False)
	rsvp = models.ForeignKey(Rsvp, default=None, on_delete=models.CASCADE)

	def _str_(self):
		return self.firstName

class Task(models.Model):
	summary = models.CharField(max_length=80)
	description = models.CharField(max_length=400)
	category = models.CharField(max_length=60)
	day = models.CharField(max_length=10)
	duration = models.IntegerField()
	startTime = models.TimeField()
	endTime = models.TimeField()
	idealTotalNumWorkers = models.IntegerField()
	numWorkersNeeded = models.IntegerField()
	volunteers = models.ManyToManyField(Invitee)

	def _str_(self):
		return self.summary

