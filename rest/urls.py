"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from rest import settings, views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from .views import VideoListCreateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('beach/', views.beach_list),
    path('drinks/<int:id>', views.beach_detail),
    path('videos/', VideoListCreateView.as_view(), name='video-list-create')
    
    
    
]



urlpatterns = format_suffix_patterns(urlpatterns)


