from django.contrib import admin

# Register your models here.
from .models import Post,Like,Following,Notification

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Following)
admin.site.register(Notification)