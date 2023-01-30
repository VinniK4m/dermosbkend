from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker

faker = Faker()


# Create your tests here.

class MedicoModelTest(APITestCase):
    urlMedicos = 'http://127.0.0.1:8000/api/medicos/'
    def setUp(self) -> None:
        from dermobkend.models import Medico
        self.medico = Medico.objects.create(nombres="Jor", apellidos="ge", tipoIdentificacion="TI", numeroIdentificacion=1155,
                              fechaNacimiento="2023-01-11", lugarNacimiento="Bogota",
                              lugarResidencia="Bogota", numeroCelular="31545", numeroRegistroProfesional="prof001",
                              correo=faker.email(),
                              clave="1234")
        medicos = Medico.objects.all()


    def test_getMedicos(self):

        response = self.client.get(self.urlMedicos)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getMedicosBy(self):

        response = self.client.get(self.urlMedicos+"1")
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_postMedicos(self):

        response = self.client.post(self.urlMedicos,
                {
                    "tipoIdentificacion": "TI",
                    "numeroIdentificacion": 1011093842,
                    "nombres": "El",
                    "apellidos": "Lito",
                    "fechaNacimiento": "2023-01-11",
                    "lugarNacimiento": "Bogota",
                    "lugarResidencia": "Bogota",
                    "numeroCelular": "3152545454",
                    "numeroRegistroProfesional": "asdasda",
                    "correo": "elcorreo@yahoo.com",
                    "clave": "123456"
                }
                )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_putMedicos(self):

        response = self.client.post(self.urlMedicos+"1",
                {
                    "nombres": "Ellos",
                    "apellidos": "Lito",
                    "lugarResidencia": "Cali",
                    "numeroCelular": "3152545454",
                    "numeroRegistroProfesional": "asdasda",
                    "correo": "elcorreo@yahoo.com",
                }
                )
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_deleteMedicos(self):

        response = self.client.delete(self.urlMedicos+"1")
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)