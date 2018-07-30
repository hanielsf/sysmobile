# Django
from django import template

register = template.Library()


# CSS_PERSONALIZADO====================================================================================
@register.filter(name='addcss')
def addcss(field, css):
    class_old = field.field.widget.attrs.get('class', None)
    class_new = class_old + ' ' + css if class_old else css

    return field.as_widget(attrs={"class": class_new})


# ===================================================================================================


# FORMAT_PERSONALIZADO===============================================================================
@register.filter(name='addmask')
def addmask(field, mask):
    mask_old = field.field.widget.attrs.get('data-format', None)
    mask_new = mask_old + ' ' + mask if mask_old else mask

    return field.as_widget(attrs={"data-format": mask_new})

# ===================================================================================================


