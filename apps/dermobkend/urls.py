from rest_framework import routers
from .api import MedicoViewSet, PacienteViewSet, EspecialidadesViewSet, MedicoEspecialidadViewSet

router = routers.DefaultRouter()

router.register('api/medicos', MedicoViewSet, 'dermosbk')
router.register('api/especialiades', EspecialidadesViewSet, 'dermosbk')
router.register('api/medicosespecialidad', MedicoEspecialidadViewSet, 'dermosbk')
router.register('api/pacientes', PacienteViewSet, 'dermosbk')

urlpatterns = router.urls

