from rest_framework.routers import SimpleRouter

from apps.caso_medico.views import CasosMedicosViewSet

app_name = "caso-medico"

router = SimpleRouter()

router.register("caso-medico", CasosMedicosViewSet)

urlpatterns = router.urls
