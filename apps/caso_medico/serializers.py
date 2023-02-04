from __future__ import annotations

from rest_framework import serializers

from apps.dermobkend.models import CasoMedico


class CasoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasoMedico
        fields = ('descripcion',)
