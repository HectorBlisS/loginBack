
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_social_oauth2 import urls as authUrls
from rest_framework import routers 
from main.views import UserViewset

router = routers.DefaultRouter()
router.register('users', UserViewset)

urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(authUrls))
]
