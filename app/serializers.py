from rest_framework import serializers
from .models import *

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = ["id", "end", "cidade", "cep",
                  "preco"]