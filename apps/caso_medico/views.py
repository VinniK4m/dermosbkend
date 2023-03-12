from os import link

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
import requests
import json
from rest_framework.decorators import action

from apps.caso_medico.serializers import CasoMedicoSerializer, DiagnosticoSerializer, ImagenDiagnosticaSerializer
from apps.dermobkend.serializers import DiagnosticoExternoSerializer
from apps.dermobkend.models import CasoMedico, Paciente, Medico, ImagenDiagnostica

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
            serializer.cre()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

class CasosMedicosMedicoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasoMedicoSerializer
    queryset = CasoMedico.objects.all()

    def list(self, request, *args, **kwargs):
        query_set = CasoMedico.objects.filter(medico=self.kwargs.get('medico_id'))
        return Response(self.serializer_class(query_set, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'], name='Diagnosticar caso')
    def diagnosticar(self, request, *args, **kwargs):
        serializer = DiagnosticoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CasosMedicosViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CasoMedicoSerializer
    queryset = CasoMedico.objects.filter(medico__isnull=True)

    def list(self, request, *args, **kwargs):
        query_set = CasoMedico.objects.filter(medico__isnull=True)
        return Response(self.serializer_class(query_set, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='automatico')
    def diagnosticar(self, request, *args, **kwargs):
        print('Entro dijo la m....a')
        request_data = request.data.copy()
        url = 'https://57640608-851c-4e1a-9cfd-29573fc37938.mock.pstmn.io/diagnosticar'
        json_diagnostico = {
            "paciente": {
                "id":123,
                "id_caso":1,
                "nombre":"Elsa",
                "apellido":"Patero",
                "identificacion":"123",
                "correo":"c@c.cpm",
                "consulta":{
                    "descripcion":"alskjda s",
                    "imagenes":[
                        {"url1":"url1"},
                        {"url2":"url2"}
                    ]
                }
            }
        }

        response =  requests.post(url, json_diagnostico)
        jsonRta = response.json()
        diagnosticoGral = jsonRta['diagnostico']
        serializerDiagnosticoEx = DiagnosticoExternoSerializer(data=diagnosticoGral)
        if serializerDiagnosticoEx.is_valid(raise_exception=True):
            serializerDiagnosticoEx.save()
            return Response(data=diagnosticoGral, status=status.HTTP_201_CREATED)

        return Response(data=diagnosticoGral, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        """Reclaim medical case"""
        instance = self.get_object()
        data = request.data
        medico = Medico.objects.filter(id=data.get('medico')).first()
        instance.medico = medico
        instance.estado = 'RECLAMADO'
        instance.save()
        serializer = CasoMedicoSerializer(instance)
        if serializer:
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImagenDiagnosticaViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ImagenDiagnosticaSerializer
    queryset = ImagenDiagnostica.objects.all()


    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.queryset, many=True).data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(self.serializer_class(instance).data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        request_data = request.data.copy()
        caso = CasoMedico.objects.filter(id=self.kwargs.get('caso_id')).get()
        if caso:
            request_data['caso'] = str(caso.id)
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.create(validated_data=serializer.validated_data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

