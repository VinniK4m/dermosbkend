from rest_framework.routers import SimpleRouter

from apps.caso_medico.views import CasosMedicosPacienteViewSet, CasosMedicosMedicoViewSet, CasosMedicosViewSet, \
    ImagenDiagnosticaViewset

app_name = "casos-medicos"

router = SimpleRouter()

router.register(r'pacientes/(?P<paciente_id>\d+)/casos-medicos', CasosMedicosPacienteViewSet)
router.register(r'medicos/(?P<medico_id>\d+)/casos-medicos', CasosMedicosMedicoViewSet)
router.register(r'casos-medicos', CasosMedicosViewSet)
router.register(r'casos-medicos/(?P<caso_id>\d+)/imagenes', ImagenDiagnosticaViewset)


urlpatterns = router.urls
