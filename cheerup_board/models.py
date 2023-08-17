from django.db import models

# Create your models here.
class PhotoPost(models.Model):
	author = models.CharField(max_length=128, null=False)
	anony_password = models.CharField(max_length=50, blank=False, null=False)

	photo = models.ImageField(upload_to='cheerup/images/%Y/%m/%d', blank=False, null=False)
	hook_text = models.CharField(max_length=100, blank=True)
	content = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'[{self.pk}] :: {self.author}'


class Comment(models.Model):
	author = models.CharField(max_length=128, null=False)
	anony_password = models.CharField(max_length=50, blank=False, null=False)
	
	content = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)

	post = models.ForeignKey(PhotoPost, on_delete=models.CASCADE)

	def __str__(self):
		return f'[{self.pk}] :: {self.author}'

class Message(models.Model):
	author = models.CharField(max_length=128, null=False)
	anony_password = models.CharField(max_length=50, blank=False, null=False)

	content = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)