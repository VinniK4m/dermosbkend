from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

from dermobkend.models import Especialidades

faker = Faker()


# Create your tests here.

class EspecialidadesModelTest(APITestCase):
    urlEspecialidadess = 'http://127.0.0.1:8000/api/especialidades/'
    def setUp(self) -> None:
        from dermobkend.models import Especialidades
        self.especialidad = Especialidades.objects.create(nombre="dermatologia", descripcion="dermatologia")
        especialidades = Especialidades.objects.all()


    def test_getEspecialidadess(self):

        response = self.client.get(self.urlEspecialidadess)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getEspecialidadessBy(self):

        response = self.client.get(self.urlEspecialidadess+"1")
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_postEspecialidadess(self):

        response = self.client.post(self.urlEspecialidadess,
                {
                    "nombre" : "dermatologia", "descripcion" : "dermatologia"
                }
                )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_putEspecialidadess(self):

        response = self.client.post(self.urlEspecialidadess+"1",
                {
                    "nombre" : "dermatologia", "descripcion" : "dermatologia"
                }
                )
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_deleteEspecialidadess(self):

        response = self.client.delete(self.urlEspecialidadess+"1")
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)