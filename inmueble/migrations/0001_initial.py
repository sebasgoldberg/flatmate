# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoInmueble'
        db.create_table(u'inmueble_tipoinmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'inmueble', ['TipoInmueble'])

        # Adding model 'Comodidad'
        db.create_table(u'inmueble_comodidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'inmueble', ['Comodidad'])

        # Adding model 'Servicio'
        db.create_table(u'inmueble_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'inmueble', ['Servicio'])

        # Adding model 'Barrio'
        db.create_table(u'inmueble_barrio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'inmueble', ['Barrio'])

        # Adding model 'Inmueble'
        db.create_table(u'inmueble_inmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.Barrio'], null=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('direccion_gmap', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tipo_inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.TipoInmueble'], null=True, blank=True)),
            ('superficie', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('precio_dia', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('precio_semana', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('precio_mes', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=2, blank=True)),
            ('publicado', self.gf('django.db.models.fields.BooleanField')()),
            ('destacado', self.gf('django.db.models.fields.BooleanField')()),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 29, 0, 0))),
            ('latitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=13, decimal_places=7, blank=True)),
            ('longitud', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=13, decimal_places=7, blank=True)),
        ))
        db.send_create_signal(u'inmueble', ['Inmueble'])

        # Adding M2M table for field comodidades on 'Inmueble'
        m2m_table_name = db.shorten_name(u'inmueble_inmueble_comodidades')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inmueble', models.ForeignKey(orm[u'inmueble.inmueble'], null=False)),
            ('comodidad', models.ForeignKey(orm[u'inmueble.comodidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inmueble_id', 'comodidad_id'])

        # Adding M2M table for field servicios on 'Inmueble'
        m2m_table_name = db.shorten_name(u'inmueble_inmueble_servicios')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('inmueble', models.ForeignKey(orm[u'inmueble.inmueble'], null=False)),
            ('servicio', models.ForeignKey(orm[u'inmueble.servicio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['inmueble_id', 'servicio_id'])

        # Adding model 'FotoInmueble'
        db.create_table(u'inmueble_fotoinmueble', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inmueble', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inmueble.Inmueble'])),
            ('foto', self.gf('inmueble.models.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'inmueble', ['FotoInmueble'])


    def backwards(self, orm):
        # Deleting model 'TipoInmueble'
        db.delete_table(u'inmueble_tipoinmueble')

        # Deleting model 'Comodidad'
        db.delete_table(u'inmueble_comodidad')

        # Deleting model 'Servicio'
        db.delete_table(u'inmueble_servicio')

        # Deleting model 'Barrio'
        db.delete_table(u'inmueble_barrio')

        # Deleting model 'Inmueble'
        db.delete_table(u'inmueble_inmueble')

        # Removing M2M table for field comodidades on 'Inmueble'
        db.delete_table(db.shorten_name(u'inmueble_inmueble_comodidades'))

        # Removing M2M table for field servicios on 'Inmueble'
        db.delete_table(db.shorten_name(u'inmueble_inmueble_servicios'))

        # Deleting model 'FotoInmueble'
        db.delete_table(u'inmueble_fotoinmueble')


    models = {
        u'inmueble.barrio': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Barrio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.comodidad': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Comodidad'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.fotoinmueble': {
            'Meta': {'object_name': 'FotoInmueble'},
            'foto': ('inmueble.models.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Inmueble']"})
        },
        u'inmueble.inmueble': {
            'Meta': {'object_name': 'Inmueble'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.Barrio']", 'null': 'True'}),
            'comodidades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Comodidad']", 'symmetrical': 'False', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'direccion_gmap': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 29, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '7', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '13', 'decimal_places': '7', 'blank': 'True'}),
            'precio_dia': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'precio_mes': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'precio_semana': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'publicado': ('django.db.models.fields.BooleanField', [], {}),
            'servicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inmueble.Servicio']", 'symmetrical': 'False', 'blank': 'True'}),
            'superficie': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'tipo_inmueble': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inmueble.TipoInmueble']", 'null': 'True', 'blank': 'True'})
        },
        u'inmueble.servicio': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'Servicio'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inmueble.tipoinmueble': {
            'Meta': {'ordering': "['descripcion']", 'object_name': 'TipoInmueble'},
            'descripcion': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inmueble']