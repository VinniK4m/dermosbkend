from rest_framework import serializers
from .models import Medico, Paciente, Especialidad, MedicoEspecialidad, Paises


class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id','nombre','descripcion')

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id','tipo_identificacion','numero_identificacion','nombres', 'apellidos', 'fecha_nacimiento', 'lugar_nacimiento', 'lugar_residencia','sexo', 'numero_celular',
                  'numero_registro_profesional','correo' , 'clave')

class MedicoEspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicoEspecialidad
        fields = ('medico','especialidad' )

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = (
        'id', 'nombres', 'apellidos', 'fechaNacimiento', 'lugarNacimiento', 'lugarResidencia', 'numeroCelular',
        'correo', 'clave')


