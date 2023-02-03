from rest_framework.decorators import action
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response

from .models import Medico, Paciente, Especialidad, MedicoEspecialidad
from rest_framework import viewsets, permissions, generics, status
from .serializers import MedicoSerializer, PacienteSerializer, EspecialidadesSerializer, MedicoEspecialidadesSerializer

#class MedicoList(generics.ListCreateAPIView):
#    queryset = Medico.objects.all()
#    serializer_class = MedicoSerializer
#    permission_classes = [permissions.AllowAny]

#    def list(self, request):
#        # Tenga en cuenta el uso de `get_queryset ()` en lugar de `self.queryset`
#        queryset = self.get_queryset()
#        serializer = MedicoSerializer(queryset, many=True)
#        return Response(serializer.data)
class MedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer

    def get_queryset(self):
        numeroIdentificacion = self.request.query_params.get('identificacion')
        lugarResidencia = self.request.query_params.get('residencia')
        print(numeroIdentificacion)
        print(lugarResidencia)

        if (numeroIdentificacion != None):
            medicos = Medico.objects.filter(numero_identificacion =numeroIdentificacion, lugar_residencia = lugarResidencia)
        else:
            medicos = Medico.objects.all()
        return medicos

    def get_view_name(self):
        return Response({})

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            if id != None:
                medicos = Medico.objects.all()
        except:
            medicos = self.get_queryset()
        serializer = MedicoSerializer(medicos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EspecialidadesSerializer

class MedicoEspecialidadViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoEspecialidadesSerializer

    def get_queryset(self):
        medico = self.request.query_params.get('medico')
        especialidad = self.request.query_params.get('especialidad')

        if (medico != None ):
            especialidadMedico = MedicoEspecialidad.objects.filter(medico =medico)
        elif (especialidad != None ):
            especialidadMedico = MedicoEspecialidad.objects.filter(especialidad=especialidad)
        else:
            especialidadMedico = MedicoEspecialidad.objects.all()
        return especialidadMedico

    def get_view_name(self):
        return Response({})

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params['id']
            if id != None:
                especialidadMedico = Medico.objects.all()
        except:
            especialidadMedico = self.get_queryset()
        serializer = MedicoEspecialidadesSerializer(especialidadMedico, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

