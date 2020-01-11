from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone 
from django.db.models.signals import post_save
 
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=200, default='')
	phone = models.IntegerField(default=0)
	website =models.URLField(default='')
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.user.username

	def create_profile(sender, **kwargs):
		if kwargs['created']:
			user_profile = UserProfile.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile, sender=User)

class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(default=timezone.now)
	image = models.ImageField(blank=True, null=True, upload_to='uploads/image', verbose_name='Post Image', default='default.png')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', default=None)


	def __str__(self):
		return self.title
	
	def snippet(self):
		return self.content[:100] +'...'

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)	


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', null=True)
	author = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment=True
		self.save()

	def __str__(self):
		return self.content	
	