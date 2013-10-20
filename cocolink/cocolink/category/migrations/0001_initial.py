# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoryLarge'
        db.create_table(u'category_categorylarge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('code', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'category', ['CategoryLarge'])

        # Adding model 'CategoryMiddle'
        db.create_table(u'category_categorymiddle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('l_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['category.CategoryLarge'])),
            ('code', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'category', ['CategoryMiddle'])


    def backwards(self, orm):
        # Deleting model 'CategoryLarge'
        db.delete_table(u'category_categorylarge')

        # Deleting model 'CategoryMiddle'
        db.delete_table(u'category_categorymiddle')


    models = {
        u'category.categorylarge': {
            'Meta': {'object_name': 'CategoryLarge'},
            'code': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'category.categorymiddle': {
            'Meta': {'object_name': 'CategoryMiddle'},
            'code': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'l_category_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['category.CategoryLarge']"}),
            'name': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['category']