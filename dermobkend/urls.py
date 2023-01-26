from rest_framework import routers
from .api import MedicoViewSet

router = routers.DefaultRouter()

router.register('api/medicos', MedicoViewSet, 'dermosbk')

urlpatterns = router.urls

