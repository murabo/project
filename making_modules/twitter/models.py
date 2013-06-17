# -*- coding: utf-8 -*-

from __future__ import absolute_import

from datetime import timedelta

from django.db import models
from django.core.cache import cache
from django.conf import settings

from common.models import CachedMasterModel

from common.datetime_util import DatetimeUtil
from common.static_values import StaticValues

from player.models import Player
from gokujo.models import Gokujo
from item.models import GameItem
from yakuza.models import Yakuza
from equipment.models import YakuzaEquipmentItem, GokujoEquipmentItem

TWITTER_INCENTIVE_CATEGORY = {
    StaticValues.TYPE_NONE: None,
    StaticValues.TYPE_CARD: Yakuza,
    StaticValues.TYPE_ITEM: GameItem,
    StaticValues.TYPE_TREASURE: Gokujo,
    StaticValues.TYPE_MONEY: None,
    StaticValues.TYPE_POINT: None,
    StaticValues.TYPE_MEDAL: None,
    StaticValues.TYPE_SELF: Yakuza,
    StaticValues.TYPE_GOKUJOEQUIP: GokujoEquipmentItem,
    StaticValues.TYPE_YAKUZAEQUIP: YakuzaEquipmentItem
    }


TWITTER_RECEIVE_ONLY = 1
TWITTER_RECEIVE_DAY = 2

TWITTER_RECEIVE_TYPE = (
    (TWITTER_RECEIVE_ONLY, u'期間中1回限定'),
    (TWITTER_RECEIVE_DAY, u'期間中1日1回限定'),
)

APPLE_TOP_URL = 'mobile_index'

TWITTER_BODY = u'''
<a href="%(APPLE_TOP_URL)s">任侠道</a>&nbsp;%(BODY)s
'''

# TWITTER_RECEIVE_DAY 状況で初日
LIST_INDEX = 0

# TWITTER_RECEIVE_DAY 状況でCM件数
NEXT_INCENTIVE_LEN = 2

class Twitter(CachedMasterModel):
    """
    ひとことマスター
    """
    category = models.IntegerField(verbose_name=u'カテゴリー', default=0, choices=StaticValues.GAME_CATEGORY)
    master_id = models.IntegerField(verbose_name=u'関連ID')
    image_categorys = models.CharField(verbose_name=u'サムネルカテゴリーリスト', max_length=255, null=True, blank=True)
    image_item_ids = models.CharField(verbose_name=u'サムネルアイテムIDリスト', max_length=255, null=True, blank=True)
    incentive_categorys = models.CharField(u'報酬カテゴリーリスト', max_length=255, null=True, blank=True)
    incentive_ids = models.CharField(u'報酬IDリスト', max_length=255, null=True, blank=True)
    incentive_nums = models.CharField(u'報酬個数リスト', max_length=255, null=True, blank=True)
    incentive_text = models.TextField(u'プレゼント内容', default='', null=True, blank=True)
    title_text = models.CharField(u'タイトル', max_length=255, null=True, blank=True)
    receive_type = models.IntegerField(verbose_name=u'受け取り方', default=TWITTER_RECEIVE_ONLY, choices=TWITTER_RECEIVE_TYPE)
    body = models.TextField(u'一言内容', default='', null=True, blank=True)
    detail_text = models.TextField(u'詳細', default='', null=True, blank=True)
    start_at = models.DateTimeField(u'開始日時', null=True, blank=True)
    end_at = models.DateTimeField(u'終了日時', null=True, blank=True)

    class Meta:
        verbose_name = u'ひとことマスター'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s:%s' % (self.master_id, self.body)

    def incentive(self, num):
        """
        インセンティブを取る
        """
        o = self.get_incentive_category_obj(num)
        if o is None:
            return None

        return o.get(self.get_incentive_id(num))


    def incentive_image(self):
        ids = self.image_item_ids
        if not ids or ids is None:
            ids = self.get_incentive_ids()
        if not ids or ids is None:
            from twitter.api import TwitterFunctionAPI
            return '<p><img src="%s" width="40" height="40" /></p>' % TwitterFunctionAPI.get_apple_image_75()

        urls = []
        for id in ids:
            if id is None:
                continue
            url = [settings.MEDIA_URL, '/images/gameitem/40/', str(id), '.gif']
            urls.append("".join(url))
        tags = []
        for url in urls:
            tags.append('<p><img src="%s" width="40" height="40" /></p>' % url)
        return "".join(tags)
    incentive_image.allow_tags = True
    incentive_image.short_description = u'サムネイル'

    def get_incentive_ids(self):
        return charfield_split(self.incentive_ids)

    def get_incentive_id(self, num):

        incentive_ids = self.get_incentive_ids()

        if incentive_ids is None:
            return None
        try:
            return incentive_ids[num]
        except:
            if len(incentive_ids) > 1:
                return None
            else:
                return incentive_ids[LIST_INDEX]

    def get_incentive_categorys(self):
        return charfield_split(self.incentive_categorys)

    def get_incentive_category(self, num):

        incentive_categorys = self.get_incentive_categorys()

        if incentive_categorys is None:
            return incentive_categorys

        try:
            return incentive_categorys[num]
        except:
            return incentive_categorys[LIST_INDEX]


    def get_incentive_category_obj(self, num):

        incentive_category = self.get_incentive_category(num)
        if incentive_category is None:
            return None

        return TWITTER_INCENTIVE_CATEGORY.get(incentive_category, None)

    def get_image_category_obj(self, num):

        image_categorys = charfield_split(self.image_categorys)
        if image_categorys is None:
            return None

        try:
            image_category = image_categorys[num]
        except:
            image_category = image_categorys[LIST_INDEX]

        return TWITTER_INCENTIVE_CATEGORY.get(image_category, None)

    def is_image(self, num):

        image_category = self.get_image_category_obj(num)

        return False if image_category is None or image_category == StaticValues.TYPE_NONE else True

    def is_incentive(self, num):

        incentive_category = self.get_incentive_category_obj(num)

        return False if incentive_category is None or incentive_category == StaticValues.TYPE_NONE else True
    def get_incentive_nums(self, num):
        return charfield_split(self.incentive_nums)

    def incentive_num(self, num):
        incentive_nums = self.get_incentive_nums(num)
        if incentive_nums is None:
            return None

        try:
            return incentive_nums[num]
        except:
            return incentive_nums[LIST_INDEX]
        else:
            return LIST_INDEX
    # おかしい
    def get_all_incentive(self):
        incentives = []
        if self.get_incentive_ids():
            for i, incentive_id in enumerate(self.get_incentive_ids()):
                incentives.append(self.incentive(i))

        return incentives
    
    @classmethod
    def get_active(cls, twitter_id):
        """
        現在有効なものを取得
        ここでフォロー漏れがあるとCSになっちゃうよ
        """
        try:
            twitter_id = int(twitter_id)
        except:
            return False

        twitter = cls.get(twitter_id)
       
        if not twitter or twitter is None:
            return False
        if not twitter.enable:
            return False
        if not cls.is_in_period(twitter):
            return False
        return True
    
    @classmethod
    def is_in_period(cls, twitter):
        """
        有効期限内のTwitterかどうか
        """
        if not twitter or twitter is None:
            return False

        now = DatetimeUtil.now()
        if twitter.start_at and twitter.start_at > now:
            return False
        if twitter.end_at and twitter.end_at < now:
            return False
        return True

