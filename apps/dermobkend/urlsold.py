from django.urls import path
from .views import MedicoView

urlpatterns= [
    path('medicos/', MedicoView.as_view(), name='medicos_list'),
    path('medicos/<int:id>', MedicoView.as_view(), name='medicos_process')
]