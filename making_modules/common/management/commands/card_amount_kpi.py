# -*- coding:utf-8 -*-
"""
解析用
カード流通量調査用バッチ
"""
from __future__ import absolute_import

import datetime
from django.core.management.base import BaseCommand
from django.db import connections

from common.static_values import StaticValues

from player.models import Player
from yakuza.models import Yakuza

from gamelog.cards_snapshot import insert_cardsnapshot_records

class Command(BaseCommand):

    def handle(self, *args, **options):
        print "=== GOKUDO ==========================="
        print "Card amount KPI Batch >> START >>"
        #logger.info "Card amount KPI Batch >> START >>"
        
        # 2週間以内にログインしているユーザー
        target_date = datetime.date.today() - datetime.timedelta(days=14)
        target_datetime = datetime.datetime(
                target_date.year, target_date.month, target_date.day, 0, 0)
        target_datetime_str = target_datetime.strftime("%Y-%m-%d")

        # PlayerYakuzaテーブルをcard_idでgroupしたcountを取得card_idでソート
        # 所有数
        HAVING_COUNT_SQL = """
        SELECT y_py.yakuza_id, count(y_py.id) as cnt
        FROM yakuza_playeryakuza as y_py
        WHERE y_py.player_id in
        (SELECT osuser_id FROM player_player as pp WHERE pp.last_login_at >= '%s')
        GROUP BY y_py.yakuza_id
        """ % (target_datetime_str)
        
        # 未受取数
        PRESENT_COUNT_SQL = """
        SELECT y_py.yakuza_id, count(y_py.id) as cnt
        FROM present_playerpresent as p_pp
        JOIN yakuza_playeryakuza as y_py ON p_pp.present = y_py.id AND p_pp.type = %s
        WHERE p_pp.player_id in
        (SELECT osuser_id FROM player_player as pp WHERE pp.last_login_at >= '%s')
        GROUP BY y_py.yakuza_id
        """ % (StaticValues.TYPE_CARD, target_datetime_str)
        
        SQL1 = "SELECT f1.yakuza_id, f1.cnt, f2.cnt FROM (%s) as f1 LEFT OUTER JOIN (%s) as f2 ON f1.yakuza_id = f2.yakuza_id" % (HAVING_COUNT_SQL, PRESENT_COUNT_SQL)
        SQL2 = "SELECT f2.yakuza_id, f1.cnt, f2.cnt FROM (%s) as f1 RIGHT OUTER JOIN (%s) as f2 ON f1.yakuza_id = f2.yakuza_id" % (HAVING_COUNT_SQL, PRESENT_COUNT_SQL)
        
        EXEC_SQL = "(%s) UNION (%s)" % (SQL1, SQL2)
        
        #print EXEC_SQL

        datas = []
        all_data = {}

        # 総計を求める
        cursor = connections['other'].cursor()
        cursor.execute(EXEC_SQL)
        rows = cursor.fetchall()
        
        print "FULL COUNT %s" % len(rows)
        
        # dictを作る
        for i, r in enumerate(rows):
            card_id = r[0]
            own_num     = 0 if r[1] is None else r[1]
            present_num = 0 if r[2] is None else r[2]
            d = {}
            if all_data.has_key(card_id):
                d = all_data[card_id]
                d["own"]     += own_num
                d["present"] += present_num
                continue
            y = Yakuza.get(card_id)
            d["card_id"]   = card_id
            d["card_name"] = y.name
            d["own"]       = own_num
            d["present"]   = present_num
            d["rank"]      = y.rarity
            d["rarity"]    = y.rarity

            all_data[card_id] = d

            print "%s DONE." % i


        datas = all_data.values()
        #print datas
        # apiをcall
        # insertされるとinsertされた行数を返します(By README)
        from gamelog.cards_snapshot.database_settings import GAMELOG_CARDSNAPSHOT_DATABASE
        insert_row = insert_cardsnapshot_records("gokudo_gree", datas, GAMELOG_CARDSNAPSHOT_DATABASE)
        print "Insert DONE! (%s record[s])" % insert_row

        # 終了
        print "Card amount KPI Batch << E N D <<"
        print "=== GOKUDO ==========================="