class TwitterPlayerReward(CachedMasterModel):
    """
    ひとこと報酬受け取り履歴
    """
    player_id = models.CharField(verbose_name=u'PlayerID', max_length=255)
    twitter_id = models.IntegerField(verbose_name="ひとことID")
    twitter_num = models.IntegerField(verbose_name="ひとこと回数", default=1)
    updated_at = models.DateTimeField(u'更新日時')
    created_at = models.DateTimeField(u'作成日時', auto_now_add=True, editable=False)

    class Meta:
        unique_together = (("player_id", "twitter_id", "twitter_num"))
        verbose_name = u'ひとこと受け取る報酬'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'twitterID:%s | PlayerID:%s ' % (self.twitter_id, self.player_id)

    def save(self, *args, **kwargs):
        auto_now = kwargs.pop('updated_at_auto_now', True)
        if auto_now:
            self.updated_at = DatetimeUtil.now().date()
        super(TwitterPlayerReward, self).save(*args, **kwargs)
        cache.set(TwitterPlayerReward.get_reward_for_player_and_twitter_cache_key(self.player_id, self.twitter_id), None)

    def delete(self, *args, **kwargs):
        cache.set(TwitterPlayerReward.get_reward_for_player_and_twitter_cache_key(self.player_id, self.twitter_id), None)
        super(TwitterPlayerReward, self).delete(*args, **kwargs)

    @property
    def twitter(self):
        return Twitter.get(self.twitter_id)

    @property
    def player(self):
        return Player.get(self.player_id)

    @classmethod
    def assign(cls, player, twitter_id):
        o, is_new = cls.objects.get_or_create(player_id=player.pk, twitter_id=twitter_id)
        if not is_new:
            o.twitter_num += 1
            o.save()
        return o

    @classmethod
    def get_reward_for_player_and_twitter_cache_key(cls, player_id, twitter_id):
        return u"%s::Player::%s::Twitter::%s" % (cls.__name__, player_id, twitter_id)

    @classmethod
    def get_reward_for_player_and_twitter(cls, player_id, twitter_id):
        cache_path = cache.get(cls.get_reward_for_player_and_twitter_cache_key(player_id, twitter_id))
        record = cache.get(cache_path, None)
        if record is None:
            try:
                record = cls.objects.get(player_id=player_id, twitter_id=twitter_id)
                cache.set(record)
            except:
                pass

        return record

    def can_twitter(self):
        twitter = Twitter.get(self.twitter_id)

        if twitter.receive_type == TWITTER_RECEIVE_ONLY:
            pass
        elif twitter.receive_type == TWITTER_RECEIVE_DAY:
            if DatetimeUtil.now().date() - self.updated_at.date() >= timedelta(days=1):
                return True

        return False


def charfield_split(var=None):
    if not var:
        return None

    if not isinstance(var, unicode):
        return None

    return [int(i) for i in var.split(',')]
