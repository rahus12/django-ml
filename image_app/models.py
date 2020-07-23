from django.db import models


# Create your models here.
class Alphabet(models.Model):
	name = models.CharField(max_length = 50)
	Alphabet_img = models.ImageField(upload_to = 'images/')
	#number = models.CharField(max_length=5, blank=True)
	

	
	