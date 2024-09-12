from rest_framework import serializers

from src.apps.shared.models import Cargo, DocumentState


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"


class DocumentStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentState
        fields = "__all__"
