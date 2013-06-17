# -*- coding: utf-8 -*-

import actionlog

from common.static_values import StaticValues

'''

インスペクターログのユーティリティクラス

使い方の例：
from common.inspector_utils import InspectorLogUtils

InspectorLogUtils.write_create_log(引数)

TIPS! 重要なこと
数値、Falseなど、アスキー文字列で表せるものは 文字列 で保存します。
日本語が含まれる可能性がある場合、必ず「repr」で変換してください。
ログに保存可能なのはアスキー文字列のみです。

インスペクターログに保存する場合、以下の情報は保存する必要はありません。
・実行しているユーザのIDと名前

インスペクターログでマスターにあるオブジェクト（アイテムや極道など）を保存する場合、次のキーを保存して下さい。
・オブジェクトのIDと名前
　※IDだけ、名前だけ、は調査困難となりますので、使用しないで下さい。

オブジェクトの数の増減がある場合（アイテムが増えるとか）、増減前、増減後も可能な限りいれましょう
　※お金とかも前と後があると追跡で便利です

インスペクターログに使用可能な文字列：
ASCII文字列のみ。変化のない値（ログのタイトルなど）でSQL上で使うのにエスケープが必要な記号は使わないようにしましょう！
　※?とか*とか%とか


'''

class InspectorLogUtils(object):

    REASON_GACHA = 'GACHA' # ガチャ
    REASON_MISSION = 'MISSION' # 地回り
    REASON_REWARD = 'REWARD' # イベントなどの報酬
    REASON_PRESENT = 'PRESENT' # プレゼント
    REASON_ENHANCEMENT = 'ENHANCEMENT' # 入魂 既存の舎弟強化なので使わないはず
    REASON_EVOLUTION = 'EVOLUTION' # 覚醒入魂
    REASON_SELL = 'SELL' # カタギに戻す
    REASON_LOGIN_BONUS = 'LOGIN_BONUS' # ログインボーナス
    REASON_MEDAL = 'MEDAL' # レア代紋
    REASON_CAMPAIGN = 'CAMPAIGN_%s_%s' # キャンペーン。開始日、終了日を入れる
    REASON_TRADE = 'TRADE' # トレード
    REASON_SHOP = 'SHOP' # ショップ
    REASON_EXCHANGE = 'EXCHANGE' # レア代紋に舎弟交換
    REASON_POKE = 'POKE' # 盃を交わす
    REASON_BATTLE = 'BATTLE' # バトル用途
    REASON_REPAIR = 'REPAIR' # 補償系
    REASON_PROMOTION = 'PROMOTION' # Promotion

    ITEM_TYPE_CARD = 'CARD' # 舎弟
    ITEM_TYPE_ITEM = 'ITEM' # アイテム
    ITEM_TYPE_KEYITEM = 'KEYITEM' # 秘宝
    ITEM_TYPE_TICKET = 'TICKET' # ガチャチケット。任侠道ではプレゼント不可なので、使ってない
    ITEM_TYPE_MONEY = 'MONEY' # 銭
    ITEM_TYPE_POINT = 'POINT' # 盃pt
    ITEM_TYPE_MEDAL = 'MEDAL' # レア代紋
    ITEM_TYPE_GOKUJOEQUIP = 'GOKUJOITEM' # 極女装備
    ITEM_TYPE_YAKUZAEQUIP = 'YAKUZAITEM' # 舎弟装備

    @classmethod
    def write_create_log(cls, player, item_list, reason=REASON_GACHA, reference=None):
        """
        ゲーム内でアイテムが純粋に増えた場合に使用するログ
        item_list = (
            (タイプ, ID, レアリティ（舎弟と秘宝のみ。他は０固定）, 数量),
        )
        """
        if not item_list:
            return

        record = []
        for number, item_data in enumerate(item_list):
            item_type, item_id, item_rarity, item_quantity = item_data

            type_string = cls.ITEM_TYPE_CARD
            if item_type == StaticValues.TYPE_CARD:
                type_string = cls.ITEM_TYPE_CARD
            elif item_type == StaticValues.TYPE_ITEM:
                type_string = cls.ITEM_TYPE_ITEM
            elif item_type == StaticValues.TYPE_MEDAL:
                type_string = cls.ITEM_TYPE_MEDAL
                if item_id > 0:
                    item_quantity = item_id
                    item_id = 0
            elif item_type == StaticValues.TYPE_MONEY:
                type_string = cls.ITEM_TYPE_MONEY
                if item_id > 0:
                    item_quantity = item_id
                    item_id = 0
            elif item_type == StaticValues.TYPE_POINT:
                type_string = cls.ITEM_TYPE_POINT
                if item_id > 0:
                    item_quantity = item_id
                    item_id = 0
            elif item_type == StaticValues.TYPE_TREASURE:
                type_string = cls.ITEM_TYPE_KEYITEM

            record.append('[ITEM_%d]' % (number+1))
            record.append('%s/%s/%s/%s' % (type_string, str(item_id), str(item_rarity), str(int(item_quantity))))

        record.append('[REASON]')
        record.append(reason)

        record.append('[REFERENCE]')
        if not reference:
            record.append('None')
        else:
            record.append(reference)

        actionlog.write('IL_CREATE', player.pk, record)

    @classmethod
    def write_delete_log(cls, player, item_list, reason=REASON_GACHA, reference=None):
        """
        ゲーム内でアイテムが純粋に減った場合に使用するログ
        item_list = (
            (タイプ, ID, レアリティ（舎弟と秘宝のみ。他は０固定）, 数量),
        )
        """
        if not item_list:
            return
        
        record = []
        for number, item_data in enumerate(item_list):
            item_type, item_id, item_rarity, item_quantity = item_data

            type_string = cls.ITEM_TYPE_CARD
            if item_type == StaticValues.TYPE_CARD:
                type_string = cls.ITEM_TYPE_CARD
            elif item_type == StaticValues.TYPE_ITEM:
                type_string = cls.ITEM_TYPE_ITEM
            elif item_type == StaticValues.TYPE_MEDAL:
                type_string = cls.ITEM_TYPE_MEDAL
                if item_id > 0:
                    item_quantity = item_id
                    item_id = 0
            elif item_type == StaticValues.TYPE_MONEY:
                type_string = cls.ITEM_TYPE_MONEY
                if item_id > 0:
                    item_quantity = item_id
                    item_id = 0
            elif item_type == StaticValues.TYPE_POINT:
                type_string = cls.ITEM_TYPE_POINT
                if item_id > 0:
                    item_quantity = item_id
                    item_id = 0
            elif item_type == StaticValues.TYPE_TREASURE:
                type_string = cls.ITEM_TYPE_KEYITEM
            elif item_type == StaticValues.TYPE_GOKUJOEQUIP:
                type_string = cls.ITEM_TYPE_GOKUJOEQUIP
            elif item_type == StaticValues.TYPE_YAKUZAEQUIP:
                type_string = cls.ITEM_TYPE_YAKUZAEQUIP

            record.append('[ITEM_%d]' % (number+1))
            record.append('%s/%s/%s/%s' % (type_string, str(item_id), str(item_rarity), str(int(item_quantity))))

        record.append('[REASON]')
        record.append(reason)

        record.append('[REFERENCE]')
        if not reference:
            record.append('None')
        else:
            record.append(reference)

        actionlog.write('IL_DELETE', player.pk, record)

    @classmethod
    def write_transfer_log(cls, player, target_player, applicant_item_list, recipient_item_list, reason=REASON_GACHA, reference=None):
        """
        ゲーム内でアイテムの移動が発生した場合に出力するログ。
        移動した事実が重要。成立したときのみ出力します
        applicant_item_list = (
            (タイプ, ID, レアリティ（舎弟と秘宝のみ。他は０固定）, 数量),
        )

        applicant_item_list: 申し込んだ側(player)の提出したアイテム
        recipient_item_list: 申し込まれた側(target_player)の提出したアイテム
        """
        record = []
        for number, item_data in enumerate(applicant_item_list):
            item_type, item_id, item_rarity, item_quantity = item_data

            type_string = cls.ITEM_TYPE_CARD
            if item_type == StaticValues.TYPE_CARD:
                type_string = cls.ITEM_TYPE_CARD
            elif item_type == StaticValues.TYPE_ITEM:
                type_string = cls.ITEM_TYPE_ITEM
            elif item_type == StaticValues.TYPE_MEDAL:
                type_string = cls.ITEM_TYPE_MEDAL
            elif item_type == StaticValues.TYPE_MONEY:
                type_string = cls.ITEM_TYPE_MONEY
            elif item_type == StaticValues.TYPE_POINT:
                type_string = cls.ITEM_TYPE_POINT
            elif item_type == StaticValues.TYPE_TREASURE:
                type_string = cls.ITEM_TYPE_KEYITEM
            elif item_type == StaticValues.TYPE_GOKUJOEQUIP:
                type_string = cls.ITEM_TYPE_GOKUJOEQUIP
            elif item_type == StaticValues.TYPE_YAKUZAEQUIP:
                type_string = cls.ITEM_TYPE_YAKUZAEQUIP

            record.append('[APPLICANT_%d]' % (number+1))
            record.append('%s/%s/%s/%s' % (type_string, str(item_id), str(item_rarity), str(int(item_quantity))))

        for number, item_data in enumerate(recipient_item_list):
            item_type, item_id, item_rarity, item_quantity = item_data

            type_string = cls.ITEM_TYPE_CARD
            if item_type == StaticValues.TYPE_CARD:
                type_string = cls.ITEM_TYPE_CARD
            elif item_type == StaticValues.TYPE_ITEM:
                type_string = cls.ITEM_TYPE_ITEM
            elif item_type == StaticValues.TYPE_MEDAL:
                type_string = cls.ITEM_TYPE_MEDAL
            elif item_type == StaticValues.TYPE_MONEY:
                type_string = cls.ITEM_TYPE_MONEY
            elif item_type == StaticValues.TYPE_POINT:
                type_string = cls.ITEM_TYPE_POINT
            elif item_type == StaticValues.TYPE_TREASURE:
                type_string = cls.ITEM_TYPE_KEYITEM
            elif item_type == StaticValues.TYPE_GOKUJOEQUIP:
                type_string = cls.ITEM_TYPE_GOKUJOEQUIP
            elif item_type == StaticValues.TYPE_YAKUZAEQUIP:
                type_string = cls.ITEM_TYPE_YAKUZAEQUIP

            record.append('[RECIPIENT_%d]' % (number+1))
            record.append('%s/%s/%s/%s' % (type_string, str(item_id), str(item_rarity), str(int(item_quantity))))

        record.append('[APPLICANT]')
        record.append(player.pk)

        record.append('[RECIPIENT]')
        record.append(target_player.pk)

        record.append('[REASON]')
        record.append(reason)

        record.append('[REFERENCE]')
        if not reference:
            record.append('None')
        else:
            record.append(reference)

        actionlog.write('IL_DELETE', player.pk, record)

    @classmethod
    def write_create_for_jimawari(cls, player, money, yakuzas=[], gokujos=[], items=[], ref=None):
        if yakuzas and not isinstance(yakuzas, list):
            yakuzas = [yakuzas]
        if gokujos and not isinstance(gokujos, list):
            gokujos = [gokujos]
        if items and not isinstance(items, list):
            items = [items]

        inspector_items = []
        inspector_items.append((StaticValues.TYPE_MONEY, 0, 0, money))

        if yakuzas:
            for yakuza in yakuzas:
                inspector_items.append((StaticValues.TYPE_CARD, yakuza.pk, yakuza.rarity, 1))

        if gokujos:
            for gokujo in gokujos:
                if not gokujo.is_treasure:
                    continue
                inspector_items.append((StaticValues.TYPE_TREASURE, gokujo.pk, 0, 1))

        if items:
            for item in items:
                inspector_items.append((StaticValues.TYPE_ITEM, item.pk, 0, 1))

        cls.write_create_log(player, inspector_items, cls.REASON_MISSION, ref)



