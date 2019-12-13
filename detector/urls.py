from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from .views import BlackViewSet

router = routers.SimpleRouter()
router.register(r'blacks', BlackViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]