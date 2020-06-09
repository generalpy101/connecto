from django.urls import path
from . import views
from .views import SearchUser

urlpatterns = [
    path('',views.home,name='home'),
    path('post/',views.post,name='post'),
    path('delete/<int:id>/',views.delPost,name='deletePost'),
    path('profile/<str:uname>/',views.userProfile,name='userProfile'),
    path('like/',views.likePost,name='likepost'),
    path('slug/comment/',views.comment,name='comment'),
    path('pro/follow/<str:username>',views.follow,name='follow'),
    path('search/',SearchUser.as_view(),name='search_user'),
    path('date/<str:date>',views.dattedPosts,name='posts_date'),
    path('notifications/',views.notification,name='notification'),
    path('notification/seen/<int:id>',views.setAsRead,name='notification_read'),
    path('notification/seen/all',views.setAsRead_all,name='notification_readAll'),
    path('notification/delete/<int:id>',views.deleteNotification,name='notification_delete'),
    path('post/<int:id>',views.postDetails,name='postDetails'),
]
