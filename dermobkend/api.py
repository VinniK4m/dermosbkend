from .models import Medico
from rest_framework import viewsets, permissions
from .serializers import MedicoSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer
