from import_export import resources
from .models import Cliente


class PersonResource(resources.ModelResource):
    class Meta:
        model = Cliente

