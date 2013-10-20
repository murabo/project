# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'post_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['myuser.MyUser'])),
            ('body_text', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lat_x', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('lng_y', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
            ('reference', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['category.CategoryMiddle'])),
        ))
        db.send_create_signal(u'post', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'post_post')


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
        },
        u'myuser.myuser': {
            'Meta': {'object_name': 'MyUser', 'db_table': "'myuser'"},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'post.post': {
            'Meta': {'object_name': 'Post'},
            'body_text': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['category.CategoryMiddle']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat_x': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            'lng_y': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            'reference': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myuser.MyUser']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['post']