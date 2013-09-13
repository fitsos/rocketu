# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'orm_app_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'orm_app', ['Poll'])

        # Adding model 'PollAnswer'
        db.create_table(u'orm_app_pollanswer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['orm_app.Poll'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vote_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'orm_app', ['PollAnswer'])

        # Adding model 'Comment'
        db.create_table(u'orm_app_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orm_app.Poll'])),
        ))
        db.send_create_signal(u'orm_app', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'orm_app_poll')

        # Deleting model 'PollAnswer'
        db.delete_table(u'orm_app_pollanswer')

        # Deleting model 'Comment'
        db.delete_table(u'orm_app_comment')


    models = {
        u'orm_app.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orm_app.Poll']"})
        },
        u'orm_app.poll': {
            'Meta': {'object_name': 'Poll'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orm_app.pollanswer': {
            'Meta': {'object_name': 'PollAnswer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': u"orm['orm_app.Poll']"}),
            'vote_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['orm_app']