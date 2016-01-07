from django.db import models
from django.contrib.auth.models import User

class PastExperiences(models.Model):
	project_type = models.CharField(max_length=100)
	project_name = models.CharField(max_length=200)
	project_status = models.CharField(max_length=100)
	skills = models.CharField(max_length=300)
	character_name = models.CharField(max_length=200, default = "Not Applicable")
	role_played = models.CharField(max_length = 200, default = "Not Applicable")
	duration_start = models.DateField()
	duration_end = models.DateField()
	remarks = models.TextField()
	special_mention = models.TextField()
	# photo = models.ImageField(blank=True, upload_to='pictures')

	class Meta:
		verbose_name_plural = 'experiences'
	def __unicode__(self):
		return str(self.project_name)    



class Recommendations(models.Model):
	project_type = models.CharField(max_length=100)
	project_name = models.CharField(max_length=200)
	project_status = models.CharField(max_length=100)
	skills = models.CharField(max_length=300)
	character_name = models.CharField(max_length=200, default = "Not Applicable")
	role_played = models.CharField(max_length = 200, default = "Not Applicable")
	duration_start = models.DateField()
	duration_end = models.DateField()
	seek_from_type = models.CharField(max_length=200)
	seek_from_name = models.CharField(max_length=200)
	email_id= models.EmailField()
	add_msg = models.TextField()


	class Meta:
		verbose_name_plural = 'Recommendations'
	def __unicode__(self):
		return str(self.project_name)  	

#Initially we will register only name, email id and password. For the rest of the stuff it will be in update profile option for artists
class Artist(models.Model):
	user = models.OneToOneField(User)
	GENDERS = (
		('M', 'Male'),
		('F', 'Female'),
        # ('O', 'Other'),
	)
	name = models.CharField(max_length=200)
	gender = models.CharField(max_length=1, choices=GENDERS)
	dob = models.DateField()	
	height = models.IntegerField() #save the height in cm and always show in both feet and centimeters
	weight = models.IntegerField() #Weight is in Kg
	email_id = models.EmailField()
	body_type = models.CharField(max_length=200)
	location = models.CharField(max_length=150)
	skills = models.CharField(max_length=100)
	education_background = models.TextField()
	certifications = models.TextField()
	past_experiences = models.ManyToManyField(PastExperiences, blank=True)
	recommendations = models.ManyToManyField(Recommendations, blank=True)
	phone = models.IntegerField(null=True)

	
	class Meta:
		verbose_name_plural = 'Artists'
	def __unicode__(self):
		return str(self.name)

	
