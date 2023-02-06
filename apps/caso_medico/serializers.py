from __future__ import annotations

from rest_framework import serializers

from apps.dermobkend.models import CasoMedico, Diagnostico


class CasoMedicoSerializer(serializers.ModelSerializer):
    diagnosticos = serializers.StringRelatedField(many=True)

    class Meta:
        model = CasoMedico
        fields = ('id', 'descripcion', 'estado', 'fecha_creacion', 'paciente', 'diagnosticos','medico')


class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ('id', 'caso', 'fecha_diagnostico', 'descripcion', 'medico', 'aceptado', 'fecha_acepta')