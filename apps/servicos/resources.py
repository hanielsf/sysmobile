from import_export import resources
from .models import OrdemServico


class PersonResource(resources.ModelResource):
    class Meta:
        model = OrdemServico

