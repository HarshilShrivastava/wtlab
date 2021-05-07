from rest_framework import serializers
from .models import Contactus
class queryserializer(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        fields='__all__'