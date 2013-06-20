# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BonusTime'
        db.create_table('common_bonustime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('begin_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('bonus_type', self.gf('django.db.models.fields.IntegerField')()),
            ('leverage', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['BonusTime'])

        # Adding model 'EventDefeatReward'
        db.create_table('common_eventdefeatreward', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')()),
            ('reward_id', self.gf('django.db.models.fields.IntegerField')()),
            ('reward_item_type', self.gf('django.db.models.fields.IntegerField')()),
            ('reward_item_id', self.gf('django.db.models.fields.IntegerField')()),
            ('reward_item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('reward_item_appearance', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('common', ['EventDefeatReward'])


    def backwards(self, orm):
        # Deleting model 'BonusTime'
        db.delete_table('common_bonustime')

        # Deleting model 'EventDefeatReward'
        db.delete_table('common_eventdefeatreward')


    models = {
        'common.bonustime': {
            'Meta': {'object_name': 'BonusTime'},
            'begin_at': ('django.db.models.fields.DateTimeField', [], {}),
            'bonus_type': ('django.db.models.fields.IntegerField', [], {}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            'event_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leverage': ('django.db.models.fields.IntegerField', [], {})
        },
        'common.eventdefeatreward': {
            'Meta': {'object_name': 'EventDefeatReward'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'event_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reward_id': ('django.db.models.fields.IntegerField', [], {}),
            'reward_item_appearance': ('django.db.models.fields.IntegerField', [], {}),
            'reward_item_count': ('django.db.models.fields.IntegerField', [], {}),
            'reward_item_id': ('django.db.models.fields.IntegerField', [], {}),
            'reward_item_type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['common']
