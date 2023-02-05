from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.caso_medico.serializers import CasoMedicoSerializer
from apps.dermobkend.models import CasoMedico, Paciente, Medico

# Create your views here.
from apps.dermobkend.serializers import DiagnosticoSerializer


class CasosMedicosPacienteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasoMedicoSerializer
    queryset = CasoMedico.objects.all()

    def get_queryset(self):
        return CasoMedico.objects.filter(paciente=self.kwargs.get('paciente_id'))

    def list(self, request, *args, **kwargs):
        query_set = CasoMedico.objects.filter(paciente=self.kwargs.get('paciente_id'))
        return Response(self.serializer_class(query_set, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        paciente = Paciente.objects.filter(id=self.kwargs.get('paciente_id')).get()
        if paciente:
            request_data['paciente'] = str(paciente.id)
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CasosMedicosMedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasoMedicoSerializer
    queryset = CasoMedico.objects.all()

    def get_queryset(self):
        return CasoMedico.objects.filter(medico=self.kwargs.get('medico_id'))

    def list(self, request, *args, **kwargs):
        query_set = CasoMedico.objects.filter(medico=self.kwargs.get('medico_id'))
        return Response(self.serializer_class(query_set, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'], name='Reclaim case')
    def reclaim(self, request, pk=None):
        """Update the user's password."""
        request_data = request.data.copy()
        medico = Medico.objects.filter(id=self.kwargs.get('medico_id')).get()
        caso = CasoMedico.objects.filter(id=self.kwargs.get('caso_id')).get()
        casos_medicos = CasoMedico.objects.filter(medico_id__isnull=True)
        serializer = self.serializer_class(data=request_data)
        return 'asd'

    @action(detail=True, methods=['post'])
    def diagnosticar(self, request):
        caso = self.get_queryset(self)
        diagnostico_serializer = DiagnosticoSerializer(data=request.data)
        if diagnostico_serializer.is_valid():
            caso.save()
            return Response({'status': 'diagnosticando'})
        else:
            return Response(diagnostico_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)