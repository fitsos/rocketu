# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarChoice'
        db.create_table(u'cars_app_carchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('instock', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cars_app', ['CarChoice'])


    def backwards(self, orm):
        # Deleting model 'CarChoice'
        db.delete_table(u'cars_app_carchoice')


    models = {
        u'cars_app.carchoice': {
            'Meta': {'object_name': 'CarChoice'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cars_app']