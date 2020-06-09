from django.urls import path

from userpage.api.views import (
	api_detail_post_view,
	api_update_post_view,
	api_delete_post_view,
	api_create_post_view,
	ApiPostListVIew
	)

urlpatterns = [
	path('<int:id>/',api_detail_post_view,name='detail'),
	path('<int:id>/update',api_update_post_view,name='update'),
	path('<int:id>/delete',api_delete_post_view,name='delete'),
	path('create',api_create_post_view,name='create'),
	path('list',ApiPostListVIew.as_view(),name='list'),
]