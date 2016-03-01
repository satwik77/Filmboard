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
	profile_pic= models.ImageField(blank=True, upload_to='pictures', null=True)

	
	# photo = models.ImageField(blank=True, upload_to='pictures')

	class Meta:
		verbose_name_plural = 'experiences'
	def __unicode__(self):
		return str(self.project_name)    



class Recommendations(models.Model):
	accepted = models.BooleanField(default=False)
	reco_from = models.CharField(max_length=200, null=True)
	reco_from_email = models.EmailField(blank=True, null=True)
	project_type = models.CharField(max_length=100, null=True)
	project_name = models.CharField(max_length=200, null=True)
	project_status = models.CharField(max_length=100, null=True)
	skills = models.CharField(max_length=300, null=True)
	character_name = models.CharField(max_length=200, default = "Not Applicable")
	role_played = models.CharField(max_length = 200, default = "Not Applicable")
	duration_start = models.DateField(null=True)
	duration_end = models.DateField(null=True)
	remarks = models.TextField(null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
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
	)
	name = models.CharField(max_length=200,blank=True, null=True)
	gender = models.CharField(max_length=1, choices=GENDERS,blank=True, null=True)
	dob = models.DateField(null=True)	
	height = models.FloatField(blank=True, null=True) #save the height in m and always show in both feet and meters
	weight = models.FloatField(blank=True, null=True) #Weight is in Kg
	email_id = models.EmailField(blank=True, null=True)
	body_type = models.CharField(max_length=200,blank=True, null=True)
	location = models.CharField(max_length=150,blank=True, null=True)
	education_background = models.TextField()
	certifications = models.TextField()
	past_experiences = models.ManyToManyField(PastExperiences, blank=True, null=True)
	profile_pic= models.ImageField(blank=True, upload_to='pictures', null=True)
	phone = models.BigIntegerField(blank=True, null=True)
	ob_type= models.CharField(max_length=200, blank=True,null=True)
	ethnicity= models.CharField(max_length=200, blank=True,null=True)
	address = models.TextField(default=' ')
	email_verified= models.BooleanField(default=False)
	my_story = models.TextField(default=' ')

	class Meta:
		verbose_name_plural = 'Artists'
	def __unicode__(self):
		return str(self.name)

class Allied(models.Model):
	user = models.OneToOneField(User)
	# GENDERS = (
	# 	('M', 'Male'),
	# 	('F', 'Female'),
 #        # ('O', 'Other'),
	# )
	name = models.CharField(max_length=200, blank=True, null=True)
	# category = models.CharField(max_length=20, choices=GENDERS)
	# dob = models.DateField()	
	location = models.CharField(max_length=150, blank=True, null=True)
	services = models.CharField(max_length=300, blank=True, null=True)
	certifications = models.TextField()
	past_experiences = models.ManyToManyField(PastExperiences, blank=True)
	phone = models.BigIntegerField(null=True)
	ob_type= models.CharField(max_length=200, blank=True,null=True)
	inventory_list= models.CharField(max_length=500, blank=True, null=True, default='')
	profile_pic= models.ImageField(blank=True, upload_to='pictures', null=True)
	email_verified= models.BooleanField(default=False)
	my_story = models.TextField(default=' ')
	
	class Meta:
		verbose_name_plural = 'Allied Services'
	def __unicode__(self):
		return str(self.name)

class locations(models.Model):
	name = models.CharField(max_length=100)
	allied = models.ForeignKey(Allied, null=True,blank=True,default=None)
	# photo = models.ImageField(blank=True, upload_to='pictures')
	class Meta:
		verbose_name_plural = 'Locations'
	def __unicode__(self):
		return str(self.name)


class Production(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=200, blank=True, null=True)
	location = models.CharField(max_length=150, blank=True, null=True)
	past_experiences = models.ManyToManyField(PastExperiences, blank=True)
	phone = models.BigIntegerField(null=True)
	profile_pic= models.ImageField(blank=True, upload_to='pictures', null=True)
	address = models.TextField(default=' ')
	email_verified= models.BooleanField(default=False)

	aboutus = models.TextField(default=' ', null=True, blank=True)
	class Meta:
		verbose_name_plural = 'Productions'
	def __unicode__(self):
		return str(self.name)


#model for all the projects
class Projects(models.Model):
	project_type = models.CharField(max_length=100)
	project_name = models.CharField(max_length=200)
	date_posted = models.DateField(auto_now_add=True)
	producer = models.ManyToManyField(Production, blank=True)
	project_status = models.CharField(max_length=100)
	project_cost = models.CharField(max_length=100) #Ask Parikshit what to keep INteger or Char?
	location = models.CharField(max_length=150)
	languages = models.CharField(max_length=400)
	duration_start = models.DateField()
	duration_end = models.DateField()
	description = models.TextField()
	profile_pic= models.ImageField(blank=True, upload_to='pictures', null=True)

	class Meta:
		verbose_name_plural = 'Projects'
	def __unicode__(self):
		return str(self.project_name)	

class ProjectRequirements(models.Model):
	REQTYPES = (
		('Artist','Artist'),
		('Allied Service','Allied Service'),
		('Producers','Producers'),
		)
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)
	req_type = models.CharField(max_length=20,choices=REQTYPES) 
	skills = models.CharField(max_length=100)
	numbers = models.IntegerField()
	character = models.CharField(max_length=200)
	role = models.CharField(max_length=100)
	description = models.TextField()
	user = models.ManyToManyField(User, blank=True)

	class Meta:
		verbose_name_plural = 'Requirements'
	def __unicode__(self):
		return str(self.project.project_name)

class Notifications(models.Model):
	message= models.CharField(max_length=300, blank=True)
	user = models.ForeignKey(User, blank=True,null=True, default=None)
	url = models.CharField(max_length=500, blank=True)
	sent= models.BooleanField(default=False)
	class Meta:
		verbose_name_plural = 'Notifications'
	def __unicode__(self):
		return str(self.user.username)

