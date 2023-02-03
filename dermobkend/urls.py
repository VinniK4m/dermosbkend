from rest_framework import routers, generics

from .api import PacienteViewSet, EspecialidadesViewSet, MedicoEspecialidadViewSet, MedicoViewSet

router = routers.DefaultRouter()

#router.register('api/elmedicos', ListCreateAPIView.as_view(queryset=Medico.objects.all(), serializer_class=MedicoSerializer), 'medico-list')
router.register('api/medicos', MedicoViewSet, 'dermosbk')
router.register('api/especialiades', EspecialidadesViewSet, 'dermosbk')
router.register('api/medicosespecialidad', MedicoEspecialidadViewSet, 'dermosbk')
router.register('api/pacientes', PacienteViewSet, 'dermosbk')

urlpatterns = router.urls


