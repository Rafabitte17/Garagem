from rest_framework.serializers import ModelSerializer

from core.models import Modelo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        files = '__all__'
