# -*- coding: utf-8 -*-
from django.contrib import admin
from twitter.models import Twitter, TwitterPlayerReward

class TwitterAdmin(admin.ModelAdmin):
    list_display=('id', 'category','master_id','image_categorys','image_item_ids', 'incentive_image', 'incentive_categorys','incentive_ids','incentive_nums','receive_type','incentive_text','body','detail_text','start_at','end_at')
    
class TwitterPlayerRewardAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                    'player_id',
                    'twitter_id',
                    'twitter_num',
                    ('updated_at', 'created_at')
                    ),
            }),
        )
    readonly_fields = ('created_at', 'updated_at',)

admin.site.register(Twitter, TwitterAdmin)
admin.site.register(TwitterPlayerReward, TwitterPlayerRewardAdmin)
