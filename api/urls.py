from django.urls import include
from rest_framework.routers import DefaultRouter

from api.views import PersonViewSet

router = DefaultRouter(trailing_slash=False)
router.register('', PersonViewSet, basename='person')

urlpatterns = []
urlpatterns += router.urls