from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User 
from .models import Profile,Following,Post,Notification

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs) :
	if created :
		Profile.objects.create(user=instance)
		Following.objects.create(user=instance)

@receiver(m2m_changed,sender = Following.followed.through) #which list is changed
def add_follower(sender,instance,action,reverse,pk_set,**kwargs) :
	'''
		sender => Signal sending model
		instance => username of user who is logged in i.e. request.user
		action => pre_add -> if user follwed someone else pre_remove if user unfollowed someone
		pk_set => Set of all users primary keys which are followed by user
	'''
	followed_user = list() #list of followed users
	loggedUser = User.objects.get(username=instance)
	for i in pk_set :
		user = User.objects.get(pk=i)
		following_obj = Following.objects.get(user=user)
		followed_user.append(following_obj)
	
	if action == 'pre_add' :	
		for i in followed_user :
			i.follower.add(loggedUser)
			i.save()
			notification = Notification.objects.create(to = i.user,content = f'started following you',
			ref_user=loggedUser,type='followed')
			notification.save()
	if action == 'pre_remove' :	
		for i in followed_user :
			i.follower.remove(loggedUser)
			i.save()
			try :
				notification = Notification.objects.get(to = i.user,ref_user=loggedUser,type='followed')
				notification.delete()
			except :
				pass

