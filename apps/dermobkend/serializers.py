from rest_framework import serializers
from .models import Medico, Paciente, Especialidad, MedicoEspecialidad, Diagnostico, Paises


class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id', 'nombre', 'descripcion')


class MedicoSerializer(serializers.ModelSerializer):
    casos_medicos_medico = serializers.StringRelatedField(many=True)

    class Meta:
        model = Medico
        fields = ('id','tipo_identificacion','numero_identificacion','nombres', 'apellidos', 'lugar_nacimiento', 'lugar_residencia', 'numero_celular',
                  'numero_registro_profesional','correo' , 'clave', 'fecha_nacimiento', "casos_medicos_medico")
        depth = 1

    def __init__(self, *args, **kwargs):
        super(MedicoSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class MedicoEspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoEspecialidad
        fields = ('medico', 'especialidad')


class PacienteSerializer(serializers.ModelSerializer):
    casos_medicos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Paciente
        fields = (
            'id', 'nombres', 'apellidos', 'lugar_nacimiento', 'fecha_nacimiento', 'lugar_residencia', 'edad',
            'sexo','numero_celular', 'correo', 'clave', "casos_medicos")

    def __init__(self, *args, **kwargs):
        super(PacienteSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class DiagnosticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnostico
        fields = ('id', 'caso', 'fecha_diagnostico', 'descripcion', 'fecha_acepta')
