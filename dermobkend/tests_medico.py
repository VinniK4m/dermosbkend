from django.test import TestCase

from dermobkend.models import Medico
from faker import Faker

faker = Faker()

# Create your tests here.

class MedicoModelTest(TestCase):
    def setUp(self):
        Medico.objects.create(nombres="Jor", apellidos="ge", tipoIdentificacion="TI", numeroIdentificacion=1155,
                              fechaNacimiento="2023-01-11", lugarNacimiento="Bogota",
                              lugarResidencia="Bogota", numeroCelular="31545", numeroRegistroProfesional="prof001",
                              correo=faker.email,
                              clave="1234")
        Medico.objects.create(nombres="Mari", apellidos="a", tipoIdentificacion="TI", numeroIdentificacion=1166,
                              fechaNacimiento="2023-01-11", lugarNacimiento="Bogota",
                              lugarResidencia="Bogota", numeroCelular="31545", numeroRegistroProfesional="prof001",
                              correo=faker.email,
                              clave="1234")
        Medico.objects.create(nombres="Lic", apellidos="ia", tipoIdentificacion="TI", numeroIdentificacion=1177,
                              fechaNacimiento="2023-01-11", lugarNacimiento="Bogota",
                              lugarResidencia="Bogota", numeroCelular="31545", numeroRegistroProfesional="prof001",
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
        Medico.objects.create(nombres="El", apellidos="nuevo", tipoIdentificacion="TI", numeroIdentificacion=1155,
                              fechaNacimiento="2023-01-11", lugarNacimiento="Bogota",
                              lugarResidencia="Bogota", numeroCelular="31545", numeroRegistroProfesional="prof001",
                              correo="correo@",
                              clave="1234")

        medicos = Medico.objects.all()

        self.assertEqual(len(medicos), 4)
