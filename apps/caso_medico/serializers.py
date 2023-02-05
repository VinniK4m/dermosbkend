from __future__ import annotations

from rest_framework import serializers

from apps.dermobkend.models import CasoMedico


class CasoMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasoMedico
        fields = ('id', 'descripcion', 'estado', 'fecha_creacion', 'paciente', 'medico')
        depth = 1