# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Permission, Group

class Command(BaseCommand):

  help=u'Crea los grupos con sus respectivos permisos'

  def handle(self,*args,**options):
    permissions = Permission.objects.filter(content_type__app_label__in=['inmueble'])
    publicadores=Group(
      name='publicadores'
      )
    publicadores.save()
    publicadores.permissions=[p.id for p in permissions]
    publicadores.save()
    self.stdout.write('Grupo %s creado con exito\n' % (publicadores.name))


