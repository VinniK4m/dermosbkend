from django.test import TestCase

from dermobkend.models import Paciente


class TestPaciente(TestCase):
    def test_apellido_property(self):
        from dermobkend.tests.factory import PacienteFactory
        paciente = PacienteFactory.create(nombres="Test", apellidos="test")
        assert Paciente.objects.get(nombres="Test").apellidos == 'test'
