from django.db import models

from datetime import datetime

# Create your models here.
class Pin(models.Model):
	Tag_Choice = (('Curb Cut', 'Curb Cut'), ('Sidewalk','Sidewalk'), ('Accessible Path','Accessible Path'), ('Transit','Transit'), ('Food', 'Food'), ('Music', 'Music'), ('Networking', 'Networking'),('Party', 'Party'), ('Sport', 'Sport'), ('Wine','Wine'), ('Others', 'Others'))
	Status_Choice = (('Barrier','Barrier'),('In Progress','In Progress'),('Resolved', 'Resolved'),('Best Practice','Best Practice'))
	#General information about Pin
	tag = models.CharField(max_length=50, choices=Tag_Choice, blank=False, default='Accessible Path')
	status = models.CharField(max_length=20, choices=Status_Choice, blank=False, default='Barrier')
	description = models.CharField(max_length=500, null=True, blank=True)
	date_created = models.DateField(blank=False)
	date_updated = models.DateField(blank=True)
	location_latitude = models.FloatField(blank=False)
	location_longitude = models.FloatField(blank=False)

class Image(models.Model):
	pin = models.ForeignKey(Pin)
	image = models.ImageField(upload_to='static/images/', blank=False)

class Comment(models.Model):
	pin = models.ForeignKey(Pin)
	comment = models.CharField(max_length=500, blank=False)
	date = models.DateField(blank=False)

