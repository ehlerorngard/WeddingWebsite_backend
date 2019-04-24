from django.db import models

class Rsvp(models.Model):
	attending = models.BooleanField(default=False)
	lodging = models.CharField(max_length=56, null=True, blank=True)
	numInviteesAlotted = models.IntegerField(null=True, blank=True)
	numAdults = models.IntegerField(null=True, blank=True)
	numChildren = models.IntegerField(null=True, blank=True)
	othersNames = models.CharField(max_length=120, blank=True)
	arrivalDay = models.CharField(max_length=10, blank=True)
	departureDay = models.CharField(max_length=10, null=True, blank=True)
	volunteeringToHelp = models.BooleanField(default=False, blank=True)
	numVeg = models.IntegerField(null=True, blank=True)
	numNoDairy = models.IntegerField(null=True, blank=True)
	numNoGluten = models.IntegerField(null=True, blank=True)
	additionalNotes = models.CharField(max_length=600, null=True, blank=True)
	needTent = models.BooleanField(default=False)
	needPad = models.BooleanField(default=False)
	needSleepingBag = models.BooleanField(default=False)
	submitted = models.BooleanField(default=False)
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
	rsvpSubmitted = models.BooleanField(default=False, blank=True)
	rsvp = models.ForeignKey(Rsvp, default=None, null=True, blank=True, on_delete=models.CASCADE)

	def _str_(self):
		return self.firstName

# class Task(models.Model):
# 	summary = models.CharField(max_length=80)
# 	description = models.CharField(max_length=400)
# 	category = models.CharField(max_length=60)
# 	day = models.CharField(max_length=10)
# 	duration = models.IntegerField()
# 	startTime = models.TimeField()
# 	endTime = models.TimeField()
# 	idealTotalNumWorkers = models.IntegerField()
# 	numWorkersNeeded = models.IntegerField()
# 	volunteers = models.ManyToManyField(Invitee)

# 	def _str_(self):
# 		return self.summary


