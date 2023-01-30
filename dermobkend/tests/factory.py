import factory
from dermobkend.models import Paciente


class PacienteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Paciente

    nombres = factory.Faker('pystr')
    apellidos = factory.Faker('pystr')
