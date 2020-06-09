from rest_framework import serializers

from userpage.models import Post

class PostSerializer(serializers.ModelSerializer) :

	username = serializers.SerializerMethodField('get_username')

	class Meta :
		model = Post
		fields = ['image','caption','date','username']

	def get_username(self,post_obj) :
		username = post_obj.user.username
		return username