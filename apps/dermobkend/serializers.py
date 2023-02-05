from rest_framework import serializers
from .models import Medico, Paciente, Especialidad, MedicoEspecialidad, Diagnostico, Paises


class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id', 'nombre', 'descripcion')


class MedicoSerializer(serializers.ModelSerializer):
    casos_medicos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Medico
        fields = ('id','tipo_identificacion','numero_identificacion','nombres', 'apellidos', 'lugar_nacimiento', 'lugar_residencia', 'numero_celular',
                  'numero_registro_profesional','correo' , 'clave', 'fecha_nacimiento', "casos_medicos")
        depth = 1


class MedicoEspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoEspecialidad
        fields = ('medico', 'especialidad')


class PacienteSerializer(serializers.ModelSerializer):
    casos_medicos = serializers.StringRelatedField(many=True)

    class Meta:
        model = Paciente
        fields = (
            'id', 'nombres', 'apellidos', 'lugar_nacimiento', 'lugar_residencia', 'edad',
            'sexo','numero_celular', 'correo', 'clave', "casos_medicos")
        depth = 1


class DiagnosticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnostico
        fields = ('id', 'caso', 'fecha_diagnostico', 'descripcion', 'fecha_acepta')
