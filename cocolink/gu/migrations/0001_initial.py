# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GuPost'
        db.create_table(u'gu_gupost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('body_text', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'gu', ['GuPost'])


    def backwards(self, orm):
        # Deleting model 'GuPost'
        db.delete_table(u'gu_gupost')


    models = {
        u'gu.gupost': {
            'Meta': {'object_name': 'GuPost'},
            'body_text': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.TextField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gu']