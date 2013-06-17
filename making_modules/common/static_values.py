# -*- coding:utf-8 -*-
from django.conf import settings
import datetime

class StaticValues(object):

    RECOVER_POWER = settings.RECOVER_POWER
    RECOVER_LOVE = settings.RECOVER_LOVE

    MAX_PLAYER_LEVEL = 210

    MAX_PLAYER_NAME_LENGTH = 50

    LIMIT_FRIEND_DATE = 14

    # 最大事務所拡張数
    #MAX_SHATEI_COUNT = 150
    #舎弟枠（事務所）上限が無くなったけどコード内で定数を使っている部分があるのでひとまず大きい数字に。コードの方を修正してこの定数も削除します。
    MAX_SHATEI_COUNT = 1000

    RECOVER_ITEM_ID = 1
    RECOVER_LOVE_ITEM_ID = 2
    RECOVER_ITEM_HUNDRED_ID = 97
    RECOVER_ITEM_HALF_ID = 109

    RECOVER_POWER_LIMITED_ID = 246
    RECOVER_LOVE_LIMITED_ID = 245

    #TODO:アイテム確認
    RECOVER_LOVE_ONE_ITEM_ID = 44 # 慈愛１回復アイテム
    RECOVER_LOVE_ONE_SELF_ITEM_ID = 377 # 自分専用慈愛１回復アイテム
    RECOVER_MINI_LOVE_ITEM_ID = 44
    #OWN_RECOVER_LOVE_ITEM_ID = 66
    OWN_RECOVER_LOVE_ITEM_ID = 137
    OWN_RECOVER_MINI_LOVE_ITEM_ID = 44

    OWN_RECOVER_ITEM_ID = 49
    TRAP_ITEM_ID = 14
    EVENT_TOWER_VIP_TICKET_ITEM_ID = 15
    EVENT_INVASION_VIP_TICKET_ITEM_ID = 27
    EVENT_CRYPTID_VIP_TICKET_ITEM_ID = 29
    EVENT_KACHIKOMI2_VIP_TICKET_ITEM_ID = 29
    EXTEND_OFFICE_ITEM_ID = 35
    EVENT_SAINT_VIP_TICKET_ITEM_ID = 37
    EVENT_SAINT_VIP_TICKET_ITEM_PRICE = 300
    EVENT_BREAK_VIP_TICKET_ITEM_ID = 40
    EVENT_TOKONATSU_VIP_TICKET_ITEM_ID = 48
    EVENT_GOKUPRO_VIP_TICKET_ITEM_ID = 72
    EVENT_BREAK_2_VIP_TICKET_ITEM_ID = 56
    EVENT_ONI_VIP_TICKET_ITEM_ID = 89
    EVENT_ONI_EQUIPMENT_ITEM_ID = [80, 81, 82, 83, 84, 85, 86, 87]
    EXTEND_OFFICE_MINI_ITEM_ID = 58
    EVENT_GOD_VIP_TICKET_ITEM_ID = 95
    EVENT_SUGOROKU_ITEM_ID = [188, 189]
    TIEUP_TICKET_ID = 108

    REWARD_HONEYS = [188, 189, 190]
    REWARD_HALF_HONEYS = [225, 226, 227]

    MAX_STORY_LEVEL = 3

    MAX_LOVE = 5

    FRIEND_BATTLE_CATEGORY_FACTOR = 1.2

    BOSS_BATTLE_CATEGORY_FACTOR = 1.3

    FRIEND_MAX_POWER_RATE = 1

    #盃をかわした後のｺﾒﾝﾄ文字制限
    BODY_TEXT_MAX_LENGTH = 30

    #最大交流ポイント
    MAX_COMMUNICATION_POINT = 89300

    # 神レアのIDリスト
    GOD_RARE_IDS = (1336, 1337, 1338, 1339, 1340, 1341)

    # 舎弟の性別
    YAKUZA_SEX_MALE = 1
    YAKUZA_SEX_FEMALE = 2
    YAKUZA_SEX_OGRE = 3

    YAKUZA_SEX = (
        (0, '未設定'),
        (YAKUZA_SEX_MALE, '男'),
        (YAKUZA_SEX_FEMALE, '女'),
        (YAKUZA_SEX_OGRE, '鬼'),
    )

    YAKUZA_SEX_VIEW = (
        (0, u'未設定'),
        (YAKUZA_SEX_MALE, u'男'),
        (YAKUZA_SEX_FEMALE, u'女'),
        (YAKUZA_SEX_OGRE, u'鬼'),
    )

    #属性（プレイヤーと舎弟にある）
    CATEGORY_ALL = 0 # カテゴリー用
    CATEGORY_FIGHTER = 1
    CATEGORY_GAMBLER = 2
    CATEGORY_INTERIGENCE = 3
    CATEGORY_EVOLUTION = 4
    CATEGORY_BATTLEMEMBER = 5

    # ダメージ倍率が上がる相手を拾う
    CATEGORY_RETIO_DOWN = {
        CATEGORY_FIGHTER: CATEGORY_GAMBLER,
        CATEGORY_GAMBLER: CATEGORY_INTERIGENCE,
        CATEGORY_INTERIGENCE: CATEGORY_FIGHTER,
    }

    # ダメージ倍率が下がる相手を拾う
    CATEGORY_RETIO_UP = {
        CATEGORY_GAMBLER: CATEGORY_FIGHTER,
        CATEGORY_INTERIGENCE: CATEGORY_GAMBLER,
        CATEGORY_FIGHTER: CATEGORY_INTERIGENCE,
    }

    # ダメージ倍率が上がる相手を拾う
    SEX_RETIO_UP = {
        YAKUZA_SEX_MALE: YAKUZA_SEX_OGRE,
        YAKUZA_SEX_OGRE: YAKUZA_SEX_FEMALE,
        YAKUZA_SEX_FEMALE: YAKUZA_SEX_MALE,
    }

    # ダメージ倍率が下がる相手を拾う
    SEX_RETIO_DOWN = {
        YAKUZA_SEX_OGRE: YAKUZA_SEX_MALE,
        YAKUZA_SEX_FEMALE: YAKUZA_SEX_OGRE,
        YAKUZA_SEX_MALE: YAKUZA_SEX_FEMALE,
    }

    YAKUZA_CATEGORY = (
        (0, '未設定'),
        (CATEGORY_FIGHTER, '武闘'),
        (CATEGORY_GAMBLER, '博徒'),
        (CATEGORY_INTERIGENCE, 'ｲﾝﾃﾘ'),
    )
    YAKUZA_CATEGORY_NAMES = (
        (0, u'未設定' , u'未', '#CCCCCC'),
        (CATEGORY_FIGHTER, u'武闘' , u'武', '#FF0000'),
        (CATEGORY_GAMBLER, u'博徒' , u'博', '#00CC00'),
        (CATEGORY_INTERIGENCE, u'ｲﾝﾃﾘ' , u'イ', '#0099FF'),
    )
    VIEW_ALL = 0
    YAKUZA_CATEGORY_VIEW = (
        (VIEW_ALL, u'全部'),
        (CATEGORY_FIGHTER, u'武闘'),
        (CATEGORY_GAMBLER, u'博徒'),
        (CATEGORY_INTERIGENCE, u'ｲﾝﾃﾘ'),
    )

    YAKUZA_CATEGORY_VIEW_EXCLUDE_ALL = (
        (CATEGORY_ALL, u'全部'),
        (CATEGORY_FIGHTER, u'武闘'),
        (CATEGORY_GAMBLER, u'博徒'),
        (CATEGORY_INTERIGENCE, u'ｲﾝﾃﾘ'),
    )

    COMPOSE_CATEGORY_VIEW = (
        (VIEW_ALL, u'全部'),
        (CATEGORY_FIGHTER, u'武闘'),
        (CATEGORY_GAMBLER, u'博徒'),
        (CATEGORY_INTERIGENCE, u'ｲﾝﾃﾘ'),
        (CATEGORY_EVOLUTION, u'覚醒'),
    )
    COMPOSE_LUMP_CATEGORY_VIEW = (
        (VIEW_ALL, u'全部'),
        (CATEGORY_FIGHTER, u'武闘'),
        (CATEGORY_GAMBLER, u'博徒'),
        (CATEGORY_INTERIGENCE, u'ｲﾝﾃﾘ'),
    )

    YAKUZA_CONVERT_TYPE = (
        (0, 'デフォルト'),
        (1, 'ジェリー'),
        (2, 'プチ極技ジェリー'),
        (3, '大極技ジェリー'),
        )

    # アイテム関係のスタティック
    GAME_ITEM_RECOVER_POWER=1
    GAME_ITEM_RECOVER_LOVE=2
    GAME_ITEM_RECOVER_ONE_LOVE=44

    CATEGORY_RECOVER = 1
    CATEGORY_EQUIPMENT = 2
    CATEGORY_SKILL = 3
    CATEGORY_SNIPER = 4
    CATEGORY_EVENT = 5
    CATEGORY_SET = 6
    CATEGORY = (
        (0, u'全部'),
        (CATEGORY_RECOVER, u'回復'),
        (CATEGORY_SKILL, u'必殺技'),
        (CATEGORY_SNIPER, u'その他'),
        (CATEGORY_EVENT, u'ｲﾍﾞﾝﾄ用'),
    )
    SHOP_CATEGORY = (
        (0, u'全部'),
        (CATEGORY_RECOVER, u'回復'),
        (CATEGORY_EQUIPMENT, u'装備'),
        (CATEGORY_SKILL, u'必殺技'),
        (CATEGORY_SNIPER, u'その他'),
        (CATEGORY_EVENT, u'ｲﾍﾞﾝﾄ用'),
        (CATEGORY_SET, u'まとめ売り'),
    )

    ATTRIBUTE_USE = 1
    ATTRIBUTE_EQUIP = 2
    ATTRIBUTE_TRAP = 3
    ATTRIBUTE_NONE = 4

    #交流関係
    #極友以外への獲得ポイント
    GET_FRIEND_NOT_POINT = 2
    #極友への獲得ポイント
    GET_FRIEND_POINT = 4
    #極友へのコメントでの獲得ポイント
    GET_FRIEND_COMMENTED_POINT = 6
    #極友以外へのコメントでの獲得ポイント
    GET_FRIEND_NOT_COMMENTED_POINT = 3
    #ログインボーナスで与える極友１人あたりのポイント
    GET_FRIEND_BONUS_POINT = 50

    # 極友申請の有効時間(日)
    FRIEND_APPLICATION_LIMIT_DAY = 7
    FRIEND_APPLICATION_LIMIT_TIME = FRIEND_APPLICATION_LIMIT_DAY * 86400

    # 最大舎弟数
    DEFAULT_MAX_SHATEI_COUNT = 50

    #フレンド増えた記念の交流ポイント数
    ADD_FRIEND_COM_POINT = 300

    #フレンドさらばしたペナルティの減少ポイント数
    REMOVE_FRIEND_PENALTY_POINT = 300
    #同日に何度もさらばした時のペナルティ
    REMOVE_FRIEND_PENALTY_POINT_SECOND = 400

    #これ以上の場合はボクシングフラッシュ
    MIN_FIGHTER_BATTLE_RARITY = 3

    #これ以上の場合は合成時に警告
    COUTION_COMPOSE_RARITY = 3

    #舎弟のレア度の表記
    YAKUZA_RARITY_NONE = 0
    YAKUZA_RARITY_NORMAL = 1
    YAKUZA_RARITY_NORMAL_PLUS = 2
    YAKUZA_RARITY_RARE = 3
    YAKUZA_RARITY_RARE_PLUS = 4
    YAKUZA_RARITY_SUPER_RARE = 5
    YAKUZA_RARITY_SUPER_RARE_PLUS = 6
    YAKUZA_RARITY_GOD_RARE = 7
    YAKUZA_RARITY_GOD_RARE_PLUS = 8
    YAKUZA_RARITY_HELL_RARE = 9
    YAKUZA_RARITY_HELL_RARE_PLUS = 10
    YAKUZA_RARITY_ASURA_RARE = 11
    YAKUZA_RARITY_ASURA_RARE_PLUS = 12
    YAKUZA_RARITY_SUPER_SUPER_RARE = 13
    YAKUZA_RARITY_SUPER_SUPER_RARE_PLUS = 14

    YAKUZA_RARITY_NAMES = (
        (YAKUZA_RARITY_NONE,            u'未設定', '#FFFFFF'),
        (YAKUZA_RARITY_NORMAL,          u'ﾉｰﾏﾙ', '#FFFFFF'),
        (YAKUZA_RARITY_NORMAL_PLUS,     u'ﾉｰﾏﾙ+', '#FFFFFF'),
        (YAKUZA_RARITY_RARE,            u'ﾚｱ', '#0099FF'),
        (YAKUZA_RARITY_RARE_PLUS,       u'ﾚｱ+', '#0099FF'),
        (YAKUZA_RARITY_SUPER_RARE,      u'Sﾚｱ', '#FFCC00'),
        (YAKUZA_RARITY_SUPER_RARE_PLUS, u'Sﾚｱ+', '#FFCC00'),
        (YAKUZA_RARITY_GOD_RARE,        u'Gﾚｱ', '#bb8d31'),
        (YAKUZA_RARITY_GOD_RARE_PLUS,   u'Gﾚｱ+', '#bb8d31'),
        (YAKUZA_RARITY_HELL_RARE,       u'Hﾚｱ', '#7b7fc1'),
        (YAKUZA_RARITY_HELL_RARE_PLUS,  u'Hﾚｱ+', '#7b7fc1'),
        (YAKUZA_RARITY_ASURA_RARE,       u'Aﾚｱ', '#ff9b52'),
        (YAKUZA_RARITY_ASURA_RARE_PLUS,  u'Aﾚｱ+', '#ff9b52'),
        (YAKUZA_RARITY_SUPER_SUPER_RARE,  u'SSﾚｱ', '#ff0000'),
        (YAKUZA_RARITY_SUPER_SUPER_RARE_PLUS,  u'SSﾚｱ+', '#ff0000'),
    )

    YAKUZA_RARITY = (
        (YAKUZA_RARITY_NONE,            u'未設定'),
        (YAKUZA_RARITY_NORMAL,          u'ﾉｰﾏﾙ'),
        (YAKUZA_RARITY_NORMAL_PLUS,     u'ﾉｰﾏﾙ+'),
        (YAKUZA_RARITY_RARE,            u'ﾚｱ'),
        (YAKUZA_RARITY_RARE_PLUS,       u'ﾚｱ+'),
        (YAKUZA_RARITY_SUPER_RARE,      u'Sﾚｱ'),
        (YAKUZA_RARITY_SUPER_RARE_PLUS, u'Sﾚｱ+'),
        (YAKUZA_RARITY_GOD_RARE,        u'Gﾚｱ'),
        (YAKUZA_RARITY_GOD_RARE_PLUS,   u'Gﾚｱ+'),
        (YAKUZA_RARITY_HELL_RARE,       u'Hﾚｱ'),
        (YAKUZA_RARITY_HELL_RARE_PLUS,  u'Hﾚｱ+'),
        (YAKUZA_RARITY_ASURA_RARE,       u'Aﾚｱ'),
        (YAKUZA_RARITY_ASURA_RARE_PLUS,  u'Aﾚｱ+'),
        (YAKUZA_RARITY_SUPER_SUPER_RARE,  u'SSﾚｱ'),
        (YAKUZA_RARITY_SUPER_SUPER_RARE_PLUS,  u'SSﾚｱ+'),
    )

    YAKUZA_RARITY_VIEW = (
        (YAKUZA_RARITY_NONE,            u'全部'),
        (YAKUZA_RARITY_NORMAL,          u'ﾉｰﾏﾙ'),
        (YAKUZA_RARITY_NORMAL_PLUS,     u'ﾉｰﾏﾙ+'),
        (YAKUZA_RARITY_RARE,            u'ﾚｱ'),
        (YAKUZA_RARITY_RARE_PLUS,       u'ﾚｱ+'),
        (YAKUZA_RARITY_SUPER_RARE,      u'Sﾚｱ'),
        (YAKUZA_RARITY_SUPER_RARE_PLUS, u'Sﾚｱ+'),
        (YAKUZA_RARITY_GOD_RARE,        u'Gﾚｱ'),
        (YAKUZA_RARITY_GOD_RARE_PLUS,   u'Gﾚｱ+'),
        (YAKUZA_RARITY_HELL_RARE,       u'Hﾚｱ'),
        (YAKUZA_RARITY_HELL_RARE_PLUS,  u'Hﾚｱ+'),
        (YAKUZA_RARITY_ASURA_RARE,      u'Aﾚｱ'),
        (YAKUZA_RARITY_ASURA_RARE_PLUS, u'Aﾚｱ+'),
        (YAKUZA_RARITY_SUPER_SUPER_RARE,u'SSﾚｱ'),
        (YAKUZA_RARITY_SUPER_SUPER_RARE_PLUS,u'SSﾚｱ+'),
    )

    YAKUZA_RARITY_VIEW_DICT = dict(YAKUZA_RARITY_VIEW)

    #極女のレア度（編集用）
    GOKUJO_RARITY = (
        (0, u'未設定'),
        (1, u'★'),
        (2, u'★★'),
        (3, u'★★★'),
        (4, u'★★★★'),
        (5, u'★★★★★'),
    )

    FIRST_BASE_PLACE_ID = 1
    FIRST_PLACE_ID = 1

    LAST_BASE_PLACE_ID = 4

    SAME_CATEGORY_BONUS = 1.05

    #ひとことサービスによるインセンティブ
    TWIT_SERVICE_ADD_POINT = 10

    #プレゼントの種類
    TYPE_NONE = 0
    TYPE_CARD = 1
    TYPE_ITEM = 2
    TYPE_TREASURE = 3
    TYPE_MONEY = 4
    TYPE_POINT = 5
    TYPE_MEDAL = 6
    TYPE_SELF = 7
    TYPE_SELECT = 8
    TYPE_GOKUJOEQUIP = 9
    TYPE_YAKUZAEQUIP = 10
    TYPE = (
        (TYPE_NONE, u'未選択'),
        (TYPE_CARD, u'舎弟'),
        (TYPE_ITEM, u'ｱｲﾃﾑ'),
        (TYPE_TREASURE, u'秘宝'),
        (TYPE_MONEY, u'銭'),
        (TYPE_POINT, u'盃pt'),
        (TYPE_MEDAL, u'ﾚｱ代紋'),
        (TYPE_SELF, u'自属性'),
        (TYPE_SELECT, u'選択'),
        (TYPE_GOKUJOEQUIP, u'極女装備'),
        (TYPE_YAKUZAEQUIP, u'舎弟装備'),
    )

    # プレゼント時のフレンドリストの表示
    FRIEND_WISH = 1    # 欲しいフレンド
    FRIEND_ALL = 2    # すべてのフレンド

    # １日にプレゼントを渡せる上限
    MAX_PRESENT_GIVE = 40

    #公式ユーザーのID
    APP_USER_FRIEND_REWARD_ID = 42206379


    #公式コミュニティURL
    SNS_OFFICIAL_COMMUNITY_URL = u'http://mcom.gree.jp/community/view/2556155'
    SNS_OFFICIAL_COMMUNITY_URL_BY_SMARTPHONE = u'http://t.gree.jp/community/2556155'

    #公式コミュニティ参加ボーナス
    SNS_OFFICIAL_COMMUNITY_JOIN_BONUS_ID = 9

    #極女コンプした時のメッセージ
    GOKUJO_COMPLETE_PLACE_MESSAGE = u'<a href="%s">%s</a>が%sの極女をｺﾝﾌﾟﾘｰﾄ!'

    #秘宝コンプした時のメッセージ
    TREASURE_COMPLETE_PLACE_MESSAGE = u'<a href="%s">%s</a>が%sの秘宝ｺﾝﾌﾟﾘｰﾄ!'

    #友だち申請関連のアクティビティ文言
    FRIEND_ACCEPT_MESSAGE = u'<a href="%s">%s</a>と極友になりました'
    FRIEND_APPLICATION_MESSAGE = u'{%% emoji "smile" %%}<a href="%s">%sから極友申請!</a>{%% emoji "smile" %%}'

    #ボスを倒した時のメッセージ
    BOSS_CLEAR_MESSAGE = u'<a href="%s">%s</a>が%sのﾎﾞｽを倒しました!'

    #ボスを倒した時のみんなのアプリ更新
    BOSS_CLEAR_MESSAGE_BY_API = u'%sをﾎﾞｺﾎﾞｺにし、%s平定!'

    #無料ガチャを引いた場合のアプリ更新
    GACHA_FREE_ONEDAY_MESSAGE_BY_API = u'%sが1日1回無料ｶﾞﾁｬで舎弟極道をｹﾞｯﾄ!!'

    #ランチタイムガチャのアプリ更新
    GACHA_LUNCH_MESSAGE_BY_API = u'ﾗﾝﾁﾀｲﾑｶﾞﾁｬで舎弟ｹﾞｯﾄ!時間限定だぞ!今すぐ来い!'
    #夜ガチャのアプリ更新
    GACHA_NIGHT_MESSAGE_BY_API = u'ﾎﾟｯｷﾘｶﾞﾁｬで舎弟ｹﾞｯﾄ!時間限定だぞ!今すぐ来い!'

    #ガチャでレア以上を引いたときのアプリ更新
    GACHA_REAR_GET_MESSAGE_BY_API = u'半端ないﾚｱ極道%sｹﾞｯﾄ!お前もｹﾞｯﾄしに来い!'

    #ゲームをはじめた時のアプリ更新
    GAME_START_MESSAGE_BY_API = u'任侠の世界に入ったぞ!ともに盃をかわそうぜ'

    #極女をコンプした時のアプリ更新
    GOKUJO_COMPLETE_MESSAGE_BY_API = u'%sの極女をｺﾝﾌﾟ!伝説の女極道%sをｹﾞｯﾄ!'

    #秘宝をコンプした時のアプリ更新
    TREASURE_COMPLETE_MESSAGE_BY_API = u'%sの秘宝をｺﾝﾌﾟ!屈強なﾚｱ極道%sをｹﾞｯﾄ!'

    #秘宝をコンプした時のアプリ更新(装備)
    TREASURE_COMPLETE_MESSAGE_BY_API = u'%sの秘宝をｺﾝﾌﾟ!強力な装備%sをｹﾞｯﾄ!'

    #秘宝（こけし）をコンプした時のアプリ更新
    TREASURE_KOKESHI_COMPLETE_MESSAGE_BY_API = u'%sが%sの秘宝をｺﾝﾌﾟﾘｰﾄし､黄金に光り輝く%sをｹﾞｯﾄ!'

    #秘宝（マトリョーシカ）をコンプした時のアプリ更新
    TREASURE_MATRYOSHKA_COMPLETE_MESSAGE_BY_API = u'%sが%sの秘宝をｺﾝﾌﾟﾘｰﾄし､黄金に光り輝く%sをｹﾞｯﾄ!'

    #ログインボーナスをもらったアプリ更新
    LOGIN_BONUS_MESSAGE_BY_API = u'貢ぎ金ゲット!お前の女も金持って待ってるんじゃないか?'

    #盃をかわしたアプリ更新
    POKE_MESSAGE_BY_API = u'%sと盃を交わしました!!'

    #エリアクリアのアプリ更新
    AREA_CLEAR_MESSAGE_BY_API = u'%sをｼﾏにした!'

    #招待インセンティブのアイテムプレゼント文言
    INVITATION_PRESENT_MESSAGE = u'%sの%s人目招待成立のﾌﾟﾚｾﾞﾝﾄです。'

    #キャンペーン期間中の招待人数達成プレゼント文言
    INVITATION_INVITE_PRESENT_MESSAGE = u'たくさん誘ってくれてありがとう!招待人数達成記念のﾎﾞｰﾅｽです!'

    #招待のデフォルト文言
    #INVITATION_DEFAULT_MESSAGE = u'極道はじめませんか?毎日無料ｶﾞﾁｬの「任侠道」を一緒にﾌﾟﾚｲしよう!'
    #INVITATION_DEFAULT_MESSAGE = u'GREE Award RPG最優秀賞受賞!話題の「任侠道」を一緒にﾌﾟﾚｲしよう！'
    #INVITATION_DEFAULT_MESSAGE = u'このｹﾞｰﾑ、一緒にやりませんか♪今なら招待されたほうもﾚｱｶﾞﾁｬﾁｹがもらえるらしいよ!ﾁｭｰﾄﾘｱﾙだけでもお願いできませんか!!?'
    #INVITATION_DEFAULT_MESSAGE = u'このｹﾞｰﾑ、一緒にやりませんか♪招待でもらえる舎弟がどうしてもほしいんです!ﾁｭｰﾄﾘｱﾙだけでもお願いできませんか!!?'
    INVITATION_DEFAULT_MESSAGE = u'今､始めるとSﾚｱ舎弟が必ずもらえる!一緒にﾌﾟﾚｲしよう!!'


    #極女コンプの報酬アイテムのプレゼント文言
    GOKUJO_COMPLETE_PRESENT_MESSAGE = u'極女ｺﾝﾌﾟﾘｰﾄおめでとう!選択した極道です!'

    #秘宝コンプの報酬アイテムのプレゼント文言
    TREASURE_COMPLETE_PRESENT_MESSAGE = u'秘宝ｺﾝﾌﾟﾘｰﾄおめでとう!選択した報酬です!'

    #秘宝（こけし）コンプの報酬アイテムのプレゼント文言
    TREASURE_KOKESHI_COMPLETE_PRESENT_MESSAGE = u'秘宝ｺﾝﾌﾟﾘｰﾄおめでとう!選択したこけしです!'

    #こけしコンプの報酬アイテムのプレゼント文言
    KOKESHI_COMPLETE_PRESENT_MESSAGE = u'こけしｺﾝﾌﾟﾘｰﾄおめでとう!こけしｺﾝﾌﾟﾘｰﾄの報酬です!'

    #ヤクザ無双全国ランキング報酬アイテムのプレゼント文言
    YAKUZAMUSO_GENERAL_RANKING_PRESENT_MESSAGE = u'ﾔｸｻﾞ無双全国ﾗﾝｷﾝｸﾞ%s位おめでとう!%s位の報酬です!'

    #ヤクザ無双グループランキング報酬アイテムのプレゼント文言
    YAKUZAMUSO_GROUP_RANKING_PRESENT_MESSAGE = u'ﾔｸｻﾞ無双ｸﾞﾙｰﾌﾟﾗﾝｷﾝｸﾞ%s位おめでとう!%s位の報酬です!'

    #秘宝（マトリョーシカ）コンプの報酬アイテムのプレゼント文言
    TREASURE_MATRYOSHKA_COMPLETE_PRESENT_MESSAGE = u'秘宝ｺﾝﾌﾟﾘｰﾄおめでとう!選択したﾏﾄﾘｮｰｼｶです!'

    #マトリョーシカコンプの報酬アイテムのプレゼント文言
    MATRYOSHKA_COMPLETE_PRESENT_MESSAGE = u'ﾏﾄﾘｮｰｼｶｺﾝﾌﾟﾘｰﾄおめでとう!ﾏﾄﾘｮｰｼｶｺﾝﾌﾟﾘｰﾄの報酬です!'

    #カチコミサンデー全国ランキング報酬アイテムのプレゼント文言
    KACHIKOMI_GENERAL_RANKING_PRESENT_MESSAGE = u'%s全国ﾗﾝｷﾝｸﾞ%s位おめでとう!%s位の報酬です!'

    #カチコミサンデーグループランキング報酬アイテムのプレゼント文言
    KACHIKOMI_GROUP_RANKING_PRESENT_MESSAGE = u'%sｸﾞﾙｰﾌﾟﾗﾝｷﾝｸﾞ%s位おめでとう!%s位の報酬です!'

    #略奪されたときのメッセージAPI
    STEAL_MESSAGE_BY_API_TITLE = u'★女は貰った!'
    STEAL_MESSAGE_BY_API_BODY = u'%s「お前の%sは俺の女だ！悔しかったら奪いに来い」！'

    #盃コメントされたときのメッセージAPI
    POKE_COMMENT_MESSAGE_BY_API_TITLE = u'★コメント到着！'
    POKE_COMMENT_MESSAGE_BY_API_BODY = u'%sから盃コメントが到着！お返ししてで盃ptゲットしろ！'

    #略奪されたときのメッセージAPI
    FRIEND_APPLICATION_MESSAGE_BY_API_TITLE = u'★極友申請あり！'
    FRIEND_APPLICATION_MESSAGE_BY_API_BODY = u'%sから極友申請！極友になって盃ptをｹﾞｯﾄしろ！'

    #若頭交代
    HEAD_YAKUZA_CHANGE_MESSAGE_BY_API = u'%sを新しい若頭にした!!'

    #略奪で負けた場合
    BATTLE_LOSE_REVENGE_MESSAGE_BY_API = u'俺の女が奪われた!お前の助けが必要だ!!'

    #リベンジメッセージAPI
    BATTLE_LOSE_REVENGE_MESSAGE_BY_API_TITLE = u'★カタキを取れ！'
    BATTLE_LOSE_REVENGE_MESSAGE_BY_API_BODY = u'極友の%sがやられた！今すぐカタキを取れ！'

    #特定ユーザーとの友だちによるプレゼントメッセージ
    FRIEND_REWARD_PRESENT_TEXTS = {
                1: u'公式ﾕｰｻﾞｰと友だちになった記念のｱｲﾃﾑです｡',
                2: u'任侠道×デュエルサマナー 契りキャンペーン記念のｱｲﾃﾑです｡',
    }

    # カルタタイトル
    KARUTA_MESSAGE_BY_API_TITLE = u'袋とじ!極女ﾄﾚｶVol.18開催!!'
    KARUTA_MESSAGE_BY_API_BODY = u'ﾋﾟｰｽを集めて星野奈央・不知火ｱﾔﾒの限定待受をGET!!ﾄﾚｶptを貯めれば、大技ﾊﾆｰや鬼SRｶﾞﾁｬﾁｹなど豪華報酬もGET出来るぞ!!このﾁｬﾝｽを見逃すな!! <a href="http://mpf.gree.jp/389">'

    RAID_BATTLE_RESCUE_MESSAGE_BY_APY_TITLE = u'【協力要請】天下人3末裔発見!!'
    RAID_BATTLE_RESCUE_MESSAGE_BY_APY_BODY = u'強力な天下人3末裔を一緒に倒そう!撃破ptを使ってｲﾍﾞﾝﾄ専用ｶﾞﾁｬもできる!'

    # 舎弟のソート順
    SORT_DEFAULT = 0
    SORT_ADD_REVERSE = 1
    SORT_ATTACK_REVERSE = 2
    SORT_ATTACK = 3
    SORT_DEFENCE_REVERSE = 4
    SORT_DEFENCE = 5
    SORT_LEVEL_REVERSE = 6
    SORT_LEVEL = 7
    SORT_RARITY_REVERSE = 8
    SORT_RARITY = 9
    SORT_SKILL_REVERSE = 10
    SORT_SKILL = 11
    SORT_MONEY_REVERSE = 12
    SORT_MONEY = 13
    SORT_ATTACK_DEFENCE_DIFF_REVERSE = 10
    SORT_ATTACK_DEFENCE_DIFF = 11

    SORT = (
            (SORT_ADD_REVERSE, u'追加された順'),
            (SORT_ATTACK_REVERSE, u'攻撃高い順'),
            (SORT_ATTACK, u'攻撃低い順'),
            (SORT_DEFENCE_REVERSE, u'防御高い順'),
            (SORT_DEFENCE, u'防御低い順'),
            (SORT_LEVEL_REVERSE, u'ﾚﾍﾞﾙ高い順'),
            (SORT_LEVEL, u'ﾚﾍﾞﾙ低い順'),
            (SORT_RARITY_REVERSE, u'ﾚｱ度高い順'),
            (SORT_RARITY, u'ﾚｱ度低い順'),
            (SORT_SKILL_REVERSE, u'極技高い順'),
            (SORT_SKILL, u'極技低い順'),
    )

    SORT_COMPOSE = (
            (SORT_DEFAULT, u'おまかせ'),
            (SORT_SKILL_REVERSE, u'極技おすすめ'),
            (SORT_ADD_REVERSE, u'追加された順'),
            (SORT_ATTACK_REVERSE, u'攻撃高い順'),
            (SORT_ATTACK, u'攻撃低い順'),
            (SORT_DEFENCE_REVERSE, u'防御高い順'),
            (SORT_DEFENCE, u'防御低い順'),
            (SORT_LEVEL_REVERSE, u'ﾚﾍﾞﾙ高い順'),
            (SORT_LEVEL, u'ﾚﾍﾞﾙ低い順'),
            (SORT_RARITY_REVERSE, u'ﾚｱ度高い順'),
            (SORT_RARITY, u'ﾚｱ度低い順'),
    )

    SORT_RAID = (
            (SORT_ATTACK_REVERSE, u'攻撃重視'),
            (SORT_DEFENCE_REVERSE, u'防御重視'),
            (SORT_ATTACK_DEFENCE_DIFF_REVERSE, u'ﾊﾞﾗﾝｽ'),
    )

    SORT_SELL = (
            (SORT_DEFAULT, u'おまかせ'),
            (SORT_ADD_REVERSE, u'追加された順'),
            (SORT_ATTACK_REVERSE, u'攻撃高い順'),
            (SORT_ATTACK, u'攻撃低い順'),
            (SORT_DEFENCE_REVERSE, u'防御高い順'),
            (SORT_DEFENCE, u'防御低い順'),
            (SORT_MONEY_REVERSE, u'手切れ金高い順'),
            (SORT_MONEY, u'手切れ金低い順'),
    )

    # アイテムの効果
    EFFECT_RECOVER_POWER = 1
    EFFECT_RECOVER_LOVE = 2
    EFFECT_RECOVER_LOVE_MINIMUM = 3

    ITEM_EFFECT = (
            (EFFECT_RECOVER_POWER, u'体力回復'),
            (EFFECT_RECOVER_LOVE, u'慈愛回復'),
    )

    # 必殺技のflash選択
    SKILL_SWF_1 = 1
    SKILL_SWF_2 = 2
    SKILL_SWF_3 = 3
    SKILL_SWF_4 = 4
    SKILL_SWF_5 = 5

    SKILL_SWF = (
            (SKILL_SWF_1, u'static/swf/skill/skill_1.swf'),
            (SKILL_SWF_2, u'static/swf/skill/skill_2.swf'),
            (SKILL_SWF_3, u'static/swf/skill/skill_3.swf'),
            (SKILL_SWF_4, u'static/swf/skill/skill_4.swf'),
            (SKILL_SWF_5, u'static/swf/skill/skill_5.swf'),
    )

    # 地回り達成時に盃pt付与
    COMMUNICATION_POINT_BY_CLEAR_AREA_JIMAWARI = 50

    # 一括選択時の全選択キー
    LUMP_COMPOSE = 0
    LUMP_COMPOSE_ALL = 1

    # 道場イベントの初期エリア
    FIRST_PLACE_DOJO_ID = 249
    # 道場の最終エリア
    DOJO_LAST_AREA_ID = 298
    # 道場の最初の都市ID
    FIRST_MIDDLE_PLACE_DOJO_ID = 18
    # 道場の最後の都市ID
    LAST_MIDDLE_PLACE_DOJO_ID = 34

    # ボーナスアイテム
    BUY_BONUS_ITEM_1_5 = (1, )
    BUY_BONUS_ITEM_1_5_COUNT = (1, )

    BUY_BONUS_ITEM_1_10 = (1, 2,)
    BUY_BONUS_ITEM_1_10_COUNT = (1, 1,)

    # ボーナスアイテム配布時のプレゼント文言
    BUY_BONUS_MESSAGE = u'ｵｰﾌﾟﾆﾝｸﾞｷｬﾝﾍﾟｰﾝにつき､ｾｯﾄ購入のﾎﾞｰﾅｽです!'

    # 道場のクリアインセンティブ
    DOJO_CLEAR_INSENTIVE_1 = 12
    DOJO_CLEAR_INSENTIVE_2 = 13
    DOJO_CLEAR_INSENTIVE_3 = 14

    DOJO_CLEAR_INSENTIVE_1 = 192
    DOJO_CLEAR_INSENTIVE_2 = 193
    DOJO_CLEAR_INSENTIVE_3 = 194

    # 現在の道場のID。プログラム内部でしか使いません
    DOJO_PID = 1

    # 招待した時の盃ポイント付与量
    INVITE_COM_POINT = 50

    # 秘宝のグループ
    CATEGORY_GROUP_TREASURE = 1
    CATEGORY_GROUP_KOKESHI = 2
    CATEGORY_GROUP_MATRYOSHKA = 3
    CATEGORY_GROUP_EQUIP = 4

    CATEGORY_GROUP = (
            (CATEGORY_GROUP_TREASURE, u'秘宝'),
            (CATEGORY_GROUP_KOKESHI, u'こけし'),
            (CATEGORY_GROUP_MATRYOSHKA, u'マトリョーシカ'),
            (CATEGORY_GROUP_EQUIP, u'装備'),
    )

    # 秘宝略奪で消費される慈愛
    CONSUME_TREASURE_LOVE = 3

    #イベントカテゴリー
    EVENT_CATEGORY_DOJO = 1
    EVENT_CATEGORY_TOWER = 2
    EVENT_CATEGORY_KACHIKOMI = 3
    EVENT_CATEGORY_INVASION = 4
    EVENT_CATEGORY_CRYPTID = 5
    EVENT_CATEGORY_MUSOU = 6
    EVENT_CATEGORY_KACHIKOMI2 = 7
    EVENT_CATEGORY_SAINT = 8
    EVENT_CATEGORY_KARUTA = 9
    EVENT_CATEGORY_CABARET = 10
    EVENT_CATEGORY_STADIUM = 11
    EVENT_CATEGORY_PROMO = 12
    EVENT_CATEGORY_GOKUPRO = 13
    EVENT_CATEGORY_RAID = 14
    EVENT_CATEGORY_HAREM = 15
    EVENT_CATEGORY_GOD = 16
    EVENT_CATEGORY_GIFT = 17
    EVENT_CATEGORY_VALENTINE = 18
    EVENT_CATEGORY_ANRI_TIEUP = 19
    EVENT_CATEGORY_TREE = 20
    EVENT_CATEGORY_RECALL = 21
    EVENT_CATEGORY_ARENA = 22
    EVENT_CATEGORY_RAID_USUAL = 23
    EVENT_CATEGORY_SUGOROKU = 24
    EVENT_CATEGORY_REQUEST = 25
    EVENT_CATEGORY_SLOT = 26
    EVENT_CATEGORY_OIRAN_PETAL = 27
    EVENT_CATEGORY_RAID_DEFEAT = 28
    EVENT_CATEGORY_TRANSPORTER = 29
    EVENT_CATEGORY_GACHA = 30
    EVENT_CATEGORY_TIEUP = 31
    EVENT_CATEGORY_FESTIVAL = 32
    EVENT_CATEGORY_LIMITOVER = 33
    EVENT_CATEGORY = (
        (0, '未設定'),
        (EVENT_CATEGORY_DOJO, u'道場'),
        (EVENT_CATEGORY_TOWER, u'ヒルズ'),
        (EVENT_CATEGORY_KACHIKOMI, u'カチコミ'),
        (EVENT_CATEGORY_INVASION, u'侵攻'),
        (EVENT_CATEGORY_CRYPTID, u'無法'),
        (EVENT_CATEGORY_MUSOU, u'無双'),
        (EVENT_CATEGORY_KACHIKOMI2, u'聖域戦'),
        (EVENT_CATEGORY_SAINT, u'摩天楼'),
        (EVENT_CATEGORY_KARUTA, u'袋とじ極女トレカ'),
        (EVENT_CATEGORY_CABARET, u'ノックアウトラブ'),
        (EVENT_CATEGORY_STADIUM, u'カチスタ'),
        (EVENT_CATEGORY_PROMO, u'プロモ用イベント'),
        (EVENT_CATEGORY_GOKUPRO, u'極女をプロデュース。'),
        (EVENT_CATEGORY_RAID, u'戦国ヤクザ'),
        (EVENT_CATEGORY_HAREM, u'キノコ狩り'),
        (EVENT_CATEGORY_GOD, u'GODヤクザ'),
        (EVENT_CATEGORY_GIFT, u'ギフトキャンペーン'),
        (EVENT_CATEGORY_VALENTINE, u'バレンタインキャンペーン'),
        (EVENT_CATEGORY_RAID, u'強襲ヤクザ'),
        (EVENT_CATEGORY_ANRI_TIEUP, u'杉原杏璃タイアップ'),
        (EVENT_CATEGORY_TREE, u'ツリー'),
        (EVENT_CATEGORY_RECALL, u'呼び戻しキャンペーン'),
        (EVENT_CATEGORY_ARENA, u'闘技場'),
        (EVENT_CATEGORY_RAID_USUAL, u'強襲ヤクザ日常化'),
        (EVENT_CATEGORY_SUGOROKU, u'すごろく'),
        (EVENT_CATEGORY_REQUEST, u'リクエスト'),
        (EVENT_CATEGORY_SLOT, u'任侠スロット'),
        (EVENT_CATEGORY_OIRAN_PETAL, u'花魁'),
        (EVENT_CATEGORY_RAID_DEFEAT, u'強襲ヤクザ撃破数版'),
        (EVENT_CATEGORY_TRANSPORTER, u'トランスポーター'),
        (EVENT_CATEGORY_GACHA, u'ガチャ累積報酬キャンペーン'),
        (EVENT_CATEGORY_TIEUP, u'タイアップ'),
        (EVENT_CATEGORY_FESTIVAL, u'宴'),
        (EVENT_CATEGORY_LIMITOVER, u'レベルキャップ解放キャンペーン'),
    )

    # ゲームキャンペーン
    CAMPAIGN_CATEGORY_NONE = 0
    CAMPAIGN_CATEGORY_COMPOSE = 1
    CAMPAIGN_CATEGORY_JIMAWARI_MONEY = 2
    CAMPAIGN_CATEGORY_JIMAWARI_YAKUZA = 3
    CAMPAIGN_CATEGORY_JIMAWARI_GOKUJO = 4
    CAMPAIGN_CATEGORY_BATTLE_MONEY = 5
    CAMPAIGN_CATEGORY_JIMAWARI_ACHIEVEMENT = 6
    CAMPAIGN_CATEGORY_FRIEND_POKE = 7
    CAMPAIGN_CATEGORY_LOGINBONUS_COM = 8
    CAMPAIGN_CATEGORY_JIMAWARI_CURE = 9
    CAMPAING_CATEGORY_EVENT_LOGIN = 10
    CAMPAIGN_CATEGORY_JIMAWARI_ITEM = 11
    CAMPAIGN_CATEGORY_MILLION = 12
    CAMPAIGN_CATEGORY_BATTLE_ITEM = 14
    CAMPAIGN_CATEGORY_JIMAWARI_EXP = 15
    CAMPAIGN_CATEGORY_PRE_DRAGON_GENESIS = 16
    CAMPAIGN_CATEGORY = (
        (CAMPAIGN_CATEGORY_NONE, u'未設定'),
        (CAMPAIGN_CATEGORY_COMPOSE, u'入魂率アップ'),
        (CAMPAIGN_CATEGORY_JIMAWARI_MONEY, u'地回り獲得金アップ'),
        (CAMPAIGN_CATEGORY_JIMAWARI_YAKUZA, u'地回り舎弟獲得率アップ'),
        (CAMPAIGN_CATEGORY_JIMAWARI_GOKUJO, u'地回り極女出現率アップ'),
        (CAMPAIGN_CATEGORY_BATTLE_MONEY, u'略奪獲得金アップ'),
        (CAMPAIGN_CATEGORY_JIMAWARI_ACHIEVEMENT, u'地回り達成度アップ'),
        (CAMPAIGN_CATEGORY_FRIEND_POKE, u'極友へのコメントつき盃ポイントアップ'),
        (CAMPAIGN_CATEGORY_LOGINBONUS_COM, u'毎日ログインボーナス：盃ポイント'),
        (CAMPAIGN_CATEGORY_JIMAWARI_CURE, u'地回り体力回復ドロップ'),
        (CAMPAING_CATEGORY_EVENT_LOGIN, u'イベントログインボーナス'),
        (CAMPAIGN_CATEGORY_JIMAWARI_ITEM, u'地回りアイテムドロップ'),
        (CAMPAIGN_CATEGORY_MILLION, u'ン万人キャンペーン'),
        (CAMPAIGN_CATEGORY_BATTLE_ITEM, u'バトルキャンペーン'),
        (CAMPAIGN_CATEGORY_JIMAWARI_EXP, u'地回り経験値アップ'),
        (CAMPAIGN_CATEGORY_PRE_DRAGON_GENESIS, u'ドラジェネ事前登録'),
    )

    KACHIKOMI_SHATEI_MINIMUM_NUM = 10
    KACHIKOMI_CONSUME_POWER = 20
    KACHIKOMI_CONSUME_LOVE = 2
    KACHIKOMI_GET_EXP_BONUS = 5
    KACHIKOMI_GET_EXP = KACHIKOMI_CONSUME_POWER + KACHIKOMI_GET_EXP_BONUS

    KACHIKOMI_RANKING_GENERAL = 1
    KACHIKOMI_RANKING_GROUP = 2
    #ランキングタイプ
    RANKING_TYPE = (
        (KACHIKOMI_RANKING_GENERAL, u'全国ランキング'),
        (KACHIKOMI_RANKING_GROUP, u'グループランキング'),
    )

    KACHIKOMI_SEARCH_POINT = 1
    KACHIKOMI_SEARCH_LEVEL = 2
    #ランキングタイプ
    KACHIKOMI_SEARCH_TYPE = (
        (KACHIKOMI_SEARCH_POINT, u'ポイント'),
        (KACHIKOMI_SEARCH_LEVEL, u'レベル'),
    )

    CABARET_SEARCH_POINT = 1
    CABARET_SEARCH_LEVEL = 2
    #ランキングタイプ
    CABARET_SEARCH_TYPE = (
        (CABARET_SEARCH_POINT, u'ポイント'),
        (CABARET_SEARCH_LEVEL, u'レベル'),
    )

    KACHIKOMI_BATTLE_LIMIT = 1

    KACHIKOMI_CATEGORY_SWF_NAME = {
            CATEGORY_FIGHTER: 'bu',
            CATEGORY_GAMBLER: 'ba',
            CATEGORY_INTERIGENCE: 'in',
            }

    # 無双で助っ人を呼べる間隔（分）
    MUSOU_RENTAL_HEAD_INTERVAL = 30

    # プレゼントで渡す舎弟の種別
    PRESENT_SHATEI_TYPE_NONE = 0
    PRESENT_SHATEI_TYPE_SPECIFY = 1
    PRESENT_SHATEI_TYPE_RANDOM_RARE = 2
    PRESENT_SHATEI_TYPE_RANDOM_RARE_PLUS = 3
    PRESENT_SHATEI_TYPE_RANDOM_S_RARE = 4
    PRESENT_SHATEI_TYPE_RANDOM_S_RARE_EXCLUDE_KOKESHI = 5
    PRESENT_SHATEI_TYPE = (
        (PRESENT_SHATEI_TYPE_NONE, u'未選択'),
        (PRESENT_SHATEI_TYPE_SPECIFY, u'ID指定'),
        (PRESENT_SHATEI_TYPE_RANDOM_RARE, u'レアランダム'),
        (PRESENT_SHATEI_TYPE_RANDOM_RARE_PLUS, u'レア＋ランダム'),
        (PRESENT_SHATEI_TYPE_RANDOM_S_RARE, u'Sレアランダム'),
        (PRESENT_SHATEI_TYPE_RANDOM_S_RARE_EXCLUDE_KOKESHI, u'Sレアランダム（こけし除く）'),
    )

    # メンテナンス直前フラグ（後で別の箇所に書き直します）
    IS_JUST_BEFORE_MAINTENANCE = True

    # トレードのアクション
    TRADE_ACTION_REQUEST = 1
    TRADE_ACTION_APPROVE = 2
    TRADE_ACTION = (
            (TRADE_ACTION_REQUEST, u'依頼'),
            (TRADE_ACTION_APPROVE, u'承諾'),
    )

    # トレード依頼の期限（分で指定）
    TRADE_REQUEST_TIME_LIMIT = 30
    # トレード承諾の期限（日で指定）
    TRADE_APPROVE_TIME_LIMIT = 2

    # トレードステータス
    TRADE_STATUS_FINISH = 0 # 終了状態（論理削除状態）
    TRADE_STATUS_START  = 1 # 申請開始（FROMプレイヤーがトレード品を選んでいる
    TRADE_STATUS_APPLY  = 2 # 申請中（TOプレイヤーがトレード品を選んでいる
    TRADE_STATUS_ACCEPT = 3 # 受理中（FROMプレイヤーがトレード品を見てOKかNGを押す
    TRADE_STATUS_BIRTH  = 4 # 成立（TOプレイヤーが受け取る
    TRADE_STATUS_FINISH = 5 # 完了（TOプレイヤーが受け取った状態
    # トレードステータス（キャンセル）
    TRADE_STATUS_AUTO_CANCEL_DAY = -4 # 自動キャンセル（成立していないのに期日がきてしまった）
    TRADE_STATUS_TO_CANCEL = -3   # TOからのキャンセル（FROMはアイテムを受け取らなければならない）
    TRADE_STATUS_FROM_CANCEL = -2 # FROMからのキャンセル（TOはアイテムを受け取らなければならない）
    TRADE_STATUS_AUTO_CANCEL_TIME = -1 # 自動キャンセル（成立していないのに期日がきてしまった）
    TRADE_STATUS = (
        (TRADE_STATUS_FINISH, u'終了状態'),
        (TRADE_STATUS_START, u'申請開始'),
        (TRADE_STATUS_APPLY, u'申請中'),
        (TRADE_STATUS_ACCEPT, u'受理中'),
        (TRADE_STATUS_BIRTH, u'成立'),
        (TRADE_STATUS_FINISH, u'完了'),
        (TRADE_STATUS_TO_CANCEL, u'TOからのｷｬﾝｾﾙ'),
        (TRADE_STATUS_FROM_CANCEL, u'FROMからのｷｬﾝｾﾙ'),
        (TRADE_STATUS_AUTO_CANCEL_TIME, u'30分自動ｷｬﾝｾﾙ'),
        (TRADE_STATUS_AUTO_CANCEL_DAY, u'48時間自動ｷｬﾝｾﾙ'),
    )

    # トレードエントリーの最大数
    TRADE_ENTRY_MAX = 5

    # トレードの一言コメントの最大文字数
    TRADE_MAX_LENGTH = 60

    # トレード関連のアクティビティ文言
    TRADE_APPLY_MESSAGE = u'<a href="%s">%sから取引申請が来ています!</a>'
    TRADE_ACCEPT_MESSAGE = u'<a href="%s">%sから取引の返事がきました!</a>'
    TRADE_BIRTH_MESSAGE = u'<a href="%s">%sとの取引が成立しました!</a>'
    TRADE_CANCEL_MESSAGE = u'<a href="%s">%sとの取引がｷｬﾝｾﾙされました</a>'
    TRADE_TIMECANCEL_MESSAGE = u'<a href="%s">%sとのﾄﾚｰﾄﾞがｷｬﾝｾﾙされました</a>'
    TRADE_DAYCANCEL_MESSAGE = u'<a href="%s">%sとのﾄﾚｰﾄﾞがｷｬﾝｾﾙされました</a>'

    # カチコミポイントのポイント(デフォルト)
    KACHIKOMI_POINT_DEFAULT = 1000
    # 勝敗によって貰えるパーセント
    KACHIKOMI_POINT_COEFFICIENT = 10
    KACHIKOMI_MIN_DEFFERENCE_IN_LEVEL = -5
    KACHIKOMI_MAX_DEFFERENCE_IN_LEVEL = 5
    KACHIKOMI_DEFFENSIVE_COEFFICIENT = 1
    KACHIKOMI_TENCHU_COEFFICIENT = 5
    KACHIKOMI_ATTACK_BONUS = 50

    # 第1回のカチコミサンデーイベントID
    KACHIKOMI_FIRST_EVENT_ID = 5

    # 通常エリアでこれ以上は進めないお！
    NOT_NORMAL_ROUTE_MOVING = False

    KACHIKOMI_POINT_RANKS = (
        (0, 10000),
        (10000, 20000),
        (20000, 30000),
        (30000, 40000),
        (40000, 50000),
        (50000, 60000),
        (60000, 70000),
        (70000, 80000),
        (80000, 90000),
        (90000, 999999),
    )

    CABARET_POINT_RANKS = (
        (0, 20),
        (20, 40),
        (40, 60),
        (60, 80),
        (80, 100),
        (100, 120),
        (120, 140),
        (140, 160),
        (160, 180),
        (180, 200),
        (200, 300),
        (300, 400),
        (400, 999),
    )

    # スキル対象属性
    SKILL_TARGET_FIGHTER = 1
    SKILL_TARGET_GAMBLER = 2
    SKILL_TARGET_INTERIGENCE = 3
    SKILL_TARGET_FIGHTER_GAMBLER = 4
    SKILL_TARGET_FIGHTER_INTERIGENCE = 5
    SKILL_TARGET_GAMBLER_INTERIGENCE = 6
    SKILL_TARGET_CATEGORY = (
        (0, '未設定'),
        (SKILL_TARGET_FIGHTER, '武闘'),
        (SKILL_TARGET_GAMBLER, '博徒'),
        (SKILL_TARGET_INTERIGENCE, 'ｲﾝﾃﾘ'),
        (SKILL_TARGET_FIGHTER_GAMBLER, '武闘&博徒'),
        (SKILL_TARGET_FIGHTER_INTERIGENCE, '武闘&ｲﾝﾃﾘ'),
        (SKILL_TARGET_GAMBLER_INTERIGENCE, '博徒&ｲﾝﾃﾘ'),
        )

    # スキル対象属性（とりあえず、現状は極女装備でしか機能してない）
    SKILL_TARGET_SEX_MALE = 1
    SKILL_TARGET_SEX_FEMALE = 2
    SKILL_TARGET_SEX_OGRE = 3
    SKILL_TARGET_SEX_MALE_FEMALE = 4
    SKILL_TARGET_SEX_MALE_OGRE = 5
    SKILL_TARGET_SEX_FEMALE_OGRE = 6
    SKILL_TARGET_SEX = (
        (0, '未設定'),
        (SKILL_TARGET_SEX_MALE, '男'),
        (SKILL_TARGET_SEX_FEMALE, '女'),
        (SKILL_TARGET_SEX_OGRE, '鬼'),
        (SKILL_TARGET_SEX_MALE_FEMALE, '男&女'),
        (SKILL_TARGET_SEX_MALE_OGRE, '男&鬼'),
        (SKILL_TARGET_SEX_FEMALE_OGRE, '女&鬼'),
        )

    # スキル属性→通常の属性リスト変換辞書
    SKILL_CATEGORY_CONV_LIST = {
        SKILL_TARGET_FIGHTER:[CATEGORY_FIGHTER],
        SKILL_TARGET_GAMBLER:[CATEGORY_GAMBLER],
        SKILL_TARGET_INTERIGENCE:[CATEGORY_INTERIGENCE],
        SKILL_TARGET_FIGHTER_GAMBLER:[CATEGORY_FIGHTER, CATEGORY_GAMBLER],
        SKILL_TARGET_FIGHTER_INTERIGENCE:[CATEGORY_FIGHTER, CATEGORY_INTERIGENCE],
        SKILL_TARGET_GAMBLER_INTERIGENCE:[CATEGORY_GAMBLER, CATEGORY_INTERIGENCE],
        }

    # スキル対象舎弟
    SKILL_TARGET_SHATEI_PLAYER = 1
    SKILL_TARGET_SHATEI_ENEMY = 2
    SKILL_TARGET_SHATEI_SELF = 3
    SKILL_TARGET_SHATEI_MIRROR = 4
    SKILL_TARGET_SHATEI = (
        (0, '未設定'),
        (SKILL_TARGET_SHATEI_PLAYER, u'プレイヤー全体'),
        (SKILL_TARGET_SHATEI_ENEMY, u'敵全体'),
        (SKILL_TARGET_SHATEI_SELF, u'使用者単体'),
        (SKILL_TARGET_SHATEI_MIRROR, u'対面相手'),
        )

    # スキル対象パラメータ
    SKILL_TARGET_PARAM_ATTACK = 1
    SKILL_TARGET_PARAM_DEFENCE = 2
    SKILL_TARGET_PARAM_ALL = 3
    SKILL_TARGET_PARAM_MONEY = 4
    SKILL_TARGET_PARAM_ATTACK_SOLID = 5
    SKILL_TARGET_PARAM_DEFENCE_SOLID = 6
    SKILL_TARGET_PARAM_ALL_SOLID = 7
    SKILL_TARGET_PARAM_MONEY_SOLID = 8
    SKILL_TARGET_PARAM = (
        (0, '未設定'),
        (SKILL_TARGET_PARAM_ATTACK, u'攻撃力'),
        (SKILL_TARGET_PARAM_DEFENCE, u'防御力'),
        (SKILL_TARGET_PARAM_ALL, u'攻撃力&防御力'),
        (SKILL_TARGET_PARAM_MONEY, u'勝利時の銭'),
        (SKILL_TARGET_PARAM_ATTACK_SOLID, u'攻撃力(固定値)'),
        (SKILL_TARGET_PARAM_DEFENCE_SOLID, u'防御力(固定値)'),
        (SKILL_TARGET_PARAM_ALL_SOLID, u'攻撃力&防御力(固定値)'),
        (SKILL_TARGET_PARAM_MONEY_SOLID, u'勝利時の銭(固定値)'),
        )

    # UPDOWN
    SKILL_UPDOWN_UP = 1
    SKILL_UPDOWN_DOWN = 2
    SKILL_UPDOWN = (
        (0, '未設定'),
        (SKILL_UPDOWN_UP, u'上昇'),
        (SKILL_UPDOWN_DOWN, u'下降'),
        )

    # 新参者歓迎キャンペーン(2000盃pt,葉巻2個、マムシ2個)
    ROOKIE_LOGIN_BOUNUS_ITEMS = (
        (TYPE_POINT, 2000, 1),
        (TYPE_ITEM, 1, 2),
        (TYPE_ITEM, 2, 2),
    )
    ROOKIE_ADDON_PRESENT_MESSAGE = u'新参者歓迎ｷｬﾝﾍﾟｰﾝのﾛｸﾞｲﾝﾎﾞｰﾅｽです!'

    # 復帰おめでとうキャンペーン(ガチャチケ,葉巻2個、マムシ2個)
    COMEBACK_LOGIN_BONUS_ITEMS = (
        (TYPE_ITEM, 36, 1),
        (TYPE_ITEM, 1, 2),
        (TYPE_ITEM, 2, 2),
    )
    COMEBACK_ADDON_PRESENT_MESSAGE = u'復帰おめでとうｷｬﾝﾍﾟｰﾝのﾛｸﾞｲﾝﾎﾞｰﾅｽです!'

    # 初心者キャンペーンの獲得値の倍率
    ROOKIE_COMPETITIVE = 2

    # 入魂率上昇中の獲得値の倍率
    RISE_COMPETITIVE = 1.5

    # 龍巫女ID
    MIKO_ID = 288

    # SR進化巫女ID
    SR_MIKO_ID = 927

    # GR進化巫女ID
    GR_MIKO_ID = 1736

    # HR進化巫女ID
    HR_MIKO_ID = 1768

    # SSR進化巫女ID
    SSR_MIKO_ID = 2688

    # プチ進化ハニーID
    PETIT_HONEY_ID = 2812

    # プチ進化ハニー+ID
    PETIT_PLUS_HONEY_ID = 2813

    # プチ進化ハニー(SR)ID
    PETIT_SR_HONEY_ID = 2834

    # プチ進化ハニー(SR)+ID
    PETIT_SR_PLUS_HONEY_ID = 2835

    # プチ進化ハニー(GR)ID
    PETIT_GR_HONEY_ID = 2830

    # プチ進化ハニー(GR)+ID
    PETIT_GR_PLUS_HONEY_ID = 2831

    # プチ進化ハニー(HR)ID
    PETIT_HR_HONEY_ID = 2832

    # プチ進化ハニー(HR)+ID
    PETIT_HR_PLUS_HONEY_ID = 2833

    # プチ進化ハニー(AR)ID
    PETIT_AR_HONEY_ID = 2836

    # プチ進化ハニー(AR)+ID
    PETIT_AR_PLUS_HONEY_ID = 2837

    # プチ進化ハニー(SSR)ID
    PETIT_SSR_HONEY_ID = 2828

    # プチ進化ハニー(SSR)+ID
    PETIT_SSR_PLUS_HONEY_ID = 2829

    # 特技吸うハニーID
    DRAIN_HONEY_ID = 3596

    # 特技吸ったハニーID
    DRAIN_RETURN_HONEY_ID = 3598
    
    

    # ゴールド10連ガチャの景品リスト
    GACHA_GOLD_ITEM_LIST = (
        (TYPE_ITEM, 1, 2),
        (TYPE_ITEM, 2, 1),
        (TYPE_ITEM, 14, 1),
        (TYPE_CARD, 225, 1),
        (TYPE_CARD, 226, 1),
        (TYPE_CARD, 227, 1),
        (TYPE_CARD, 191, 1),
        (TYPE_POINT, 3000, 1),
    )

    # 5000円ガチャの景品リスト
    GACHA_5000GOLD_ITEM_LIST = (
        (TYPE_ITEM, 1, 2),
        (TYPE_ITEM, 2, 1),
        (TYPE_ITEM, 14, 1),
        (TYPE_ITEM, 31, 1),
        (TYPE_CARD, 188, 1),
        (TYPE_CARD, 189, 1),
        (TYPE_CARD, 190, 1),
        (TYPE_CARD, 307, 1),
        (TYPE_POINT, 3000, 1),
        (TYPE_MEDAL, 3, 1),
    )

    # 福袋のプレゼントメッセージ
    LUCKY_BAG_PRESENT_MESSAGE = u'%sの中身です。'

    # スマートフォン限定ガチャの景品極道
    GACHA_SMARTPHONE_ITEM_LIST = (
        (TYPE_CARD, 705, 1),
        (TYPE_CARD, 706, 1),
        (TYPE_CARD, 707, 1),
    )

    # 富裕層ガチャのメッセージ
    RICH_GACHA_MESSAGE = u'%sの中身です。'
    # 富裕層ガチャ 3000円の景品リスト
    RICH_GACHA_3000_ITEM_LIST = (
        (TYPE_CARD, 598, 1),  # 小技ハニー
        (TYPE_MONEY, 500000, 1),    # 50万銭
    )


    # 富裕層ガチャ 5000円の景品リスト
    RICH_GACHA_5000_ITEM_LIST = (
        (TYPE_ITEM, 1, 2),
        (TYPE_ITEM, 2, 2),
        (TYPE_ITEM, 14, 2),
        (TYPE_ITEM, 31, 1),     # レア＋ガチャチケット
        (TYPE_CARD, 188, 1),
        (TYPE_CARD, 189, 1),
        (TYPE_CARD, 190, 1),
        (TYPE_CARD, 191, 1),
        (TYPE_POINT, 3000, 1),
        (TYPE_MEDAL, 3, 1),
    )

    # 富裕層ガチャ 10000円の景品リスト
    RICH_GACHA_10000_ITEM_LIST = (
        (TYPE_CARD, 599, 1),  # 小技ハニー
        (TYPE_MONEY, 1000000, 1),    # 50万銭
        (TYPE_ITEM, 1, 10),   # 葉巻10
    )

    # 今月はいつ？
    #NOW_MONTH = datetime.date.today().month
    #NOW_MONTH = 6
    NOW_MONTH = 7 if datetime.datetime.today().hour < 15 and datetime.datetime.today().day <= 1 else 8

    # ガチャチケットID
    GACHA_TICKET_ID = 28
    GACHA_TICKET_PLUS_ID = 30
    GACHA_SROT_TICKET_ID = 52

    GACHA_TICKET_SEIRYU = 386
    GACHA_TICKET_SUZAKU = 385
    GACHA_TICKET_GENBU = 400
    GACHA_TICKET_BYAKKO = 399

    GACHA_SEIRYU = 610
    GACHA_SUZAKU = 645
    GACHA_GENBU = 668
    GACHA_BYAKKO = 626

    # ダブルガチャのプレゼントメッセージ
    DOUBLE_GACHA_PRESENT_MESSAGE = u'ﾀﾞﾌﾞﾙｶﾞﾁｬの2枚目の舎弟です。'

    # ハニーガチャのプレゼントメッセージ
    GACHA_HONEY_PRESENT_MESSAGE = u'%sででた舎弟です!'

    # ハニーガチャのみんなのアプリ更新メッセージ
    GACHA_HONEY_ACTIVITY_MESSAGE = u'GREE Award 2011 RPG最優秀賞受賞記念ﾊﾆｰｶﾞﾁｬをまわしたよ!!'

    RETRY_GACHA_PRESENT_MESSAGE = u'巻き戻しｶﾞﾁｬで出た舎弟です。'

    # フィーバーガチャのプレゼントメッセージ
    FEVER_GACHA_PRESENT_MESSAGE = u'ﾌｨｰﾊﾞｰｶﾞﾁｬで出た舎弟です。'

    # 次公開予定の場所
    NEXT_BASE_PLACE_NAME = u'鹿児島'

    # メダルの文言
    WORDS_MEDAL = u"ﾚｱ代紋"

    # メダルレート
    RARE = 3
    RARE_PLUS = 4
    S_RARE = 5
    S_RARE_PLUS = 6
    G_RARE = 7
    G_RARE_PLUS = 8
    H_RARE = 9
    H_RARE_PLUS = 10
    MEDAL_RATE = {
        RARE        : 1,
        RARE_PLUS   : 5,
        S_RARE      : 10,
        S_RARE_PLUS : 20,
        G_RARE      : 10,
        G_RARE_PLUS : 20,
        H_RARE      : 10,
        H_RARE_PLUS : 20,
    }

    # レアミキサーのマスタID
    MEDAL_RARE_MIXER_ID = 50
    MEDAL_RARE_MIXER_EXCHANGE_NUM = 20

    # SレアミキサーのマスタID
    MEDAL_SRARE_MIXER_ID = 51
    MEDAL_SRARE_MIXER_EXCHANGE_NUM = 50

    # 攻撃・防御特化ミキサー
    MEDAL_EQUIPMENT_MIXER = 41
    MEDAL_EQUIPMENT_MIXER_ATTACK_ID = 52
    MEDAL_EQUIPMENT_MIXER_DEFENSE_ID = 53
    MEDAL_EQUIPMENT_MIXER_IDS = [
        MEDAL_EQUIPMENT_MIXER_ATTACK_ID,
        MEDAL_EQUIPMENT_MIXER_DEFENSE_ID,
        MEDAL_EQUIPMENT_MIXER,
    ]

    MEDAL_EQUIPMENT_ITEMS = {
        MEDAL_EQUIPMENT_MIXER:(
            (TYPE_YAKUZAEQUIP, (44, ), 1, 600),
            (TYPE_YAKUZAEQUIP, (45, ), 1, 600),
            (TYPE_YAKUZAEQUIP, (50, ), 1, 1300),
            (TYPE_YAKUZAEQUIP, (67, ), 1, 1100),
            (TYPE_YAKUZAEQUIP, (66, ), 1, 1100),
            (TYPE_YAKUZAEQUIP, (65, ), 1, 1100),
            (TYPE_YAKUZAEQUIP, (70, ), 1, 1000),
            (TYPE_YAKUZAEQUIP, (69, ), 1, 1000),
            (TYPE_YAKUZAEQUIP, (68, ), 1, 1000),
            (TYPE_YAKUZAEQUIP, (103, ), 1, 100),
            (TYPE_YAKUZAEQUIP, (102, ), 1, 100),
            (TYPE_YAKUZAEQUIP, (98, ), 1, 500),
            (TYPE_YAKUZAEQUIP, (97, ), 1, 500),
        ),
        MEDAL_EQUIPMENT_MIXER_ATTACK_ID:(
            (TYPE_YAKUZAEQUIP, (64, ), 1, 2000),
            (TYPE_YAKUZAEQUIP, (71, ), 1, 2000),
            (TYPE_YAKUZAEQUIP, (87, ), 1, 2000),
            (TYPE_YAKUZAEQUIP, (97, ), 1, 2000),
            (TYPE_YAKUZAEQUIP, (89, ), 1, 1300),
            (TYPE_YAKUZAEQUIP, (100, ), 1, 500),
            (TYPE_YAKUZAEQUIP, (85, ), 1, 100),
            (TYPE_YAKUZAEQUIP, (91, ), 1, 50),
            (TYPE_YAKUZAEQUIP, (102, ), 1, 50),
        ),
        MEDAL_EQUIPMENT_MIXER_DEFENSE_ID:(
            (TYPE_YAKUZAEQUIP, (93, ), 1, 4000),
            (TYPE_YAKUZAEQUIP, (88, ), 1, 2000),
            (TYPE_YAKUZAEQUIP, (98, ), 1, 2000),
            (TYPE_YAKUZAEQUIP, (90, ), 1, 1300),
            (TYPE_YAKUZAEQUIP, (101, ), 1, 500),
            (TYPE_YAKUZAEQUIP, (86, ), 1, 100),
            (TYPE_YAKUZAEQUIP, (92, ), 1, 50),
            (TYPE_YAKUZAEQUIP, (103, ), 1, 50),
        )
    }

    # メダルの特殊効果種類
    MEDAL_EXCHANGE_EFFECT_RECOVER_LOVE = 1
    MEDAL_EXCHANGE_EFFECT_VIPMODE_MINI = 2
    MEDAL_EXCHANGE_EFFECT_EVENT_MODULE = 3
    MEDAL_EXCHANGE_EFFECT_RARE_MIXER = 4

    MEDAL_EXCHANGE_EFFECTS = (
            ( MEDAL_EXCHANGE_EFFECT_RECOVER_LOVE, u'慈愛回復' ),
            ( MEDAL_EXCHANGE_EFFECT_VIPMODE_MINI, u'VIPモードミニ' ),
            ( MEDAL_EXCHANGE_EFFECT_EVENT_MODULE, u'イベント用特別品' ),
            ( MEDAL_EXCHANGE_EFFECT_RARE_MIXER, u'レアミキサー' ),
    )

    # レアリティのカテゴリー用ビュー
    SORT_RARITY_MEDAL = (
            (RARE,u'ﾚｱ'),
            (RARE_PLUS,u'ﾚｱ+'),
            (S_RARE,u'Sﾚｱ'),
            (S_RARE_PLUS,u'Sﾚｱ+'),
            (H_RARE, u'Hﾚｱ'),
            (H_RARE_PLUS,u'Hﾚｱ+'),
            (G_RARE, u'Gﾚｱ'),
            (G_RARE_PLUS,u'Gﾚｱ+'),
    )

    # スキルの最大レベル
    MAX_SKILL_LEVEL = 20

    # 装備品解除アイテムID
    ITEM_EQUIPMENT_REMOVER_ID = 19
    # 事務所拡張アイテムID
    ITEM_OFFICE_EXTEND_ID = (35, 58)

    # 入魂経験値上昇中か？
    IS_RISE_COMPOSE_VALUE = False

    #　交換文言
    CHANGE_ITEM_PRESENT_MESSAGE = u'[交換]%sと交換。'

    # 事務所拡張する数
    EXTEND_MAX_SHATEI = 5

    # アカウント停止ユーザー
    ACCOUNT_BAN_LIST_NEVER = [1192258,1760525,1987107,2789258,3516051,5013273,5174093,5833410,6356120,6869137,7272985,7925851,8253078,8594200,9887898,10792422,13909527,13963378,14906345,15152682,16171961,16401790,19200035,19391887,19578266,21785449,25912836,26865431,27104288,28036302,28309792,28729203,28838886,29418205,29635597,29703105,29703105,30175560,30473558,31892184,32511517,32998736,33165035,33424201,33550366,33618855,36760664,36812606,37092932,37169147,37244365,37245675,38268856,38458737,38899129,39017860,39168986,39227944,39777571,40050281,40079686,41101395,42030998,42225771,42264972,42389595,42495122,42532755,42629466,43126822,43503310,43521119,43582121,43725185,43868454,44384633,44699260,44861681,45144952,45249947,45478873,45498674,45500452,45518679]
    #ACCOUNT_BAN_LIST_TEMP = [46251501,17695695,37476946,15145464,39117797,9775761,43334311,8642100,40986745,44245398,17530012,34928081,25251431,39582714,34231240,39555222,7422469,16485364,6541040,14624894,22411962,40034323,32465232,28897392,17584551,42099004,41140151,22815968,8431104,9368205,6578922,16914841,27243141,44586319,6957862,5474452,42614805,14367371,39595162,9075017,5553762,11807257,2496071,19269308,42903281,43007178,25868437,35362666,23214480,25540766,17797026,6890852,16067372,43103474,2929836,9747202,15170804,25959397,37081161,39108594,36808837,21345027,22532786,34824768,41462382,38139260,14066839,45436424,9116792,25153216,44824875,20216566,17716845,45888633,30111623,14887522,45932018,9397965,45806445,26465283,17850993,33310443,15968798,16723329,27486042,12641575,34972235,19891026,45905637,35853992,19679798,45903959,9591707,9638276,7957183,25269684,7245364,27462534,11794174,42146482,41558880,2241514,21586465,39792717,37870895,2663773,17781239,25815107,34862911,20224813,10584605,45920476,33290366,1261967,44123991,5830257,12692525,44716363,12925589,42644241,45423399,31468913,44391481,25995266,42560379,46165969,45637741,41661834,44743876,40239853,30045035,21934508,10349302,43971508,33908703,5071919,8454783,28449497,39489369,45919153,45137849,25393937,38211149,46056798,956035,16930839,10255170,26083141,31439068,7513723,16312886,44977198,7245089,39265473,28760367,10587540,22254183,33341699,45041824,35788467,1960252,44746274,8739031,4786737,43118565,40094922,44193317,45976518,43584120,29783870,45963397,42153993,2535314,39226442,21720258,19056853,6976943,45822771,25183245,29512081,43633015,19601604,32353658,44272231,45935822,18930625,16966151,38967441,5269316,44023282,24520380,35323089,9603425,25249884,37330369,9929206,11602071,7344204,33169497,10320834,19871769,7927103,44494728,14144902,23748127,26236530,23648426,34448200,15948460,27924494,38718000,14996143,12746198,11881653,20947026,45708448,14173284,35463177,12520137,14432462,12409685,43208851,20947025,27355348,43090431,45054060,20308522,46035152,45012188,1881658,5920592,16147133,19978720,23008673,44018338,19898891,30824036,44911829,20817593,41654772,9523779,41955567,20449374,14535436,39596437,42339017,36906095,17663239,43266202,3363967,12995332,13150133,18067126,34183056,45573122,24894006,6340442,42441060,42844893,16559149,21478074,12482223,34987232,45853600,35873458,44806006,25903377,40762058,8068203,19460892,46122674,9408951,27494677,6113755,29627051,9498848,15581453,29951543,43849567,4963792,12509719,15313016,17388832,15095927,13452669,37877369,42390652,24488269,42763477,6939037,43917664,37953715,44595007,43146558,40162362,27402140,28237854,41454281,42811963,41024720,34662657,15737084,42741862,25188797,26665054,43657185,45444650,16024483,43815209,26364350,31423144,41773315,44645361,41076971,27810056,4971156,19973717,45126057,38123983,10515253,38542142,27876245,26189535,34242689,29136956,31424147,30496050,28667734,30353534,26683373,21419726,43720035,35290750,33787431,45615743,45258091,40951836,30260567,36817801,45527190,44402262,10468774,38601758,25021396,41937495,8077893,45857289,44192052,45049388,10178348,8875599,6555642,45818789,7328251,18807746,37987005,30620766,42285291,18669718,41954889,24690086,14753933,12317705,41197183,41119024,41420370,45870836,8190504,25589435,3982477,43392596,41932875,6305398,9524388,38511541,16313491,30674044,43918176,26545233,33418842,42988775,5187248,18671982,9389381,45493177,23681601,38313497,26729887,33516533,13982615,44362796,46089863,9415657,4186785,4534712,44866554,45958444,35038555,42166113,32821799,18214930,43378540,11400644,45637515,8630502,43309052,31338622,11899726,32093635,16396284,23156924,1449997,6612647,44646839,46088014,23456419,36987075,23959441,11325449,45503080,43679536,22060234,45686198,44259298,39003442,11504632,37902451,46046690,11138894,14621256,38472003,20338066,15094168,9413367,43002720,33576918,40897198,41621082,35689519,18974612,25573281,17473637,14402307,23508613,37940625,43803097,16965993,32610453,42568447,35569202,44193754,26771074,17432542,44698994,25152586,32646523,43691482,38814767,32290000,41457688,25672812,19453251,24457895,25580978,3161783,37741493,27739864,13044701,36208476,43672573,4240633,10129335,37744089,15125652,44128602,35615363,30599605,7027082,32160802,44538722,2992835,8881237,29795132,34439896,19369354,13196460,36822835,8799944,12673310,31228144,3969174,43054971,41699304,29392395,25751405,35030164,40011067,45953067,7173521,39473136,43854988,4181060,30918045,45390485,42425697,11482573,23473178,20417292,38945674,12317385,7575450,44196314,32384965,5283033,16118115,9700730,30497788,12372383,45790006,8010394,10007588,37236835,13860215,37333744,3488033,44238418,24101270,2560453,24680073,16094405,43476218,3562475,45377954,43154106,16978562,42753093,18606838,40918422,29578310,16069773,36655370,17809075,21015049,19790693,26099589,9318468,41022618,42983704,31415507,28419519,43402108,46091115,32213668,44800180,23719278,23469078,8678778,44746107,34561325,18992648,42353195,30364399,23862274,40591648,19231775,34010448,18830493,43327358,8229162,9340669,45116501,36078094,30474516,42814038,4016050,34939946,30091847,43629810,18062412,43714755,12402325,2332307,42436951,33452109,11225592,9396208,18125436,11624333,43047986,17023245,44119354,24603979,21515620,44254427,45840725,39663329,42349945,14428370,36882977,37122115,13590412,16748799,45433016,6513328,13136930,27299949,8786217,21884551,26537337,43744529,45065334,13402302,44711173,18850865,42660136,20366965,17998107,23047489,26284283,5513526,32142164,7895136,7290265,43563770,43409895,37243227,45716958,31882591,9014843,37255646,31564720,43030393,19653644,32093418,45923587,10431069,6388001,7444679,20182978,33556912,40612976,12448343,19501302,1641666,13356537,46115909,42515092,20562078,7583813,17809846,17199790,4092810,43116955,41012870,36982192,6452260,44816188,2188174,1661534,10190318,43563450,42691503,6489739,41962864,28933782,8753148,40910617,45386970,45132020,26024831,22864601,14314716,22948184,32076628,38280345,27096377,27844658,19809926,18578666,41435941,6521436,14506558,8460285,18774473,8245055,9161382,14705141,39486642,13855527,1220706,32767321,34440760,11181250,6120897,25572087,16026216,6229217,316495,13893978,6724710,28646751,40415866,22098520,17543883,25498503,28093136,27176217,41157507,7698325,20221190,29182600,15731145,4110897,40790572,18833338,8743359,17639161,8863295,12932614,19742931,24305748,40903040,43109767,34727660,15062829,17731385,7665785,22231346,21014276,43895565,13073334,45539737,30839299,16273846,43748360,33310998,16957478,46198192,22154237,8630144,15450050,14441885,16691435,7798749,36677123,2332439,43000808,25929948,9163001,4085707,39374059,37173973,28496295,3168049,36979424,44576823,45396132,44063455,3322729,35553835,20332389,43593149,24164869,13284965,23461092,39550220,16569000,42535128,4385920,22841242,13656586,39446100,23890876,20203427,41199901,44215587,40433951,16632534,12469861,11772207,30823649,23420175,21574501,43598522,34381798,43288656,44629138,23280007,21132106,5457250,15169356,17675719,45860119,30694778,18681513,46007654,24494669,19871543,16114901,2566522,1824994,38408000,31444966,44460948]
    #ACCOUNT_BAN_LIST_GACHA25 = [11427669,45427866,1680032,45427767,20705060,43576937,25498503,37972709,46922030,42888884,7069261,44746274,27212331,24963788,17241018,41246913,20048175,2228958,20898186,18213765,14279113,17472314,27117082,38244106,10446879,14136095,19617223,42915758,8409011,39580447,26665054,8054365,42878718,23671298,14328694,18995027,42777456,31003193,43826110,47506936,37792272,34231240,48223254,15346135,22094927,13970180,32073931,5407648,46194151,30332479,3514325,15705423,37713083,22602384,18090882,22257022,23111530,9329862,30188513,13426851,8535953,3705666,16629406,35582599,15581453,33004589,40325339,9549381,29975339,41249955,47917834,8352952,31295656,40939932,6947327,46536112,19394972,20785690,46634224,33226850,42752740,21053941,23880215,45931086,15977701,45589490,3200754,17204120,2362157,19973717,10158553,17388832,35932255,5271131,26716729,31526601,42998874,46994564,25944449,48182610,7720377,47613486,24707690,46138057,6452184,44816420,5352373,11499665,34507738,40816942,4550149,34130760,8829317,25014211,16591230,32645586,41471206,23612199,7471027,13122426,30822487,6745966,18681804,32689306,17373234,26669520,43027651,21897181,37667569,28024754,31359253,35674065,8017482,41435941,47813753,19752448,25722782,45150812,19229630,1661534,18197073,29371011,39179980,43866091,44525478,46038936]
    # 18794010 のユーザーは禁止されていたが復帰させた

    ACCOUNT_BAN_LIST = ACCOUNT_BAN_LIST_NEVER

    #任侠→海賊インセンティブ関連
    KAIZOKU_APPLICATION_ID = 2440
    GOKUDO_HONBAN_APP_ID = 389
    WRITE_INCENTIVE_LOG_URL = 'http://incentive.gu3.jp/m/incentive/write/inflowlog/%s/%s/%s/%s/'
    KAIZOKU_REGIST_URL = 'http://mpf.gree.jp/%s/' + str(KAIZOKU_APPLICATION_ID)
    GET_INCENTIVE_LOG_URL = 'http://incentive.gu3.jp/m/incentive/get/inflowlog/%s/%s/%s/%s/'
    GET_REWARD_LOG_URL = 'http://incentive.gu3.jp/m/incentive/get/inflowincentivelog/%s/%s/'
    GET_REWARD_LOG_ALL_URL = 'http://incentive.gu3.jp/m/incentive/get/inflowincentivelog/all/%s/%s/'
    UPDATE_REWARD_RECEIVED = 'http://incentive.gu3.jp/m/incentive/update/inflowincentivelog/received/%s/%s/'
    GET_INFLOW_INCENTIVE_LOG_ALL = u'/get/inflowincentivelog/all/%s/%s/'

    API_PASSWORD = 'r6xf9rc6'
    KAIZOKU_INVITE_ACCEPT_FEED_MESSAGE_BY_API = u'%sが海賊道に登録したよ！'
    KAIZOKU_INVITE_ACCEPT_FEED_MESSAGE = u'%sが<a href="http://mpf.gree.jp/2440">海賊道</a>に登録したよ！'
    KAIZOKU_RECEIVE_PRIZE_FEED_MESSAGE_BY_API = u'%sが仲間を海賊道に招待！%sを無料でGETした！'
    KAIZOKU_RECEIVE_PRIZE_FEED_MESSAGE = u'%sが仲間を<a href="http://mpf.gree.jp/2440">海賊道</a>に招待！%sを無料でGETした！'
    REGISTRATION_REWARD_ID = 6

    # イベント開催期間中か
    EVENT_IS_OPEN_TERM = False

    # イベントがラストスパート期間か
    EVENT_IS_SPURT = False

    # イベントがラストスパート期間中の係数
    EVENT_SPURT_COEFFICIENT = 1.5

    # スマフォ対応？ログインボーナス
    IS_LOGIN_BONUS_SIX_DAYS = True if datetime.datetime.today().month == 8 and datetime.datetime.today().day >= 20 and datetime.datetime.today().day <= 30 else False

    # スマフォ対応？ログインボーナスのプレゼント文言
    LOGIN_BONUS_SIX_DAYS_PRESENT_MESSAGE = u'ｽﾏｰﾄﾌｫﾝ対応記念ｷｬﾝﾍﾟｰﾝ!%d回目のﾌﾟﾚｾﾞﾝﾄ!!'

    # ログインボーナスの景品
    LOGIN_BONUS_SIX_DAYS_ITEMS = (
        (
         (TYPE_ITEM, 36, 1),
        ),
        (
         (TYPE_CARD, 191, 1),
        ),
        (
         (TYPE_CARD, 188, 1),
         (TYPE_CARD, 189, 1),
         (TYPE_CARD, 190, 1),
        ),
        (
         (TYPE_ITEM, 1, 3),
        ),
        (
         (TYPE_ITEM, 14, 3),
        ),
        (
         (TYPE_ITEM, 36, 1),
        ),
    )

    # メダル景品に龍巫女、レディガチャが出現している
    IS_MEDAL_ITEM_RARE_OPEN = False

    # ガチャスロット
    #スロットを回せる回数
    GACHASROT_MAXIMUM_PROGRESS = 3
    #チャンスボーナスの最大値
    GACHASROT_CHANCEBONUS_MAXIMUM_NUM = 1000
    #チャンスボーナスで付与されるポイント
    GIVE_GACHASROT_CHANCEBONUS_POINT = {
        10: 224,
        9: 192,
        8: 240,
        7: 224,
        6: 192,
        0: 0
    }

    GACHASROT_PROBABILITY = {
        'seven_start': 91,
        'seven_end': 100,
        'bell_start': 0,
        'bell_end': 44,
        'cherry_start': 45,
        'cherry_end': 90
    }

    # NPCPlayer の持つ PlayerYakuza の実 Player の ID
    # 任侠道の公式ユーザーや他のユーザーと重ならないように海賊道の公式ユーザー
    NPC_OWNER_PLAYER_ID = 46212981

    ### RAIDイベント(戦国ヤクザ)
    # ポイント増量フラグ
    RAID_IS_POINT_BONUS = False
    # ゼニー増量フラグ
    RAID_IS_MONY_BONUS = False
    # ゼニー増量係数
    RAID_MONEY_COEFFICIENT = 2

    # レイドでの回復アイテム指定
    # RAID_USE_ITEM_MY_DRINK = 6
    # RAID_USE_ITEM_DRINK = 7
    # RAID_USE_ITEM_CANDY_1 = 1
    # RAID_USE_ITEM_CANDY_2 = 2
    # RAID_USE_ITEM_CANDY_3 = 3
    # RAID_USE_ITEM_CANDY_4 = 4
    # RAID_USE_ITEM_CANDY_5 = 5
    # RAID_USE_ITEM_MELT_DRINK = 8

    # RAID_LOVE_ITEM = {
    #         RAID_USE_ITEM_MY_DRINK: 137,
    #         RAID_USE_ITEM_DRINK: 2,
    #         RAID_USE_ITEM_CANDY_1: 44,
    #         RAID_USE_ITEM_CANDY_2: 44,
    #         RAID_USE_ITEM_CANDY_3: 44,
    #         RAID_USE_ITEM_CANDY_4: 44,
    #         RAID_USE_ITEM_CANDY_5: 44,
    #         RAID_USE_ITEM_MELT_DRINK: 245,
    #         }
    #

    # TODO 多分使わない
    # REFRESH_FAQ_ID = 25
    # ポイント増量係数 RAID_POINT_COEFFICIENT = 2

    # キノコ狩り
    EVENT_HAREM_SKILL_INCIDENCE = 3

    EVENT_URL_MAPPING = {
            102: "harem_index",
    }

    # 初心者ガチャのID（100円、200円、300円）
    BEGINNER_GACHA_FIGHTER = (42, 45, 48)
    BEGINNER_GACHA_GAMBLER = (43, 46, 49)
    BEGINNER_GACHA_INTELIGENCE = (44, 47, 50)
    BEGINNER_LAST_GACHA = (48, 49, 50, )
    BEGINNER_GACHA_ALL = (42, 43, 44, 45, 46, 47, 48, 49, 50, )

    # DONATION_GACHA_IDS
    DONATION_GACHA_IDS = (72, 73, 74, 75, 76, )

    # TODO 仮置き
    CHECK_EVENT_ID = [117]

    # デバックアイテムリスト
    DEBUG_ITEM_IDS = (65, 66)

    # 広告の暗号化キー
    AD_PROGRAM_KEY = '_kncSX3H'

    # 温泉発見で回復する体力
    CAMPAIGN_CURE_POINT = 30

    # レンタルボックスのID
    ID_RENTAL_BOX = 71

    #レアミキサーのみのbanリスト
    RARE_MIXER_BAN_LIST = []

    # ポーナスカテゴリ
    BONUS_CATEGORY_SUCCESSION = 1
    BONUS_CATEGORY = (
        (0, '未設定'),
        (BONUS_CATEGORY_SUCCESSION, u'継続ﾎﾟｰﾅｽ')
    )

    #
    NOTICE_CATEGORY_CAMPAIGN = 1
    NOTICE_CATEGORY_EVENT = 2
    NOTICE_CATEGORY_NEWFUNCTION = 3
    NOTICE_CATEGORY_CABA = 4
    NOTCIE_CATEGORY_RENEWAL = 5
    NOTCIE_CATEGORY_GACHA = 6


    # スロットカテゴリー

    #スロット開催数
    SLOT_HELD_NUM = 2

    SLOT_REEL_1 = 1     # 一番目
    SLOT_REEL_2 = 2     # 二番目
    SLOT_REEL_3 = 3     # 三番目

    SLOT_REWARD_CATEGORY_CARD_NONE = 0      # 外れ
    SLOT_REWARD_CATEGORY_CARD_HALF = 1      # 自属性ﾊｰﾌﾊﾆｰ
    SLOT_REWARD_CATEGORY_MONEY_1000 = 2     # 銭1000
    SLOT_REWARD_CATEGORY_POINT_200 = 3      # 盃200
    SLOT_REWARD_CATEGORY_ITEM_HONEY = 4     # ﾊﾆｰｶﾞﾁｬﾁｹｯﾄ
    SLOT_REWARD_CATEGORY_CARD_RHZ = 5       # 龍巫女
    SLOT_REWARD_CATEGORY_MONEY_20000 = 6    # 銭20000
    SLOT_REWARD_CATEGORY_POINT_2000 = 7     # 盃2000
    SLOT_REWARD_CATEGORY_SMALL_HONEY = 8    # 小技ﾊﾆｰ
    SLOT_REWARD_CATEGORY_GACHA_S = 9        # Sｶﾞﾁｬﾁｹｯﾄ

    SLOT_REWARD_CHOICE = (
        (SLOT_REWARD_CATEGORY_CARD_NONE, u'外れ'),
        (SLOT_REWARD_CATEGORY_MONEY_1000, u'銭1000'),
        (SLOT_REWARD_CATEGORY_POINT_200, u'盃200'),
        (SLOT_REWARD_CATEGORY_ITEM_HONEY, u'ﾊﾆｰｶﾞﾁｬﾁｹｯﾄ'),
        (SLOT_REWARD_CATEGORY_CARD_HALF, u'自属性ﾊｰﾌﾊﾆｰ'),
        (SLOT_REWARD_CATEGORY_MONEY_20000, u'銭20000'),
        (SLOT_REWARD_CATEGORY_POINT_2000, u'盃2000'),
        (SLOT_REWARD_CATEGORY_SMALL_HONEY, u'小技ﾊﾆｰ'),
        (SLOT_REWARD_CATEGORY_CARD_RHZ, u'龍巫女'),
        (SLOT_REWARD_CATEGORY_GACHA_S, u'Sｶﾞﾁｬﾁｹｯﾄ')
    )

    SLOT_REWARDS_NAME = {
        SLOT_REWARD_CATEGORY_CARD_NONE: u'外れ',
        SLOT_REWARD_CATEGORY_MONEY_1000: u'銭1000',
        SLOT_REWARD_CATEGORY_POINT_200: u'盃200',
        SLOT_REWARD_CATEGORY_ITEM_HONEY: u'ﾊﾆｰｶﾞﾁｬﾁｹｯﾄ',
        SLOT_REWARD_CATEGORY_CARD_HALF: u'自属性ﾊｰﾌﾊﾆｰ',
        SLOT_REWARD_CATEGORY_MONEY_20000: u'銭20000',
        SLOT_REWARD_CATEGORY_POINT_2000: u'盃2000',
        SLOT_REWARD_CATEGORY_SMALL_HONEY: u'小技ﾊﾆｰ',
        SLOT_REWARD_CATEGORY_CARD_RHZ: u'龍巫女',
        SLOT_REWARD_CATEGORY_GACHA_S: u'Sｶﾞﾁｬﾁｹｯﾄ'
    }

    SLOT_REWARD_DETAIL = {
        SLOT_REWARD_CATEGORY_MONEY_1000: 1000,
        SLOT_REWARD_CATEGORY_POINT_200: 200,
        SLOT_REWARD_CATEGORY_ITEM_HONEY: 54,
        SLOT_REWARD_CATEGORY_CARD_HALF: {
            CATEGORY_FIGHTER: 225,
            CATEGORY_GAMBLER: 226,
            CATEGORY_INTERIGENCE: 227
            },
        SLOT_REWARD_CATEGORY_MONEY_20000: 20000,
        SLOT_REWARD_CATEGORY_POINT_2000: 2000,
        SLOT_REWARD_CATEGORY_SMALL_HONEY: 598,
        SLOT_REWARD_CATEGORY_CARD_RHZ: 288,
        SLOT_REWARD_CATEGORY_GACHA_S:33
        }

    SLOT_REWARD_CATEGORY_MESSAGES = {
        SLOT_REWARD_CATEGORY_MONEY_1000: u'ｽﾛｯﾄを武闘で止めた!1000銭ｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_POINT_200: u'ｽﾛｯﾄを博徒で止めた!200盃ｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_ITEM_HONEY: u'ｽﾛｯﾄをｲﾝﾃﾘで止めた!ﾊﾆｰｶﾞﾁｬﾁｹｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_CARD_HALF: u'ｽﾛｯﾄを任侠道で止めた!ﾊｰﾌﾊﾆｰｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_MONEY_20000: u'FEVER!武闘で揃えて20000銭ｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_POINT_2000: u'FEVER!博徒で揃えて2000盃ｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_SMALL_HONEY: u'FEVER!ｲﾝﾃﾘで揃えて小技ﾊﾆｰｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_CARD_RHZ: u'FEVER!任侠道で揃えて龍巫女ｹﾞｯﾄ!',
        SLOT_REWARD_CATEGORY_GACHA_S: u'FEVER!ﾊﾞﾗﾊﾞﾗ賞でSRｶﾞﾁｬﾁｹｹﾞｯﾄ!'
    }

    # プロモ機能をつかった全員補償
    COMPENSATION_PROMOS_LIST = [5, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25,
            26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]

    # 未成年の年齢定義（指定値未満が未成年）
    MINOR_AGE_BORDER = 20

    GAME_EVENT = 1
    GAME_CAMPAIGN = 2

    GAME_CATEGORY = (
        (GAME_EVENT, u'イベント'),
        (GAME_CAMPAIGN, u'キャンペーン')
    )

    ADD_JIMAWARI_BONUS =[18]

    # 入魂費用割引の分母
    COMPOSE_CAMPAIGN_MONEY_COEFFICIENT = 2


