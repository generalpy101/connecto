from django.urls import path
from account.api.views import (
		registration_view,
		account_properties_view,
		update_account_view
	)
from  rest_framework.authtoken.views import obtain_auth_token

urlpatterns  = [
	path('register',registration_view,name='register'),
	path('login',obtain_auth_token,name='login_api'),
	path('properties',account_properties_view,name='properties'),
	path('update',update_account_view,name='update'),
]