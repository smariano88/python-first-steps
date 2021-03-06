"""meeting_planner URL Configuration

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

#  pylint: disable=C0103
#    ^ eventually we should be able to override or update the
#      CONST_NAME_RGX value

from django.contrib import admin
from django.urls import path, include
from website.views import about, welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='home'),
    path('about', about),
    path('meetings/', include('meetings.urls')),
]

admin.site.site_header = "Meeting room"
admin.site.site_title = "Meeting room portal"
admin.site.index_title = "Welcome to Meeting room Portal"
