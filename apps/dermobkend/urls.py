from rest_framework import routers
from .api import MedicoViewSet, PacienteViewSet, EspecialidadesViewSet, MedicoEspecialidadViewSet, SoporteViewSet

router = routers.DefaultRouter()

router.register('medicos', MedicoViewSet, 'dermosbk')
router.register('especialiades', EspecialidadesViewSet, 'dermosbk')
router.register('medicosespecialidad', MedicoEspecialidadViewSet, 'dermosbk')
router.register('pacientes', PacienteViewSet, 'dermosbk')
router.register('soportes', SoporteViewSet, 'dermosbk')

urlpatterns = router.urls

