# -*- coding:utf-8 -*-

import actionlog

class TwitterActionLogUtils(object):
    
    @classmethod
    def write_beginning_twitter(cls, player, twitter_id, twitter_num):
        """
        twitter実行回数ログ
        """
        record = (
            '[TwitterId]', str(twitter_id),
            '[TwitterNum]', str(twitter_num)
            )
        actionlog.write('TWITTER_BEGINNING', player.pk, record)


    @classmethod
    def write_total_twitter(cls, player, twitter_id):
        """
        twitter実行ログ
        """
        record = (
            '[TwitterId]', str(twitter_id),
            )
        actionlog.write('TWITTER_TOTAL', player.pk, record)
