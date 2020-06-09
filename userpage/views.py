from django.shortcuts import render,redirect,HttpResponse,reverse
from django.http import HttpResponseForbidden,HttpResponseNotAllowed
from django.contrib import messages
from .models import Post,Like,Following
from account.models import Profile
from django.contrib.auth.models import User
import json
from .models import Notification
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

@login_required
def home(request):
	user = Following.objects.get(user= request.user)
	followed_users = user.followed.all()
	posts = Post.objects.filter(user__in = followed_users).order_by('-date') | Post.objects.filter(user=request.user).order_by('-date')
	liked_post = list()
	notifications = Notification.objects.filter(to = request.user,seen=False)

	for i in posts :
		try :
			is_liked = Like.objects.get(post = i,user = request.user)
			liked_post.append(i)
		except :
			pass
	data = {
		'posts' : posts,
		'liked_post' : liked_post,
		'notifications' : notifications
	}

	return render(request,'userpage/postfeed.html',data)

@login_required
def post(request) :
	if request.method == 'POST' :
		try :
			image = request.FILES['image']
			caption = request.POST.get('caption','')
			user = request.user
			post_obj = Post(user=user,image=image,caption=caption)
		except :
			caption = request.POST.get('caption','')
			user = request.user
			post_obj = Post(user=user,caption=caption)

		post_obj.save()
		messages.success(request,'Post uploaded')
		return redirect(reverse('home'))
	else :
		messages.error('An error occured')
		return redirect(request,reverse('home'))
@login_required

def delPost(request,id) :
	post_ = Post.objects.get(pk=id)
	if request.user == post_.user :
		try : 
			img_url = post.image.url
			post_.delete()
			messages.info(request,'Post has been deleted')
		except :
			post_.delete()
			messages.info(request,'Post has been deleted')
		return HttpResponse('post deleted')
	else :
		return HttpResponseForbidden()
@login_required

def userProfile(request,uname) :
	try : 
		user = User.objects.get(username= uname)
		profile = Profile.objects.get(user = user)
		post = getPost(user)
		is_following = Following.objects.filter(user=request.user,followed = user)
		following_obj = Following.objects.get(user = user)
		follower,following = following_obj.follower.count(),following_obj.followed.count()
		notifications = Notification.objects.filter(to = request.user,seen=False)
		data = {
			'getUser' : user,
			'profile' : profile,
			'post' : post,
			'is_following' : is_following,
			'following' : following,
			'follower' : follower,
			'notifications' :notifications
		}
		return render(request,'userpage/userProfile.html',data)
	except Exception as e :
		print(e)
		messages.error(request,'Username doesnt exists')
		return redirect('/user')

def getPost(cuser) :
	post_obj = Post.objects.filter(user=cuser).order_by('-date')
	imgList = [post_obj[i:i+3] for i in range(0,len(post_obj),3)]
	return imgList
@login_required

def likePost(request) :
	post_id = request.GET.get('likeid','')
	post = Post.objects.get(pk = post_id)
	user = request.user
	like = Like.objects.filter(post = post,user=user)
	liked = False

	if like :
		Like.dislike(post,user)

	else : 
		liked = True
		Like.like(post,user)

	resp = {
		'liked' : liked
	}
	response = json.dumps(resp)

	return HttpResponse(response,content_type='application/json')
@login_required

def comment(request) :
	comment = request.GET.get('commentText','')
	print(comment)
	return render(request,"userpage/comments.html")
@login_required

def follow(request,username) :
	main_user = request.user
	following = User.objects.get(username=username)

	try :
		check = Following.objects.get(user=main_user,followed=following)
		check_bool = True 
	except :
		check_bool = False

	if check_bool :
		Following.unfollow(main_user,following)
		check_bool = False
	else :
		Following.follow(main_user,following)
		check_bool = True

	resp = {'following' : check_bool}

	response = json.dumps(resp)
	return HttpResponse(response,content_type='application/json')

class SearchUser(ListView):
    model = User
    template_name = "userpage/searchUser.html"

    def get_queryset(self) :
    	username = self.request.GET.get('username','')
    	users = User.objects.filter(username__icontains = username)
    	return users
@login_required

def dattedPosts(request,date) :
	user = Following.objects.get(user= request.user)
	followed_users = user.followed.all()
	posts = Post.objects.filter(
		user__in = followed_users,date__startswith=date).order_by('-date') |Post.objects.filter(
		user=request.user,date__startswith=date).order_by('-date')
	liked_post = list()
	notifications = Notification.objects.filter(to = request.user,seen=False)


	for i in posts :
		try :
			is_liked = Like.objects.get(post = i,user = request.user)
			liked_post.append(i)
		except :
			pass
	data = {
		'posts' : posts,
		'liked_post' : liked_post,
		'date' : date,
		'notifications' : notifications,
	}

	return render(request,'userpage/timmedPosts.html',data)
@login_required

def notification(request) :
	notifications_all = Notification.objects.filter(to = request.user).order_by('-date')
	notifications = Notification.objects.filter(to = request.user,seen=False)

	data = {
		'notifications_all' : notifications_all,
		'notifications' : notifications
	}

	return render(request,'userpage/notifications.html',data)
@login_required

def setAsRead(request,id) :
	notification_obj = Notification.objects.get(pk=id) 
	if request.user == notification_obj.to :
		notification_obj.seen = True 
		notification_obj.save()
		return HttpResponse('Seen')
	else : 
		return HttpResponseForbidden()
@login_required

def setAsRead_all(request) :
	notification_obj = Notification.objects.filter(to = request.user)
	for notification in notification_obj :
		notification.seen = True 
		notification.save()
	return HttpResponse('Seen')
@login_required

def deleteNotification(request,id) :
	notification_obj = Notification.objects.get(pk=id) 
	if request.user == notification_obj.to :
		notification_obj.delete()
		return HttpResponse('deleted')
	else :
		return HttpResponseForbidden()
@login_required

def postDetails(request,id) :
	post = Post.objects.get(pk=id)
	return render(request,'userpage/postDetail.html',{'post':post})