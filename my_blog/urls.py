"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import notifications.urls
from body.views import index 

urlpatterns = [
    path('',include('body.urls', namespace='body')),
    path('',index),
    path('admin/', admin.site.urls),
    path('user/', include('userprofile.urls', namespace='user')),
    path('password-reset/', include('password_reset.urls')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice/',include('notice.urls',namespace='notice')),
    path('link/',include('link.urls', namespace='links')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
