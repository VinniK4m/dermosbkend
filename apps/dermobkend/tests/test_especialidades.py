from django.test import TestCase
from rest_framework.test import APIClient
from apps.dermobkend.models import Especialidad
from faker import Faker

faker = Faker()


# Create your tests here.

class EspecialidadModelTest(TestCase):
    def setUp(self):
        Especialidad.objects.create(nombre="dermatologia pediatrica", descripcion="dermatologia")
        Especialidad.objects.create(nombre="dermatologia adultos", descripcion="dermatologia")
        Especialidad.objects.create(nombre="cancer de piel", descripcion="dermatologia")
        Especialidad.objects.create(nombre="otra", descripcion="dermatologia")
        client: APIClient = APIClient()

    def test_get_especialida(self):
        self.client.get('/especialidad/')

    def test_findEspecialidads(self):
        especialidades = Especialidad.objects.all()
        self.assertEqual(len(especialidades), 4)

    def test_findEspecialidad(self):
        especialidad = Especialidad.objects.get(id=1)
        self.assertNotEquals(especialidad.nombre, "otra")

    def test_updateEspecialidad(self):
        especialidad = Especialidad.objects.get(id=1)
        especialidad.nombre = "Otro nombre"
        especialidad.save()
        especialidad = Especialidad.objects.get(id=1)
        self.assertNotEquals(especialidad.nombre, "Jor")

    def test_deleteEspecialidad(self):
        especialidad = Especialidad.objects.get(id=2)
        especialidad.delete()
        especialidades = Especialidad.objects.all()
        self.assertEqual(len(especialidades), 3)

    def test_createEspecialidad(self):
        Especialidad.objects.create(nombre="derma", descripcion="derma")

        especialidades = Especialidad.objects.all()

        self.assertEqual(len(especialidades), 5)
