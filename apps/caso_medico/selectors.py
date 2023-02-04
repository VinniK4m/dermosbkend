from apps.dermobkend.models import Paciente


def paciente_get_by_id(paciente_id: int) -> Paciente:
    return Paciente.objects.get(pk=paciente_id)
