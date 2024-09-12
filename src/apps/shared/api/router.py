from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from src.apps.shared.api.viewsets import CargoViewSet, DocumentStateViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register("cargo", CargoViewSet)
router.register("document-state", DocumentStateViewSet)

urlpatterns = router.urls