class RaidItemValues(object):

    RAID_LOVE_ITEM_CANDY = StaticValues.RECOVER_LOVE_ONE_ITEM_ID # 慈愛ちょっとだけ回復
    RAID_LOVE_ITEM_DRINK = StaticValues.RECOVER_LOVE_ITEM_ID # 慈愛全回復
    RAID_LOVE_ITEM_MY_DRINK =  StaticValues.OWN_RECOVER_LOVE_ITEM_ID # 自分専用の慈愛全回復
    RAID_LOVE_ITEM_MELT_DRINK = StaticValues.RECOVER_LOVE_LIMITED_ID # とける慈愛全回復
    RAID_LOVE_ITEM_MY_CANDY = StaticValues.RECOVER_LOVE_ONE_SELF_ITEM_ID # 自分専用の慈愛ちょっとだけ回復

    RAID_LOVE_ONE_ITEM_IDS = (
        RAID_LOVE_ITEM_CANDY,
        RAID_LOVE_ITEM_MY_CANDY,
    )

    # レイドでの回復アイテム指定
    RAID_USE_ITEM_CANDY_1 = 1
    RAID_USE_ITEM_CANDY_2 = 2
    RAID_USE_ITEM_CANDY_3 = 3
    RAID_USE_ITEM_CANDY_4 = 4
    RAID_USE_ITEM_CANDY_5 = 5
    RAID_USE_ITEM_MY_DRINK = 6
    RAID_USE_ITEM_DRINK = 7
    RAID_USE_ITEM_MELT_DRINK = 8
    RAID_USE_ITEM_MY_CANDY_1 = 9
    RAID_USE_ITEM_MY_CANDY_2 = 10
    RAID_USE_ITEM_MY_CANDY_3 = 11
    RAID_USE_ITEM_MY_CANDY_4 = 12
    RAID_USE_ITEM_MY_CANDY_5 = 13

    RAID_LOVE_ITEM_DICT = {
        RAID_USE_ITEM_CANDY_1: u'まむしｷｬﾝﾃﾞｨ×1',
        RAID_USE_ITEM_CANDY_2: u'まむしｷｬﾝﾃﾞｨ×2',
        RAID_USE_ITEM_CANDY_3: u'まむしｷｬﾝﾃﾞｨ×3',
        RAID_USE_ITEM_CANDY_4: u'まむしｷｬﾝﾃﾞｨ×4',
        RAID_USE_ITEM_CANDY_5: u'まむしｷｬﾝﾃﾞｨ×5',
        RAID_USE_ITEM_MY_DRINK: u'自分専用まむしｷﾝｸﾞ',
        RAID_USE_ITEM_DRINK: u'まむしｷﾝｸﾞ',
        RAID_USE_ITEM_MELT_DRINK: u'まむしｱｲｽ',
        RAID_USE_ITEM_MY_CANDY_1: u'自分専用まむしｷｬﾝﾃﾞｨ×1',
        RAID_USE_ITEM_MY_CANDY_2: u'自分専用まむしｷｬﾝﾃﾞｨ×2',
        RAID_USE_ITEM_MY_CANDY_3: u'自分専用まむしｷｬﾝﾃﾞｨ×3',
        RAID_USE_ITEM_MY_CANDY_4: u'自分専用まむしｷｬﾝﾃﾞｨ×4',
        RAID_USE_ITEM_MY_CANDY_5: u'自分専用まむしｷｬﾝﾃﾞｨ×5',
    }

    RAID_LOVE_ITEM = {
        RAID_USE_ITEM_CANDY_1: 44,
        RAID_USE_ITEM_CANDY_2: 44,
        RAID_USE_ITEM_CANDY_3: 44,
        RAID_USE_ITEM_CANDY_4: 44,
        RAID_USE_ITEM_CANDY_5: 44,
        RAID_USE_ITEM_MY_DRINK: 137,
        RAID_USE_ITEM_DRINK: 2,
        RAID_USE_ITEM_MELT_DRINK: 245,
        RAID_USE_ITEM_MY_CANDY_1: 377,
        RAID_USE_ITEM_MY_CANDY_2: 377,
        RAID_USE_ITEM_MY_CANDY_3: 377,
        RAID_USE_ITEM_MY_CANDY_4: 377,
        RAID_USE_ITEM_MY_CANDY_5: 377,
    }

    # レイド回復アイテムのIDと個数の対応
    RAID_LOVE_ITEM_QUANTITY_DICT = {
        RAID_USE_ITEM_CANDY_1: 1,
        RAID_USE_ITEM_CANDY_2: 2,
        RAID_USE_ITEM_CANDY_3: 3,
        RAID_USE_ITEM_CANDY_4: 4,
        RAID_USE_ITEM_CANDY_5: 5,
        RAID_USE_ITEM_MY_DRINK: 1,
        RAID_USE_ITEM_DRINK: 1,
        RAID_USE_ITEM_MELT_DRINK: 1,
        RAID_USE_ITEM_MY_CANDY_1: 1,
        RAID_USE_ITEM_MY_CANDY_2: 2,
        RAID_USE_ITEM_MY_CANDY_3: 3,
        RAID_USE_ITEM_MY_CANDY_4: 4,
        RAID_USE_ITEM_MY_CANDY_5: 5,
    }

    # レイド回復アイテムのIDと回復量の対応
    RAID_LOVE_ITEM_USE_RECOVER_LOVE_DICT = {
        RAID_USE_ITEM_CANDY_1: 1,
        RAID_USE_ITEM_CANDY_2: 2,
        RAID_USE_ITEM_CANDY_3: 3,
        RAID_USE_ITEM_CANDY_4: 4,
        RAID_USE_ITEM_CANDY_5: 5,
        RAID_USE_ITEM_MY_DRINK: 5,
        RAID_USE_ITEM_DRINK: 5,
        RAID_USE_ITEM_MELT_DRINK: 5,
        RAID_USE_ITEM_MY_CANDY_1: 1,
        RAID_USE_ITEM_MY_CANDY_2: 2,
        RAID_USE_ITEM_MY_CANDY_3: 3,
        RAID_USE_ITEM_MY_CANDY_4: 4,
        RAID_USE_ITEM_MY_CANDY_5: 5,
    }
