from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Medico
import json


# Create your views here.
class MedicoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            medicos=list(Medico.objects.filter(id=id).values())
            if (len(medicos)>0):
                medico= medicos[0]
                datos = {'message': "Success", 'medico': medico}
            else:
                datos = {'message': "medico no existe"}
            return JsonResponse(datos)
        else:
            medicos = list(Medico.objects.values())
            if len(medicos) > 0:
                datos = {'message': "Success", 'medicos': medicos}
            else:
                datos = {'message': 'medicos no encontrados'}
            return JsonResponse(datos)

    def post(self, request):
        dataJson = json.loads(request.body)
        Medico.objects.create(nombres=dataJson['nombres'],apellidos=dataJson['apellidos'], fechaNacimiento=dataJson['fecha_nacimiento'],
                              lugarResidencia=dataJson['lugar_residencia'],lugarNacimiento=dataJson['lugar_nacimiento'],
                              numeroCelular=dataJson['numero_celular'],numeroRegistroProfesional=dataJson['numero_registro_profesional'],
                              correo=dataJson['correo'],clave=dataJson['clave'])

        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        dataJson = json.loads(request.body)
        medicos = list(Medico.objects.filter(id=id).values())
        if (len(medicos) > 0):
            medico = Medico.objects.get(id=id)
            medico.nombres = dataJson['nombres']
            medico.apellidos = dataJson['apellidos']
            medico.fechaNacimiento = dataJson['fechaNacimiento']
            medico.lugarResidencia = dataJson['lugarResidencia']
            medico.lugarNacimiento = dataJson['lugarNacimiento']
            medico.numeroCelular = dataJson['numeroCelular']
            medico.numeroRegistroProfesional = dataJson['numeroRegistroProfesional']
            medico.correo = dataJson['correo']
            medico.clave = dataJson['clave']
            medico.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "medico no existe"}
        return JsonResponse(datos)

    def delete(self, request, id):
        medicos = list(Medico.objects.filter(id=id).values())
        if (len(medicos) > 0):
            Medico.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "medico no existe"}
        return JsonResponse(datos)
