from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User 
from .models import Profile
from userpage.models import Following

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs) :
	print('signal')
	if created :
		Profile.objects.create(user=instance)
		Following.objects.create(user=instance)