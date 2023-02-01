from django.test import TestCase

from dermobkend.models import Medico
from faker import Faker

faker = Faker()

# Create your tests here.

class MedicoModelTest(TestCase):
    def setUp(self):
        Medico.objects.create(nombres="Jor", apellidos="ge", tipo_identificacion="TI", numero_identificacion=1155,
                              fecha_nacimiento="2023-01-11", lugar_nacimiento="Bogota",
                              lugar_residencia="Bogota", numero_celular="31545", numero_registro_profesional="prof001",
                              correo=faker.email,
                              clave="1234")
        Medico.objects.create(nombres="Mari", apellidos="a", tipo_identificacion="TI", numero_identificacion=1166,
                              fecha_nacimiento="2023-01-11", lugar_nacimiento="Bogota",
                              lugar_residencia="Bogota", numero_celular="31545", numero_registro_profesional="prof001",
                              correo=faker.email,
                              clave="1234")
        Medico.objects.create(nombres="Lic", apellidos="ia", tipo_identificacion="TI", numero_identificacion=1177,
                              fecha_nacimiento="2023-01-11", lugar_nacimiento="Bogota",
                              lugar_residencia="Bogota", numero_celular="31545", numero_registro_profesional="prof001",
                              correo=faker.email,
                              clave="1234")

    def test_findMedicos(self):
        medicos = Medico.objects.all()
        self.assertEqual(len(medicos), 3)

    def test_findMedico(self):
        medico = Medico.objects.get(id=1)
        self.assertEqual(medico.nombres, "Jor")

    def test_updateMedico(self):
        medico = Medico.objects.get(id=1)
        medico.nombres = "Otro nombre"
        medico.save()
        medico = Medico.objects.get(id=1)
        self.assertNotEqual(medico.nombres, "Jor")

    def test_deleteMedico(self):
        medico = Medico.objects.get(id=2)
        medico.delete()
        medicos = Medico.objects.all()
        self.assertEqual(len(medicos), 2)

    def test_createMedico(self):
        Medico.objects.create(nombres="El", apellidos="nuevo", tipo_identificacion="TI", numero_identificacion=1155,
                              fecha_nacimiento="2023-01-11", lugar_nacimiento="Bogota",
                              lugar_residencia="Bogota", numero_celular="31545", numero_registro_profesional="prof001",
                              correo="correo@",
                              clave="1234")

        medicos = Medico.objects.all()

        self.assertEqual(len(medicos), 4)
