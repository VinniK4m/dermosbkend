from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

from apps.dermobkend.models import Especialidad

faker = Faker()


# Create your tests here.

class EspecialidadModelTest(APITestCase):
    urlEspecialidads = 'http://127.0.0.1:8000/api/v1/especialidades/'
    def setUp(self) -> None:
        self.especialidad = Especialidad.objects.create(nombre="dermatologia", descripcion="dermatologia")
        especialidades = Especialidad.objects.all()


    def test_getEspecialidads(self):

        response = self.client.get(self.urlEspecialidads)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_getEspecialidadsBy(self):

        response = self.client.get(self.urlEspecialidads+"1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_postEspecialidads(self):

        response = self.client.post(self.urlEspecialidads,
                {
                    "nombre" : "dermatologia", "descripcion" : "dermatologia"
                }
                )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_putEspecialidads(self):

        response = self.client.post(self.urlEspecialidads+"1",
                {
                    "nombre" : "dermatologia", "descripcion" : "dermatologia"
                }
                )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_deleteEspecialidads(self):

        response = self.client.delete(self.urlEspecialidads+"1")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)