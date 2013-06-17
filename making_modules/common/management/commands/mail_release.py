# -*- coding: utf-8 -*-
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

from gameevent.models import GameEvent
from gacha.models import Gacha
from medal.models import MedalExchangeMaster
from django.db.models import Q
from django.conf import settings

SUBJECT = str("【任侠道】本日リリース、クローズ予定のリスト")

if settings.DEBUG:
    FROM_MAIL = "sakai@gu3.co.jp"
    TO_MAIL = "gokudo_engieers@gu3.co.jp"
else:
    FROM_MAIL = "batch-report@gu3.co.jp"
    TO_MAIL = "yakuza@gu3.co.jp"

class Command(BaseCommand):   
    def handle(self, *args, **options):
        """
        本日リリース、クローズ予定のリストをメールする
        """
        #本日リリース、クローズ予定のものを取得
        range_start = datetime.datetime.today().strftime("%Y-%m-%d 00:00:00")
        range_end = datetime.datetime.today().strftime("%Y-%m-%d 23:59:59")

        event_plan = GameEvent.objects.filter(Q(event_start_at__range=(range_start,range_end)) | Q(event_end_at__range=(range_start,range_end))).using('replica')
        gacha_plan = Gacha.objects.filter(Q(date_start__range=(range_start,range_end)) | Q(date_end__range=(range_start,range_end))).using('replica')
        medal_plan = MedalExchangeMaster.objects.filter(Q(start_at__range=(range_start,range_end)) | Q(end_at__range=(range_start,range_end))).using('replica')

        #本文の生成
        word = str(datetime.date.today())+u"のリリース、クローズ予定のリストをご連絡致します。\n\n"
        release_list = str("【リリース】\n")
        close_list = str("\n【クローズ】\n")

        event_release = str("・ｲﾍﾞﾝﾄ\n")
        event_close   = str("・ｲﾍﾞﾝﾄ\n")

        gacha_release = str("・ｶﾞﾁｬ\n")
        gacha_close   = str("・ｶﾞﾁｬﾞ\n")

        medal_release = str("・ﾒﾀﾞﾙ\n")
        medal_close   = str("・ﾒﾀﾞﾙ\n")

        for event in event_plan:
            event_release += str(self.material_word(event.event_start_at,event.event_end_at,event.name,True))
            event_close += str(self.material_word(event.event_start_at,event.event_end_at,event.name,False))

        for gacha in gacha_plan:
            gacha_release += str(self.material_word(gacha.date_start,gacha.date_end,gacha.name,True))
            gacha_close += str(self.material_word(gacha.date_start,gacha.date_end,gacha.name,False))

        for medal in medal_plan:
            medal_release += str(self.material_word(medal.start_at,medal.end_at,medal.name,True))
            medal_close += str(self.material_word(medal.start_at,medal.end_at,medal.name,False))
        
        #本文の連結
        release_list += event_release + gacha_release + medal_release
        close_list += event_close + gacha_close + medal_close

        #メールの送信
        send_mail(SUBJECT, word+release_list+close_list, FROM_MAIL,[TO_MAIL], fail_silently=False)

    def material_word(self,start_at,end_at,name,date_flg):
        start = start_at.strftime("%Y-%m-%d")
        end = end_at.strftime("%Y-%m-%d")
        
        if date_flg:
            if start==datetime.date.today().strftime("%Y-%m-%d"):
                return u"  %s    %s\n" % (str(start_at),unicode(name))
            else:
                return ""
        else:
            if end==datetime.date.today().strftime("%Y-%m-%d"):   
                return u"  %s    %s\n" % (str(end_at),unicode(name))
            else:
                return ""
