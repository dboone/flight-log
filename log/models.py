from django.db import models

# 
class Airport(models.Model):
	name = models.CharField('Name', max_length=200)
	code = models.CharField('Code', max_length=200)
	
	def __unicode__(self):
		return u'%s (%s)' % (self.name, self.code) 

class Trip(models.Model):
	depart = models.ForeignKey(Airport, related_name='trip_depart')
	arrive = models.ForeignKey(Airport, related_name='trip_arrive')
	distance = models.FloatField('Distance')
	duration = models.FloatField('Duration')
	
	def __unicode__(self):
		return u'From: %s\nTo: %s' % (self.depart, self.arrive)

class Plane(models.Model):
	call_number = models.CharField('Call Number', max_length=200)
	
	def __unicode__(self):
		return u'%s' % self.call_number

class Entry(models.Model):
	trip = models.ForeignKey(Trip)
	plane = models.ForeignKey(Plane)
	notes = models.TextField('Notes')
	
	def __unicode__(self):
		return u'%s' % self.notes
