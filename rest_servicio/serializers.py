from rest_framework import serializers
from users.models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['idServicio','nombreServicio','img','descripcionServicio','categoria']