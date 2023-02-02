from rest_framework import serializers
from .models import Medico, Paciente

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id','tipo_identificacion','numero_identificacion','nombres', 'apellidos', 'lugar_nacimiento', 'lugar_residencia', 'numero_celular',
                  'numero_registro_profesional','correo' , 'clave')
        read_only_fields = ('correo',)

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
        'id', 'nombres', 'apellidos', 'lugarNacimiento', 'lugarResidencia', 'numeroCelular',
        'correo', 'clave')
