from rest_framework import viewsets

from .serializers import CargoSerializer, DocumentStateSerializer
from src.apps.shared.models import Cargo, DocumentState


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class DocumentStateViewSet(viewsets.ModelViewSet):
    queryset = DocumentState.objects.all()
    serializer_class = DocumentStateSerializer
