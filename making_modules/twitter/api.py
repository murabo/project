# -*- coding: utf-8 -*-
from __future__ import absolute_import

import time
import urllib

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.conf import settings

from common.datetime_util import DatetimeUtil
from player.models import TestPlayer

from item.models import GameItem, PlayerItem
from gokujo.models import Gokujo, PlayerGokujo
from yakuza.models import Yakuza, PlayerYakuza
from equipment.models import YakuzaEquipmentItem, GokujoEquipmentItem
from present.models import PlayerPresent, PlayerWishList

from twitter.models import Twitter, TwitterPlayerReward, APPLE_TOP_URL, TWITTER_BODY, NEXT_INCENTIVE_LEN, TWITTER_RECEIVE_ONLY, TWITTER_RECEIVE_DAY
from twitter.actionlog_util import TwitterActionLogUtils
from common.static_values import StaticValues


class TwitterFunctionAPI(object):
    """
    一言共通化(ちゅんちゅん)
    ※ 一言必要の場合views 最後return 直前に 
        - context = TweetFuncionAPI.get_tweet_function(request, context, 文言, 戻るリング, obj, 戻るリングの引数)
    ※ 戻るurlリンク引数がないの場合take_overは無視
    ※ 一言終わって画面にButton表示しないの場合は
    ※ 画像表示が必要の場合objにinstanceを入れる
    """
    @classmethod
    def get_tweet_function_image(cls, request, ctxt, twitter_id, callbackurl=None, take_over=[]):
        """
        サムネルが付く一言
        """
        twitter = Twitter.get(int(twitter_id))
        if twitter is None:
            return cls.get_ctxt(request=request, ctxt=ctxt, is_twitter=False, can_twitter=False)
        
        if not Twitter.is_in_period(twitter):
            return cls.get_ctxt(request=request, ctxt=ctxt, is_twitter=False, can_twitter=False)
        
        twitter_player_reward = TwitterPlayerReward.get_reward_for_player_and_twitter(request.player.pk, twitter_id)
        
        num = 0
        if twitter_player_reward is not None:
            if not twitter_player_reward.can_twitter():
                return cls.get_ctxt(request=request, ctxt=ctxt, twitter=twitter, is_twitter=False)
            num += twitter_player_reward.twitter_num

        if callbackurl is None:
            callbackurl = "twitter_result_execute"
            take_over = [twitter_id]
        
        callbackurl = cls.get_callbackurl(request, callbackurl, take_over)
        image_url_75, image_url_240 = cls.get_image_url(twitter, num)
        
        return cls.get_ctxt(request, ctxt, callbackurl, twitter, image_url_75, image_url_240, twitter_id=twitter_id)
    
    @classmethod
    def get_callbackurl(cls, request, url, take_over=[]):
        """
        urlチェンジ
        """
        if request.is_smartphone:
            url = reverse(url, args=take_over)
            url = 'http://%s%s' % (settings.SITE_DOMAIN_SP, url)
        else:
            url = reverse(url, args=take_over)
            url = 'http://%s%s?signed=1&guid=ON&t=%s' % (settings.SITE_DOMAIN_FP, url, int(time.time()))
        
        return urllib.quote(url)
    
    @classmethod
    def get_image_url(cls, obj, num):
        
        if not obj.is_image(num):
            return cls.get_apple_image()
        get_image_category_obj = obj.get_image_category_obj(num)

        if get_image_category_obj is None:
            if get_image_category_obj == StaticValues.TYPE_MONEY:
                return cls.get_apple_image()
            elif get_image_category_obj == StaticValues.TYPE_POINT:
                return cls.get_apple_image()
            elif get_image_category_obj == StaticValues.TYPE_MEDAL:
                return cls.get_apple_image()
            else:
                return cls.get_apple_image()

        o = get_image_category_obj.get(obj.image_item_id)

        if o is None:
            return cls.get_apple_image()

        return cls._get_image_url(o)
    
    @classmethod
    def get_yakuza_image(cls, yakuza):
        return yakuza.image_url_m(), yakuza.image_url()
    
    @classmethod
    def get_gokujo_image(cls, gokujo):
        return obj.image_url_s_for_media(), obj.image_url_event_zukan() if obj.is_treasure else obj.image_url()
    
    @classmethod
    def get_gameitem_image(cls, item):
        return obj.image_url_comp(), obj.image_url()

    @classmethod
    def get_equipmentitem_image(cls, equipment):
        return obj.image_url_s(), obj.image_url()
    
    @classmethod
    def get_money_image(cls):
        return None, None
    
    @classmethod
    def get_medal_image(cls):
        return None, None
    
    @classmethod
    def get_point_image(cls):
        return None, None

    @classmethod
    def get_apple_image(cls):
        return cls.get_apple_image_75(), cls.get_apple_image_240()
    
    @classmethod
    def get_apple_image_75(self):
        return settings.MEDIA_URL + '/images/twitter/75/apple.gif'
    
    @classmethod
    def get_apple_image_240(self):
        return settings.MEDIA_URL + '/images/twitter/240/apple.gif'
    
    @classmethod
    def _get_image_url(cls, o=None):
        """
        表示するサムネルを取る
        """
        if o is None:
            return cls.get_apple_image()
        
        try:
            if isinstance(o, Yakuza):
                cls.get_yakuza_image(o)
            elif isinstance(o, PlayerYakuza):
                image_url_75 = o.yakuza.image_url_m()
                image_url_240 = o.yakuza.image_url()
            elif isinstance(o, GameItem):
                cls.get_gameitem_image(o)
            elif isinstance(o, PlayerItem):
                image_url_75 = o.item.image_url_comp()
                image_url_240 = o.item.image_url()
            elif isinstance(o, Gokujo):
                cls.get_gokujo_image(o)
            elif isinstance(o, PlayerGokujo):
                image_url_75 = o.gokujo.image_url_s_for_media()
                image_url_240 = o.gokujo.image_url_event_zukan() if o.is_treasure else o.image_url()
            else:
                cls.get_equipmentitem_image(o)
        except:
            return cls.get_apple_image()

        return image_url_75, image_url_240
    
    @classmethod
    def twitter_incentive_present(cls, player, twitter_id):
        TwitterActionLogUtils.write_total_twitter(player, twitter_id)
        twitter_player_reward = TwitterPlayerReward.get_reward_for_player_and_twitter(player.pk, twitter_id)
        num = 0
        if twitter_player_reward:
            if not twitter_player_reward.can_twitter():
                return False
            num += twitter_player_reward.twitter_num
        
        twitter = Twitter.get(twitter_id)

        if twitter is None:
            return False
        try:
            o = twitter.incentive(num)
        except:
            o = None
        if not o is None:
            incentive_type = twitter.get_incentive_category(num)
            if incentive_type == StaticValues.TYPE_ITEM and o and o.melt_down_time:
                # 溶けるアイテムならば直接付与
                PlayerItem.assign(player, o, twitter.incentive_num(num))
            else:
                PlayerPresent.give_official_present(player, o, twitter.incentive_text, num=twitter.incentive_num(num), type=twitter.get_incentive_category(num))
        
        twitter_player_reward = TwitterPlayerReward.assign(player, twitter.id)
        TwitterActionLogUtils.write_beginning_twitter(player, twitter_id, twitter_player_reward.twitter_num)

        cache_path = u'Twitter::%s::Player::%s' % (twitter_player_reward.twitter_id, player.pk)
        cache.set(cache_path, o, 5)

        return False

    @classmethod
    def get_incentive_present(cls, player, twitter_id):
        cache_path = u'Twitter::%s::Player::%s' % (twitter_id, player.pk)
        twitter = Twitter.get(twitter_id)
        error = None
        if twitter is None or not twitter:
            error = True
        return cache.get(cache_path, None), error
    
    @classmethod
    def get_ctxt(cls, request, ctxt, callbackurl=None, twitter=None, image_url_75=None, image_url_240=None, is_twitter=True, can_twitter=True, twitter_id=0):
        """
        Twitter系はここでfixしないとCSにつながるので注意
        """
        
        if is_twitter:
            body_values = {
                'BODY': twitter.body if twitter is not None else u'',
                }
        else:
            body_values = {
                'BODY': u'',
                }

        # 引数FIX (取得したtwitterインスタンスが有効期限外、あるいは無効であればとりあえず表示させない)
        if twitter is None or not twitter:
            if twitter_id == 0 and can_twitter:
                can_twitter = False
        if twitter:
            if not Twitter.is_in_period(twitter):
                can_twitter = False

        is_next_twitter = False
        if twitter and twitter.receive_type == TWITTER_RECEIVE_DAY and not is_twitter:
            is_next_twitter = True if (twitter.end_at.date() - DatetimeUtil.now().date()).days > 0 else False

        ctxt.update({
                'callbackurl': callbackurl,
                'twitter': twitter,
                'is_twitter': is_twitter,
                'is_next_twitter': is_next_twitter,
                'body_values': body_values,
                'image_url_75': image_url_75,
                'image_url_240': image_url_240,
                'can_twitter': can_twitter,
                'debug': settings.OPENSOCIAL_DEBUG,
                'twitter_id': twitter_id,
                })
        return ctxt
    
    @classmethod
    def get_twitter_player_reward(cls, player, twitter_id):
        return TwitterPlayerReward.get_reward_for_player_and_twitter(player.pk, twitter_id)

    @classmethod
    def get_next_incentive(cls, player, twitter_player_reward):
        twitter = twitter_player_reward.twitter
        next_incentives = None
        
        if twitter.receive_type == TWITTER_RECEIVE_ONLY:
            return twitter, None
        elif twitter.receive_type == TWITTER_RECEIVE_DAY:
            num = twitter_player_reward.twitter_num
            days = (twitter.end_at.date() - twitter_player_reward.updated_at.date()).days
            days = min(days, NEXT_INCENTIVE_LEN)
            all_incentive = twitter.get_all_incentive()
            next_incentives = []
            for i in range(num, num + days):
                try:
                    if all_incentive[i]:
                        next_incentives.append(all_incentive[i])
                except:
                    pass
    
        return twitter, next_incentives
    
    @classmethod
    def is_active(cls, twitter_id):
        if Twitter.get_active(twitter_id):
            return True
        return False

