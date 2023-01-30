from rest_framework import serializers
from .models import Medico, Paciente

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id','nombres', 'apellidos', 'fechaNacimiento', 'lugarNacimiento', 'lugarResidencia', 'numeroCelular',
                  'numeroRegistroProfesional','correo' , 'clave')
        read_only_fields = ('correo',)

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
        'id', 'nombres', 'apellidos', 'fechaNacimiento', 'lugarNacimiento', 'lugarResidencia', 'numeroCelular',
        'correo', 'clave')
