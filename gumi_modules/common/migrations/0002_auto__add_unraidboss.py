# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'UnRaidBoss'
        db.create_table('common_unraidboss', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('event_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('group_id', self.gf('django.db.models.fields.IntegerField')()),
            ('yakuza_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('max_hp', self.gf('django.db.models.fields.IntegerField')()),
            ('appearance_message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('win_message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lose_message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('win_message_alt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lose_message_alt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('extend_flag', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('common', ['UnRaidBoss'])


    def backwards(self, orm):
        
        # Deleting model 'UnRaidBoss'
        db.delete_table('common_unraidboss')


    models = {
        'common.bonustime': {
            'Meta': {'object_name': 'BonusTime'},
            'begin_at': ('django.db.models.fields.DateTimeField', [], {}),
            'bonus_type': ('django.db.models.fields.IntegerField', [], {}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {}),
            'event_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leverage': ('django.db.models.fields.IntegerField', [], {}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
        },
        'common.unraidboss': {
            'Meta': {'object_name': 'UnRaidBoss'},
            'appearance_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'event_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'extend_flag': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'group_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'lose_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lose_message_alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'max_hp': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'win_message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'win_message_alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'yakuza_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['common']
