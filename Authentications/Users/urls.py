from rest_framework import routers
from .api import UserssViewSet

#Controllers api
routes=routers.DefaultRouter()
routes.register('api/users',UserssViewSet,'UserControllers')
urlpatterns =routes.urls

