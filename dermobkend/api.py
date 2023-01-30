from .models import Medico, Paciente
from rest_framework import viewsets, permissions
from .serializers import MedicoSerializer, PacienteSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PacienteSerializer

