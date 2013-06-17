# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Twitter'
        db.create_table('twitter_twitter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('category', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('master_id', self.gf('django.db.models.fields.IntegerField')()),
            ('image_categorys', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('image_item_ids', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('incentive_categorys', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('incentive_ids', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('incentive_nums', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('incentive_text', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('title_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('receive_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('body', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('detail_text', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('twitter', ['Twitter'])

        # Adding model 'TwitterPlayerReward'
        db.create_table('twitter_twitterplayerreward', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('player_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('twitter_id', self.gf('django.db.models.fields.IntegerField')()),
            ('twitter_num', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('twitter', ['TwitterPlayerReward'])

        # Adding unique constraint on 'TwitterPlayerReward', fields ['player_id', 'twitter_id', 'twitter_num']
        db.create_unique('twitter_twitterplayerreward', ['player_id', 'twitter_id', 'twitter_num'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'TwitterPlayerReward', fields ['player_id', 'twitter_id', 'twitter_num']
        db.delete_unique('twitter_twitterplayerreward', ['player_id', 'twitter_id', 'twitter_num'])

        # Deleting model 'Twitter'
        db.delete_table('twitter_twitter')

        # Deleting model 'TwitterPlayerReward'
        db.delete_table('twitter_twitterplayerreward')


    models = {
        'twitter.twitter': {
            'Meta': {'object_name': 'Twitter'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'detail_text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_categorys': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'image_item_ids': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'incentive_categorys': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'incentive_ids': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'incentive_nums': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'incentive_text': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'master_id': ('django.db.models.fields.IntegerField', [], {}),
            'receive_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'twitter.twitterplayerreward': {
            'Meta': {'unique_together': "(('player_id', 'twitter_id', 'twitter_num'),)", 'object_name': 'TwitterPlayerReward'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_id': ('django.db.models.fields.IntegerField', [], {}),
            'twitter_num': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['twitter']
