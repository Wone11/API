from rest_framework import routers
from .api import ControllersViewSet

#Controllers api
routes=routers.DefaultRouter()
routes.register('api/controllers',ControllersViewSet,'UserControllers')
urlpatterns =routes.urls

