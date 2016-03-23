from django.db import models

class State(models.Model):  
	abbreviation = models.CharField(max_length=2, null=True, blank=True)
	name = models.CharField(max_length=100)

	def __unicode__(self):  
	    return self.name

class StateCapital(models.Model):
	
	name = models.CharField(max_length=100)
	
	state = models.OneToOneField('main.State', null=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	capital_population = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=100)
	state = models.ForeignKey('main.State')

	zip_code = models.CharField(max_length=100, null=True, blank=True)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)
	county = models.CharField(max_length=100, null= True, blank = True)
	
	def __unicode__(self):
		return self.name
