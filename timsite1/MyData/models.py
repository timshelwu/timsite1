import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
		
class DataList(models.Model):
	myParent = models.ForeignKey('self', blank = True, null = True)
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class StringParameter(models.Model):
	myParent = models.ForeignKey(DataList)
	name = models.CharField(max_length=200)
	value = models.CharField(max_length=1000, blank = True, null = True)
	def __str__(self):
		return self.name
	def __unicode__(self):
		return '%s: %s' % (self.name, self.value)
		
class IntegerParameter(models.Model):
	myParent = models.ForeignKey(DataList)
	name = models.CharField(max_length=200)
	value = models.IntegerField(blank = True, null = True)
	def __str__(self):
		return self.name
		
class BooleanParameter(models.Model):
	myParent = models.ForeignKey(DataList)
	name = models.CharField(max_length=200)
	value = models.BooleanField(default=False, blank = True)
	def __str__(self):
		return self.name
		
class DecimalParameter(models.Model):
	myParent = models.ForeignKey(DataList)
	name = models.CharField(max_length=200)
	value = models.DecimalField(max_digits=19, decimal_places=10, blank = True, null = True)
	def __str__(self):
		return self.name
		
class UnitParameter(models.Model):
	myParent = models.ForeignKey(DataList)
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name