from rest_framework import routers
from .api import MedicoViewSet, PacienteViewSet, EspecialidadesViewSet, MedicoEspecialidadViewSet, SoporteViewSet, \
    SoportesMedicoViewSet, DiagnosticoExternoViewSet, SeguimientosViewSet, SeguimientosMedicoViewSet,DiagnosticoXViewSet

router = routers.DefaultRouter()

router.register('medicos', MedicoViewSet, 'dermosbk')
router.register(r'medicos/(?P<medico_id>\d+)/soportes', SoportesMedicoViewSet)
router.register('especialiades', EspecialidadesViewSet, 'dermosbk')
router.register('medicosespecialidad', MedicoEspecialidadViewSet, 'dermosbk')
router.register('pacientes', PacienteViewSet, 'dermosbk')
router.register('soportes', SoporteViewSet, 'dermosbk')
router.register('diagnosticoexterno', DiagnosticoExternoViewSet, 'dermosbk')
router.register('seguimientos', SeguimientosViewSet, 'dermosbk')
router.register('diagnosticosx', DiagnosticoXViewSet, 'dermosbk')
router.register(r'seguimientomedico/(?P<medico_id>\d+)', SeguimientosMedicoViewSet)

urlpatterns = router.urls

