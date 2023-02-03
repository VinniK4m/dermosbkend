from rest_framework import routers
from .api import MedicoViewSet, PacienteViewSet, EspecialidadesViewSet, MedicoEspecialidadViewSet

router = routers.DefaultRouter()

router.register('medicos', MedicoViewSet, 'dermosbk')
router.register('especialiades', EspecialidadesViewSet, 'dermosbk')
router.register('medicosespecialidad', MedicoEspecialidadViewSet, 'dermosbk')
router.register('pacientes', PacienteViewSet, 'dermosbk')

urlpatterns = router.urls

