from rest_framework import serializers
from .models import Medico, Paciente, Especialidad, MedicoEspecialidad, \
    Diagnostico, DiagnosticoExterno, Soporte, Lesion, Seguimiento
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id', 'nombre', 'descripcion')


class MedicoSerializer(serializers.ModelSerializer):
    casos_medicos_medico = serializers.StringRelatedField(many=True)
    soportes_medico = serializers.StringRelatedField(many=True)

    class Meta:
        model = Medico
        fields = ('id', 'tipo_identificacion', 'numero_identificacion', 'nombres', 'apellidos', 'lugar_nacimiento',
                  'lugar_residencia', 'numero_celular',
                  'numero_registro_profesional', 'correo', 'clave', 'fecha_nacimiento', "casos_medicos_medico",
                  "soportes_medico")
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
            'sexo', 'numero_celular', 'correo', 'clave', "casos_medicos", "perfil_dermatologico")
        depth = 1

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


class DiagnosticoExternoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiagnosticoExterno
        fields = ('id', 'caso', 'fecha_diagnostico', 'diagnostico', 'nombre_medico','correo', 'recomendaciones',
                  'ciudadcita','fechacitapresencial','urlCitaremota')


class SoporteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Soporte
        fields = ('id', 'medico', 'tipo_soporte', 'institucion_educativa',
                  'nombre_programa', 'descripcion', 'graduado', 'fecha_grado', 'fecha_soporte', 'validado', 'url')

class LesionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesion
        fields = ('id', 'tipo', 'forma','numero', 'distribucion')

class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seguimiento
        fields = ('diagnostico', 'medico', 'mensaje_paciente','fecha_msg_paciente', 'mensaje_medico', 'fecha_msg_medico', 'detalle')
