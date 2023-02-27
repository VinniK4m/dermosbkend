from rest_framework.response import Response

from .models import Medico, Paciente, Especialidad, MedicoEspecialidad, Paises, Soporte, Lesion
from rest_framework import viewsets, permissions, generics, status
from .serializers import MedicoSerializer, PacienteSerializer, EspecialidadesSerializer, MedicoEspecialidadesSerializer, \
    SoporteSerializer, LesionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class MedicoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    serializer_class = MedicoSerializer

    def get_queryset(self):
        numeroIdentificacion = self.request.query_params.get('identificacion')
        lugarResidencia = self.request.query_params.get('residencia')
        print(numeroIdentificacion)
        print(lugarResidencia)

        if (numeroIdentificacion != None):
            medicos = Medico.objects.filter(numero_identificacion=numeroIdentificacion,
                                            lugar_residencia=lugarResidencia)
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

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(request_data['correo'], request_data['correo'], request_data['clave'])
            user.first_name = request_data['nombres']
            user.last_name = request_data['apellidos']
            user.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


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

        if (medico != None):
            especialidadMedico = MedicoEspecialidad.objects.filter(medico=medico)
        elif (especialidad != None):
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

        return Response(serializer.data, status=status.HTTP_200_OK)


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(request_data['correo'], request_data['correo'], request_data['clave'])
            user.first_name = request_data['nombres']
            user.last_name = request_data['apellidos']
            user.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SoporteViewSet(viewsets.ModelViewSet):
    queryset = Soporte.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SoporteSerializer


class SoportesMedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = SoporteSerializer
    queryset = Soporte.objects.all()

    def list(self, request, *args, **kwargs):
        query_set = Soporte.objects.filter(medico=self.kwargs.get('medico_id'))
        return Response(self.serializer_class(query_set, many=True).data)


class LesionViewSet(viewsets.ModelViewSet):
    queryset = Lesion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LesionSerializer
