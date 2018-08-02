from import_export import resources
from .models import Pessoa


class PersonResource(resources.ModelResource):
    class Meta:
        model = Pessoa

