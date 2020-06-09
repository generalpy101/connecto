from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls'),name='account_app'),
    path('home/',include('userpage.urls'),name='userpage'),
    #REST_FRAMEWORK URLS
    path('api/post/',include('userpage.api.urls'),name = 'post_api'),
    path('api/account/',include('account.api.urls'),name='account_api')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
