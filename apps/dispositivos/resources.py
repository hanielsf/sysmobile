from import_export import resources
from .models import Dispositivo


class PersonResource(resources.ModelResource):
    class Meta:
        model = Dispositivo

