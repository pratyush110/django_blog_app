from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	country = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	hobbies = models.TextField()

	def __str__(self):
		return f'{self.user.username} Profile'
