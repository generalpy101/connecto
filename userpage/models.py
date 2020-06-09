from django.db import models
from django.contrib.auth.models import User
from account.models import Profile

# Create your models here.
class Post(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	caption = models.CharField(max_length=200,null=True)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='Post')

	def __str__(self) :
		return f"{self.user} : {self.date}"


class Like(models.Model) :
	user = models.ManyToManyField(User,related_name='likedBy')
	post = models.OneToOneField(Post, on_delete=models.CASCADE,related_name='postLike')

	@classmethod
	def like(cls,post,liking_user) :
		obj,create = cls.objects.get_or_create(post = post)
		obj.user.add(liking_user)

	@classmethod
	def dislike(cls,post,disliking_user) :
		obj,create = cls.objects.get_or_create(post = post)
		obj.user.remove(disliking_user)

	def __str__(self) :
		return f"{self.post}"

class Following(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	followed = models.ManyToManyField(User,related_name = 'followed')
	follower = models.ManyToManyField(User,related_name='follower')

	@classmethod
	def follow(cls,user,other) :
		obj,create = cls.objects.get_or_create(user = user)
		obj.followed.add(other)
	@classmethod
	def unfollow(cls,user,other) :
		obj,create = cls.objects.get_or_create(user = user)
		obj.followed.remove(other)

	def __str__(self) :
		return f"{self.user}"


class Notification(models.Model) :
	notification_type = (('Liked','liked'),('Followed','followed'))
	to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
	seen = models.BooleanField(default=False)
	ref_user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='referenced_user')
	ref_post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True,related_name='referenced_post')
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	type = models.CharField(max_length=255,choices=notification_type,default='liked')

	def __str__(self) :
		return f"{self.to} : {self.content}"

from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed,sender = Like.user.through)
def send_notification(sender,instance,action,reverse,pk_set,**kwargs) :
	user = User()
	for i in pk_set :
		user = User.objects.get(pk=i)
	if action == 'post_add' :
		notification = Notification.objects.create(to = instance.post.user,content = f'liked your post',
			ref_user=user,ref_post=instance.post,type='liked')
		notification.save()
	if action == 'post_remove' :
		try :
			notification = Notification.objects.get(to = instance.post.user,type='liked',
				ref_user=user,ref_post = instance.post)
			notification.delete()
		except :
			pass