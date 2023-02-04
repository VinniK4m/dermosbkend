from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.caso_medico.selectors import paciente_get_by_id
from apps.caso_medico.serializers import CasoMedicoSerializer
from apps.dermobkend.models import CasoMedico


# Create your views here.
class CasosMedicosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasoMedicoSerializer
    queryset = CasoMedico.objects.all()

    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.queryset, many=True).data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=self.serializer_class.validated_data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
