from django.db import models

# Create your models here.

class database(models.Model):
	
	db_host = models.TextField()
	db_user = models.TextField()
	db_pass = models.TextField()
	db_name = models.TextField()

