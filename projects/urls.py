from rest_framework import routers
from .api import ProjectsViewSet
from django.urls import path
from .views import ApiKeyManager

router = routers.DefaultRouter()

router.register('api/projects', ProjectsViewSet, 'projects')

urlpatterns = router.urls

urlpatterns.append(path('api_key/', ApiKeyManager.as_view()))
