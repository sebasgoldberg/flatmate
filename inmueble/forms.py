from inmueble.models import DireccionInmueble
from iampacks.cross.direccion.forms import BaseDireccionForm

class DireccionInmuebleForm(BaseDireccionForm):
  class Meta:
    model = DireccionInmueble
