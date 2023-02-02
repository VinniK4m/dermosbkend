from rest_framework import routers
from .api import MedicoViewSet, PacienteViewSet

router = routers.DefaultRouter()

router.register('medicos/', MedicoViewSet, 'dermosbk')
router.register('pacientes/', PacienteViewSet, 'dermosbk')

urlpatterns = router.urls

