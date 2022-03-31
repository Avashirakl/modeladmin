from django.urls import include, path

from rest_framework import routers

from posts.views import PostViewSet

router = routers.DefaultRouter()
router.register('', PostViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls)),
]