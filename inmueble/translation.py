from modeltranslation.translator import translator, TranslationOptions
from inmueble.models import TipoInmueble

class TipoInmuebleTranslationOptions(TranslationOptions):
  fields = ('descripcion',)

translator.register(TipoInmueble, TipoInmuebleTranslationOptions)
