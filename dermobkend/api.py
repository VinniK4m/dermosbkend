from .models import Medico, Paciente, Especialidades, MedicoEspecialidad
from rest_framework import viewsets, permissions
from .serializers import MedicoSerializer, PacienteSerializer, EspecialidadesSerializer, MedicoEspecialidadesSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer

class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EspecialidadesSerializer

class MedicoEspecialidadViewSet(viewsets.ModelViewSet):
    queryset = MedicoEspecialidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoEspecialidadesSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

