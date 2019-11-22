"""datasortproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.utils.functional import curry
from django.views.defaults import *
# from rest_framework import routers
# from API.views import *

admin.autodiscover()

handler500 = "web.views.server_error"
handler404 = "web.views.page_not_found_error"





class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# Routers provide an easy way of automatically determining the URL conf.


urlpatterns = [
    # url(r'^', include('auth0login.urls')),
    url(r'admin/', admin.site.urls),
    url(r'^auth0', include(router.urls)),
    url(r'^', include('apps.datasortapp.urls')),	
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
    
]

