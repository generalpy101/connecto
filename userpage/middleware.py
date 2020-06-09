from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect,reverse
from django.contrib import messages

class LoginRequiredMiddleware(object):
	"""docstring for LoginRequiredMiddleware
	   if user is authenticated : move fwd
	   else : sign up first
	"""
	def __init__(self,get_response) :
		self.get_response = get_response

	def __call__(self,request) :
		response = self.get_response(request)
		return response

	def process_view(self,request,view_func,view_args,view_kwargs) :
		url = request.path
		auth = request.user.is_authenticated
		
		if auth and url == settings.HOME_URL :
			
			return redirect('/home')
		if not auth and (url != settings.HOME_URL and url not in settings.EXEMPT_URLS and url not in reverse('api')) :
			return redirect(settings.HOME_URL)


