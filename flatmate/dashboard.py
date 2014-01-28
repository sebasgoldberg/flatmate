# coding=utf-8
"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'iamcast.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name
from django.conf import settings

from inmueble.models import Inmueble

from datetime import datetime, date, timedelta


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def add_ultimos_inmuebles(self,cantidad_inmuebles):

      ultimos_inmuebles=tuple([
        [i,i.admin_url()] for i in Inmueble.objects.order_by('-id')[:cantidad_inmuebles]
        ])

      self.children.append(modules.LinkList(
        _('Ultimos Inmuebles'),
        column=2,
        children=ultimos_inmuebles
      ))
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        
        self.children.append(modules.Group(
            _('Aplicaciones Principales'),
            column=1,
            collapsible=True,
            children = [
                modules.ModelList(
                    column=1,
                    collapsible=False,
                    models=('inmueble.models.Inmueble',),
                ),
            ]
        ))

        self.children.append(modules.ModelList(
            _('Diccionario de datos'),
            collapsible=True,
            column=1,
            models=('inmueble.*',),
            exclude = ('inmueble.models.Inmueble', ),
        ))
        
        self.children.append(modules.ModelList(
            _('Administracion de usuarios y permisos'),
            column=1,
            collapsible=False,
            models=('django.contrib.*',),
        ))

        self.add_ultimos_inmuebles(5)

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=True,
            column=2,
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Links'),
            column=3,
            children=[
                {
                    'title': settings.AMBIENTE.dominio,
                    'url': '/',
                    'external': False,
                },
                {
                    'title': _(u'facebook'),
                    'url': 'https://www.facebook.com/profile.php?id=1497121106',
                    'external': True,
                },
            ]
        ))

