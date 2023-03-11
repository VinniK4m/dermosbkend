from __future__ import annotations

from rest_framework import serializers

from apps.dermobkend.models import CasoMedico, Diagnostico, ImagenDiagnostica


class CasoMedicoSerializer(serializers.ModelSerializer):
    diagnosticos = serializers.StringRelatedField(many=True)
    imagenes = serializers.StringRelatedField(many=True)

    class Meta:
        model = CasoMedico
        fields = '__all__'
        depth = 1

    def __init__(self, *args, **kwargs):
        super(CasoMedicoSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ('id', 'caso', 'fecha_diagnostico', 'descripcion', 'medico', 'aceptado', 'fecha_acepta')
        depth = 1

    def __init__(self, *args, **kwargs):
        super(DiagnosticoSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class ImagenDiagnosticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenDiagnostica
        fields = '__all__'
