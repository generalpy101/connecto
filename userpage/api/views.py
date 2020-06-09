from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter,OrderingFilter

from django.contrib.auth.models import User
from userpage.models import Post
from userpage.api.serializers import PostSerializer

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_detail_post_view(request,id) :
	try :
		post_obj = Post.objects.get(pk=id)

	except Post.DoesNotExist :
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == "GET" :
		serializer = PostSerializer(post_obj)
		return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_update_post_view(request,id) :
	try :
		post_obj = Post.objects.get(pk=id)

	except Post.DoesNotExist :
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if post_obj.user != user :
		return Response({'error' : "Wrong person"})

	if request.method == "PUT" :
		serializer = PostSerializer(post_obj,data = request.data)
		data = {}
		if serializer.is_valid() :
			serializer.save()
			data['success'] = "Update successful"
			return Response(data=data)
		return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def api_delete_post_view(request,id) :
	try :
		post_obj = Post.objects.get(pk=id)

	except Post.DoesNotExist :
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if post_obj.user != user :
		return Response({'error' : "Wrong person"})

	if request.method == "DELETE" :
		operation = post_obj.delete()
		data = {}
		if operation :
			data['success'] = "Success"
		else :
			data['failure'] = 'Failed'
		return Response(data=data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_create_post_view(request) :
	account = request.user

	post_obj = Post(user = account)

	if request.method == "POST" :
		serializer = PostSerializer(post_obj,data = request.data)
		data = {}
		if serializer.is_valid() :
			serializer.save()
			return Response(serializer.data,status = status.HTTP_201_CREATED)
		return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


class ApiPostListVIew(ListAPIView) :
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = PageNumberPagination
	filter_backends = (SearchFilter,OrderingFilter)
	search_fields = ('user__username','caption')