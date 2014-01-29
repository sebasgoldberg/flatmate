from django.shortcuts import render
from inmueble.models import Inmueble

# Create your views here.
def inmueble(request):
  inmuebles = Inmueble.objects.filter(publicado=True)
  cantidad = len(inmuebles)
  if cantidad>0:
    latitud = 0
    longitud = 0
    for i in inmuebles:
      latitud += i.latitud 
      longitud += i.longitud
    latitud = latitud / cantidad
    longitud = longitud / cantidad
  else:
    latitud = None
    longitud = None
  return render(request,
    'inmueble/inmueble.html', 
    { 'inmuebles': inmuebles,
      'latitud': latitud,
      'longitud': longitud })

