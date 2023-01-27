from rest_framework import routers
from .api import MedicoViewSet, PacienteViewSet

router = routers.DefaultRouter()

router.register('api/medicos', MedicoViewSet, 'dermosbk')
router.register('api/pacientes', PacienteViewSet, 'dermosbk')

urlpatterns = router.urls

