# -*- coding: utf-8 -*-

import actionlog

'''

アクションログのユーティリティクラス

使い方の例：
from common.actionlog_utils import ActionLogUtils

ActionLogUtils.write_poke_log(引数)

実際の使い方は
gokudo/mobile/poke.py 行87 を参照してください。

TIPS! 重要なこと
数値、Falseなど、アスキー文字列で表せるものは 文字列 で保存します。
日本語が含まれる可能性がある場合、必ず「repr」で変換してください。
ログに保存可能なのはアスキー文字列のみです。

アクションログに保存する場合、以下の情報は保存する必要はありません。
・実行しているユーザのIDと名前

アクションログでマスターにあるオブジェクト（アイテムや極道など）を保存する場合、次のキーを保存して下さい。
・オブジェクトのIDと名前
　※IDだけ、名前だけ、は調査困難となりますので、使用しないで下さい。

オブジェクトの数の増減がある場合（アイテムが増えるとか）、増減前、増減後も可能な限りいれましょう
　※お金とかも前と後があると追跡で便利です

アクションログに使用可能な文字列：
ASCII文字列のみ。変化のない値（ログのタイトルなど）でSQL上で使うのにエスケープが必要な記号は使わないようにしましょう！
　※?とか*とか%とか


'''

class EventActionLogUtils(object):
    event_id = 0

    @classmethod
    def get_event_id(cls):
        return cls.event_id

    @classmethod
    def write(cls, action, osuser_id, record):
        event_id = cls.get_event_id()
        if event_id:
            record = (
                    '[EventID]', str(event_id),
                    ) + record

        actionlog.write(action, osuser_id, record)

    @classmethod
    def write_easymode_cancel_log(cls, player_id):
        '''
        easymodeが解除されたタイミングを記録
        '''

        record = (
            '[PlayerId]', str(player_id),
        )

        actionlog.write('EASYMODE_CANCEL', player_id, record)

    @classmethod
    def write_easymode_relate_error_log(cls, player_id):
        '''
        easymodeが他のユーザによる参照エラーで初期化されたとき
        '''

        record = (
            '[PlayerId]', str(player_id),
        )

        actionlog.write('EASYMODE_RERATE_ERROR', player_id, record)

class ActionLogUtils(object):


    @classmethod
    def write_tutorial_before_reset_player_log(cls, player):
        '''
        チュートリアル途中で新チュートリアルに切り替わった人。１回リセットしていますログ
        '''
        record = (
            '[IsReset]', '1',
            )

        actionlog.write('NEW_TUTORIAL_RESET', player.pk, record)

    @classmethod
    def write_daily_log(cls, player, device, user_agent):
        '''
        GA_ATTRIBUTE
        '''
        record = (
            '[device]', str(device),
            '[model]', str(user_agent),
            )

        actionlog.write('GA_ATTRIBUTE', player.pk, record)

    @classmethod
    def write_zako_assign_log(cls, player, zako_ids):
        '''
        雑魚舎弟を自動アサインしましたログ
        '''
        record = (
            '[IsAssign]', '1',
            '[AssignZakoIDs]', ','.join(zako_ids),
            )

        actionlog.write('ZAKO_YAKUZA_ASSIGN', player.pk, record)

    @classmethod
    def write_add_levelup_log(cls, player, before_exp, after_exp, exp, before_level, after_level, level, before_power, after_power, before_max_power, after_max_power):
        '''
        レベルアップしたログ
        '''

        record = (
            '[BeforeExp]', str(before_exp),
            '[AfterExp]', str(after_exp),
            '[GetExp]', str(exp),
            '[BeforeLevel]', str(before_level),
            '[AfterLevel]', str(after_level),
            '[GetLevel]', str(level),
            '[BeforePower]', str(before_power),
            '[AfterPower]', str(after_power),
            '[BeforeMaxPower]', str(before_max_power),
            '[AfterMaxPower]', str(after_max_power),
            )

        actionlog.write('LEVEL_UP', player.pk, record)

    @classmethod
    def write_walk_log(cls, player, place_id, before_exp, after_exp, exp, before_money, after_money, money, before_power, after_power, power, before_achievement_level, after_achievement_level, achievement_level, pop_npc, is_rookie=False):
        '''
        地回りしたログ
        '''

        record = (
            '[PlaceID]', str(place_id),
            '[BeforeExp]', str(before_exp),
            '[AfterExp]', str(after_exp),
            '[GetExp]', str(exp),
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[GetMoney]', str(money),
            '[BeforePower]', str(before_power),
            '[AfterPower]', str(after_power),
            '[ConsumePower]', str(power),
            '[BeforeAchievementLevel]', str(before_achievement_level),
            '[AfterAchievementLevel]', str(after_achievement_level),
            '[AddAchievementLevel]', str(achievement_level),
            '[NpcClass]', str(pop_npc.__class__.__name__),
            '[NpcID]', str(pop_npc.pk) if pop_npc else '0',
            '[IsRookie]', str(is_rookie),
            )

        actionlog.write('JIMAWARI_WALK', player.pk, record)

    @classmethod
    def write_event_break_battle_log(cls, player, player_attack, target_player, target_player_defence, friend_player, friend_player_attack, is_win_attack, is_win_defence, old_pt, new_pt, reward_item_id, num_straight_wins):
        '''
        ハーレムイベントバトルログ
        '''

        is_friend = False
        friend_player_pk = None
        friend_player_name = None
        friend_player_level = None
        if friend_player:
            is_friend = True
            friend_player_pk = friend_player.pk
            friend_player_name = friend_player.name
            friend_player_level = friend_player.level

        record = (
                '[PlayerLevel]', str(player.level),
                '[TargetPlayerPk]', str(target_player.pk),
                '[TargetPlayerLevel]', str(target_player.level),
                '[Is_Friend]', str(is_friend),
                '[FriendPk]', str(friend_player_pk),
                '[FriendName]', repr(friend_player_name),
                '[FriendLevel]', str(friend_player_level),
                '[FriendAttackPoint]', str(friend_player_attack),
                '[IsWinAttack]', str(is_win_attack),
                '[IsWinDefence]', str(is_win_defence),
                '[PlayerAttackPoint]', str(player_attack),
                '[TargetPlayerDefencePoint]', str(target_player_defence),
                '[OldPT]', str(old_pt),
                '[NewPT]', str(new_pt),
                '[NumStraightWins]', str(num_straight_wins),
                '[reward_item_id]', str(reward_item_id),
        )
        actionlog.write('USER_BATTLE_BREAK', player.pk, record)

    @classmethod
    def write_tokonatsu_walk_log(cls, player, place_id, before_exp, after_exp, exp, before_money, after_money, money, before_power, after_power, power, before_achievement_level, after_achievement_level, achievement_level, pop_npc, before_point, after_point, point):
        '''
        地回りしたログ
        '''

        record = (
            '[PlaceID]', str(place_id),
            '[BeforeExp]', str(before_exp),
            '[AfterExp]', str(after_exp),
            '[GetExp]', str(exp),
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[GetMoney]', str(money),
            '[BeforePower]', str(before_power),
            '[AfterPower]', str(after_power),
            '[ConsumePower]', str(power),
            '[BeforeAchievementLevel]', str(before_achievement_level),
            '[AfterAchievementLevel]', str(after_achievement_level),
            '[AddAchievementLevel]', str(achievement_level),
            '[NpcClass]', str(pop_npc.__class__.__name__),
            '[NpcID]', str(pop_npc.pk) if pop_npc else 'None',
            '[BeforeCryptidPoint]', str(before_point),
            '[AfterCryptidPoint]', str(after_point),
            '[CryptidPoint]', str(point),
            )

        actionlog.write('ONI_WALK', player.pk, record)

    @classmethod
    def write_poke_log(cls, player, target_player, before_com_point, after_com_point, get_point):
        '''
        盃をかわしたログ
        '''

        record = (
            '[TargetPlayer]', str(target_player.pk),
            '[BeforeComPoint]', str(before_com_point),
            '[AfterComPoint]', str(after_com_point),
            '[GetComPoint]', str(get_point),
        )

        actionlog.write('POKE', player.pk, record)

    @classmethod
    def write_poke_comment_log(cls, player, target_player, before_com_point, after_com_point, get_point):
        '''
        盃をかわして、コメントを残したログ
        '''

        record = (
            '[TargetPlayer]', str(target_player.pk),
            '[BeforeComPoint]', str(before_com_point),
            '[AfterComPoint]', str(after_com_point),
            '[GetComPoint]', str(get_point),
        )

        actionlog.write('POKE_COMMENT', player.pk, record)

    @classmethod
    def write_userbattle_log(cls, player, target_player, user_battle_id, gokujo, get_money, my_before_money, my_after_money, target_before_money, target_after_money, is_win, is_trap, is_judgment):
        '''
        ユーザー間バトルログ
        '''
        gokujo_id = 0
        gokujo_name = u''

        if gokujo:
            gokujo_id = gokujo.pk
            gokujo_name = gokujo.name

        record = (
            '[UserBattleID]', str(user_battle_id),
            '[PlayerLevel]', str(player.level),
            '[CurrentPower]', str(player.get_current_power()),
            '[TargetPlayer]', str(target_player.pk),
            '[TargetPlayerLevel]', str(target_player.level),
            '[TargetGokujoID]', str(gokujo_id),
            '[TargetGokujoName]', repr(gokujo_name),
            '[GetMoney]', str(get_money),
            '[MyBeforeMoney]', str(my_before_money),
            '[MyAfterMoney]', str(my_after_money),
            '[TargetBeforeMoney]', str(target_before_money),
            '[TargetAfterMoney]', str(target_after_money),
            '[BattleResult]', str(is_win),
            '[SpendTrap]', str(is_trap),
            '[ShockJudgment]', str(is_judgment),
        )

        actionlog.write('USER_BATTLE', player.pk, record)

    @classmethod
    def write_event_kachikomi_log(cls, player, player_attack, target_player, target_player_defence, friend_player, friend_player_attack, is_win, get_exp, is_tenchu, player_kachikomi_pt, friend_kachikomi_pt, wrest_point):
        '''
        カチコミバトルログ
        '''

        is_friend = False
        friend_player_pk = None
        friend_player_name = None
        friend_player_level = None
        if friend_player:
            is_friend = True
            friend_player_pk = friend_player.pk
            friend_player_name = friend_player.name
            friend_player_level = friend_player.level

        record = (
                '[PlayerLevel]', str(player.level),
                '[TargetPlayerPk]', str(target_player.pk),
                '[TargetPlayerLevel]', str(target_player.level),
                '[Is_Friend]', str(is_friend),
                '[FriendPk]', str(friend_player_pk),
                '[FriendName]', repr(friend_player_name),
                '[FriendLevel]', str(friend_player_level),
                '[FriendAttackPoint]', str(friend_player_attack),
                '[Win]', str(is_win),
                '[PlayerAttackPoint]', str(player_attack),
                '[TargetPlayerDefencePoint]', str(target_player_defence),
                '[GetExp]', str(get_exp),
                '[Is_Tenchu]', str(is_tenchu),
                '[PlayerKachikomiPT]', str(player_kachikomi_pt),
                '[FriendKachikomiPT]', str(friend_kachikomi_pt),
                '[WrestPoint]', str(wrest_point),

        )
        actionlog.write('USER_BATTLE_KACHIKOMI', player.pk, record)

    @classmethod
    def write_event_cabaret_log(cls, player, player_attack, target_player, target_player_defence, friend_player, friend_player_attack, is_win, old_pt, new_pt, reward_item_id):
        '''
        キャバイベントバトルログ
        '''

        is_friend = False
        friend_player_pk = None
        friend_player_name = None
        friend_player_level = None
        if friend_player:
            is_friend = True
            friend_player_pk = friend_player.pk
            friend_player_name = friend_player.name
            friend_player_level = friend_player.level

        record = (
                '[PlayerLevel]', str(player.level),
                '[TargetPlayerPk]', str(target_player.pk),
                '[TargetPlayerLevel]', str(target_player.level),
                '[Is_Friend]', str(is_friend),
                '[FriendPk]', str(friend_player_pk),
                '[FriendName]', repr(friend_player_name),
                '[FriendLevel]', str(friend_player_level),
                '[FriendAttackPoint]', str(friend_player_attack),
                '[Win]', str(is_win),
                '[PlayerAttackPoint]', str(player_attack),
                '[TargetPlayerDefencePoint]', str(target_player_defence),
                '[OldPT]', str(old_pt),
                '[NewPT]', str(new_pt),
                '[reward_item_id]', str(reward_item_id),
        )
        actionlog.write('USER_BATTLE_CABARET', player.pk, record)

    @classmethod
    def write_event_stadium_log(cls, player, player_attack, target_player, target_player_defence, friend_player, friend_player_attack, is_win, player_score, target_player_score):
        '''
        カチスタのバトルログ
        '''

        is_friend = False
        friend_player_pk = None
        friend_player_name = None
        friend_player_level = None
        if friend_player:
            is_friend = True
            friend_player_pk = friend_player.pk
            friend_player_name = friend_player.name
            friend_player_level = friend_player.level
        if target_player.npc:
            npc_id = target_player.npc.pk
        else:
            npc_id = 0

        record = (
                '[PlayerLevel]', str(player.level),
                '[TargetPlayerPk]', str(target_player.pk),
                '[NPC]', str(npc_id),
                '[TargetPlayerLevel]', str(target_player.level),
                '[Is_Friend]', str(is_friend),
                '[FriendPk]', str(friend_player_pk),
                '[FriendName]', repr(friend_player_name),
                '[FriendLevel]', str(friend_player_level),
                '[FriendAttackPoint]', str(friend_player_attack),
                '[Result]', 'Win' if is_win else 'Lose',
                '[RankLevel]', player.get_stadium_ranklevel(),
                '[PlayerAttackPoint]', str(player_attack),
                '[TargetPlayerDefencePoint]', str(target_player_defence),
                '[PlayerScore]', str(player_score),
                '[TargetPlayerScore]', str(target_player_score),
        )
        actionlog.write('USER_BATTLE_STADIUM_RESULT', player.pk, record)

    @classmethod
    def write_event_stadium_player_stat_log(cls, player, player_stat):
        '''
        カチスタの戦歴の記録
        '''
        record = (
                '[ActiveWin]', player_stat['active_win'],
                '[PassiveWin]', player_stat['passive_win'],
                '[ActiveLose]', player_stat['active_lose'],
                '[PassiveLose]', player_stat['passive_lose'],
                '[ClearCount]', player_stat['clear_count'],
                '[FailCount]', player_stat['fail_count'],
                '[IsClear]', player_stat['is_clear'],
                '[IsFail]', player_stat['is_fail'],
                '[IsRanklevelUp]', player_stat['is_ranklevel_up'],
                '[IsRanklevelDown]', player_stat['is_ranklevel_down'],
                '[IsRankUp]', player_stat['is_rank_up'],
                '[IsRankDown]', player_stat['is_rank_down'],
                '[IsMaxRanklevel]', player_stat['is_max_ranklevel'],
                '[AmountActiveWin]', player_stat['amount_active_win'],
                '[AmountPassiveWin]', player_stat['amount_passive_win'],
                '[AmountActiveLose]', player_stat['amount_active_lose'],
                '[AmountPassiveLose]', player_stat['amount_passive_lose'],
                '[MaxRanklevel]', player_stat['max_ranklevel'],
                '[IsGainRankUpRwward]', player_stat['is_gain_rank_up_reward'],
        )
        actionlog.write('USER_BATTLE_STADIUM_STAT', player.pk, record)

    @classmethod
    def write_stadium_receive_reward_log(cls, player, index_number, reward_number):
        '''
        カルタのコンプ報酬受け取りログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[IndexNumber]', str(index_number),
            '[RewardNumber]', str(reward_number),
            )
        actionlog.write('STADIUM_RECEIVE_REWARD', player.osuser_id, record)

    @classmethod
    def write_event_musou_log(cls, player, player_attack, target_player, target_player_defence, friend_player, friend_player_attack, is_win, get_exp, is_tenchu, player_kachikomi_pt, friend_kachikomi_pt, wrest_point):
        '''
        無双バトルログ
        （とりあえず、内容はカチコミバトルログと同じ）
        '''

        is_friend = False
        friend_player_pk = None
        friend_player_name = None
        friend_player_level = None
        if friend_player:
            is_friend = True
            friend_player_pk = friend_player.pk
            friend_player_name = friend_player.name
            friend_player_level = friend_player.level

        record = (
                '[PlayerPk]', str(player.pk),
                '[PlayerName]', repr(player.name),
                '[PlayerLevel]', str(player.level),
                '[TargetPlayerPk]', str(target_player.pk),
                '[TargetPlayerName]', repr(target_player.name),
                '[TargetPlayerLevel]', str(target_player.level),
                '[Is_Friend]', str(is_friend),
                '[FriendPk]', str(friend_player_pk),
                '[FriendName]', repr(friend_player_name),
                '[FriendLevel]', str(friend_player_level),
                '[FriendAttackPoint]', str(friend_player_attack),
                '[Win]', str(is_win),
                '[PlayerAttackPoint]', str(player_attack),
                '[TargetPlayerDefencePoint]', str(target_player_defence),
                '[GetExp]', str(get_exp),
                '[Is_Tenchu]', str(is_tenchu),
                '[PlayerKachikomiPT]', str(player_kachikomi_pt),
                '[FriendKachikomiPT]', str(friend_kachikomi_pt),
                '[WrestPoint]', str(wrest_point),

        )
        actionlog.write('USER_BATTLE_MUSOU', player.pk, record)

    @classmethod
    def write_add_com_log(cls, player, before_com, after_com, consume_com):
        '''
        盃ptを追加したログ
        '''

        record = (
            '[BeforeComPoint]', str(before_com),
            '[AfterComPoint]', str(after_com),
            '[AddComPoint]', str(consume_com),
        )

        actionlog.write('ADD_COM_POINT', player.pk, record)

    @classmethod
    def write_consume_power_log(cls, player, before_power, after_power, consume_power):
        '''
        体力を消費したログ
        '''

        record = (
            '[BeforePower]', str(before_power),
            '[AfterPower]', str(after_power),
            '[ConsumePower]', str(consume_power),
        )

        actionlog.write('CONSUME_POWER', player.pk, record)

    @classmethod
    def write_recover_power_log(cls, player, before_power, after_power, recover_power, item, rn, t):
        '''
        体力を回復したログ
        '''

        record = (
            '[BeforePower]', str(before_power),
            '[AfterPower]', str(after_power),
            '[CurrentMaxPower]', str(player.max_power),
            '[RecoverPower]', str(recover_power),
            '[ItemID]', str(item.pk),
            '[RecoverNumber]', rn,
            '[Time]', str(t),
        )

        actionlog.write('RECOVER_POWER', player.pk, record)

    @classmethod
    def write_recover_love_log(cls, player, before_love, after_love, recover_love, item=None, t=None):
        '''
        慈愛を回復したログ
        '''

        if item is not None:
            item = item.pk
        record = (
            '[BeforeLove]', str(before_love),
            '[AfterLove]', str(after_love),
            '[RecoverLove]', str(recover_love),
            '[ItemID]', str(item),
            '[Time]', str(t),
        )

        actionlog.write('RECOVER_LOVE', player.pk, record)

    @classmethod
    def write_consume_love_log(cls, player, before_love, after_love, consume_love):
        '''
        慈愛を消費したログ
        '''

        record = (
            '[BeforeLove]', str(before_love),
            '[AfterLove]', str(after_love),
            '[ConsumeLove]', str(consume_love),
        )

        actionlog.write('CONSUME_LOVE', player.pk, record)

    @classmethod
    def write_consume_com_log(cls, player, before_com, after_com, consume_com):
        '''
        盃を消費したログ
        '''

        record = (
            '[BeforeComPoint]', str(before_com),
            '[AfterComPoint]', str(after_com),
            '[ConsumeComPoint]', str(consume_com),
        )

        actionlog.write('CONSUME_COM_POINT', player.pk, record)

    @classmethod
    def write_gokujo_love_gift_log(cls, player, gokujo, before_level, after_level):
        '''
        極女に愛を注いだログ
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[CurrentPower]', str(player.get_current_power()),
            '[GokujoID]', str(gokujo.pk),
            '[GokujoName]', repr(gokujo.name),
            '[BeforeStoryLevel]', str(before_level),
            '[AfterStoryLevel]', str(after_level),
        )

        actionlog.write('LOVE_GIFT', player.pk, record)

    @classmethod
    def write_assign_item_log(cls, player, item, add_num, before_num, after_num):
        '''
        アイテムを追加したログ
        '''

        record = (
            '[ItemID]', str(item.pk),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[AssignNum]', str(add_num),
        )

        actionlog.write('ASSIGN_ITEM', player.pk, record)

    @classmethod
    def write_assign_melt_item_log(cls, player, item, add_num, time):
        '''
        溶けるアイテムの溶ける時間を追加したログ
        '''

        record = (
            '[ItemID]', str(item.pk),
            '[ItemName]', repr(item.name),
            '[AssignedNum]', str(add_num),
            '[MeltTime]', str(time),
        )

        actionlog.write('ASSIGN_MELT_ITEM', player.pk, record)

    @classmethod
    def write_melt_down_item_log(cls, player, item, down_num, before_num, after_num):
        '''
        溶けるアイテムの溶けたことを記録するログ
        '''

        record = (
            '[ItemID]', str(item.pk),
            '[ItemName]', repr(item.name),
            '[MeltNum]', str(down_num),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
        )

        actionlog.write('MELT_DOWN_ITEM', player.pk, record)

    @classmethod
    def write_assign_yakuza_log(cls, player, yakuza, player_yakuza, add_num=1):
        '''
        舎弟を追加したログ
        '''
        if yakuza:
            yakuza_name = yakuza.name
        else:
            yakuza_name = 'None'
        record = (
            '[PlayerYakuzaID]', str(player_yakuza.pk),
            '[PlayerYakuzaLevel]', str(player_yakuza.level),
            '[PlayerYakuzaExp]', str(player_yakuza.exp),
            '[PlayerYakuzaCreatedAt]', str(player_yakuza.created_at),
            '[PlayerYakuzaUpdatedAt]', str(player_yakuza.updated_at),
            '[YakuzaID]', str(yakuza.pk),
            '[YakuzaName]', repr(yakuza_name),
            '[AssignNum]', str(add_num),
        )

        actionlog.write('ASSIGN_YAKUZA', player.pk, record)

    @classmethod
    def write_get_drop_gokujo_log(cls, player, gokujo):
        '''
        極女を取得したログ
        '''

        record = (
            '[GokujoId]', str(gokujo.id),
            '[GokujoName]', repr(gokujo.name),
            )

        actionlog.write('GET_GOKUJO', player.pk, record)

    @classmethod
    def write_get_drop_treasure_log(cls, player, gokujo, before, after, num):
        '''
        秘宝を取得したログ
        '''

        record = (
            '[GokujoId]', str(gokujo.id),
            '[GokujoName]', repr(gokujo.name),
            '[BeforeNum]', str(before),
            '[AfterNum]', str(after),
            '[AddNum]', str(num),
            )

        actionlog.write('GET_GOKUJO_TREASURE', player.pk, record)

    @classmethod
    def write_gacha_log(cls, player, gacha, yakuza, add_num=1, lunch_time_gacha=0):
        '''
        ガチャを回したログ
        '''

        record = (
            '[GachaID]', str(gacha.pk),
            '[YakuzaID]', str(yakuza.pk),
            '[YakuzaName]', repr(yakuza.name),
            '[Rarity]', str(yakuza.rarity),
            '[Category]', str(yakuza.category),
            '[AssignNum]', str(add_num),
            '[LunchTime]', str(lunch_time_gacha),
        )

        actionlog.write('DO_GACHA', player.pk, record)

    @classmethod
    def write_gacha_mixing_log(cls, player, gacha, yakuza, material_yakuza, add_num=1):
        '''
        ミキサーガチャ実行ログ
        '''

        record = (
            '[GachaID]', str(gacha.pk),
            '[YakuzaID]', str(yakuza.pk),
            '[YakuzaName]', repr(yakuza.name),
            '[Rarity]', str(yakuza.rarity),
            '[Category]', str(yakuza.category),
            '[MaterialID]', str(material_yakuza.pk),
            '[MaterialName]', repr(material_yakuza.name),
            '[MaterialRarity]', str(material_yakuza.rarity),
            '[AssignNum]', str(add_num),
        )

        actionlog.write('MIXER_GACHA', player.pk, record)


    @classmethod
    def write_buy_gacha_log(cls, player, gacha, price, point_code):
        '''
        有料ガチャを購入
        '''

        record = (
            '[GachaID]', str(gacha.pk),
            '[Price]', str(price),
            '[PointCode]', str(point_code),
        )

        actionlog.write('BUY_GACHA', player.pk, record)

    @classmethod
    def write_buy_gacha_timeout_log(cls, player, gacha, price, point_code):
        '''
        ガチャ決済のタイムアウト
        '''

        record = (
                '[GachaID]', str(gacha.pk),
                '[Price]', str(price),
                '[PointCode]', str(point_code),
                '[PlayerID]', str(player.pk),
        )

        actionlog.write('BUY_GACHA_TIMEOUT', player.pk, record)

    @classmethod
    def write_base_place_clear_log(cls, player, base_place):
        '''
        県制覇
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[BasePlaceID]', str(base_place.pk),
            )

        actionlog.write('CLEAR_BASE_PLACE', player.pk, record)


    @classmethod
    def write_middle_place_clear_log(cls, player, middle_place):
        '''
        都市制覇
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[MiddlePlaceID]', str(middle_place.pk),
            )

        actionlog.write('CLEAR_MIDDLE_PLACE', player.pk, record)


    @classmethod
    def write_receive_present_log(cls, player, present, present_name, player_yakuza_id=0):
        '''
        プレゼントを受け取った
        '''

        record = (
            '[PresentID]', str(present.pk),
            '[SendPlayerID]', str(present.send_player_id),
            '[PresentType]', str(present.type),
            '[PresentObjectID]', str(present.present),
            '[PresentName]', repr(present_name),
            '[PresentCount]', str(present.num),
            '[Message]', repr(present.text) if present.text else 'None',
            '[YakuzaID]', str(player_yakuza_id),
            )

        actionlog.write('RECEIVE_PRESENT', player.pk, record)

    @classmethod
    def write_receive_present_error_log(cls, player, present, present_name, player_yakuza_id=0):
        '''
        プレゼントの受け取り失敗ログ
        '''

        record = (
            '[PresentID]', str(present.pk),
            '[SendPlayerID]', str(present.send_player_id) if present.send_player_id else 'None',
            '[PresentType]', str(present.type),
            '[PresentObjectID]', str(present.present) if present.present else 'None',
            '[PresentName]', repr(present_name) if present_name else 'None',
            '[PresentCount]', str(present.num) if present.num else 'None',
            '[Message]', repr(present.text) if present.text else 'None',
            '[YakuzaID]', str(player_yakuza_id),
            )

        actionlog.write('RECEIVE_PRESENT_ERROR', player.pk, record)


    @classmethod
    def write_give_official_present_log(cls, player, present, txt, type, num=1, time_limited=None):
        '''
        プレゼントを贈った
        '''
        present_id = None
        present_name = None
        type = int(type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = 0
            present_name = 'communication_point'
        elif type == 6:
            present_id = 0
            present_name = 'medal'
        elif present:
            present_id = present.pk
            try:
                present_name = present.name
            except AttributeError:
                present_name = present.__class__.__name__
        else:
            present_id = 0
            present_name = present.__class__.__name__

        record = (
            '[TargetPlayerID]', str(player.pk),
            '[PresentType]', str(type),
            '[PresentID]', str(present_id),
            '[PresentName]', repr(present_name),
            '[PresentCount]', str(num),
            '[TimeLimited]', str(time_limited),
            '[Message]', repr(txt) if txt else 'None',
            )

        actionlog.write('GIVE_OFFICIAL_PRESENT', player.pk, record)

    @classmethod
    def write_give_compensation_present_log(cls, player, present, txt, type, num=1):
        '''
        補償用スクリプトからプレゼントを贈った
        内容はwrite_give_official_present_logと同じ
        '''
        present_id = None
        present_name = None
        type = int(type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = 0
            present_name = 'communication_point'
        elif type == 6:
            present_id = 0
            present_name = 'medal'
        elif present:
            present_id = present.pk
            try:
                present_name = present.name
            except AttributeError:
                present_name = present.__class__.__name__
        else:
            present_id = 0
            present_name = present.__class__.__name__

        record = (
            '[TargetPlayerID]', str(player.pk),
            '[PresentType]', str(type),
            '[PresentID]', str(present_id),
            '[PresentName]', repr(present_name),
            '[PresentCount]', str(num),
            '[Message]', repr(txt) if txt else 'None',
            )

        actionlog.write('GIVE_COMPENSATION_PRESENT', player.pk, record)

    @classmethod
    def write_give_present_log(cls, player, present, present_name='None'):
        '''
        プレゼントを贈った
        '''

        record = (
            '[PresentID]', str(present.pk),
            '[TargetPlayerID]', str(present.player_id),
            '[PresentType]', str(present.type),
            '[PresentObjectID]', str(present.present),
            '[PresentName]', repr(present_name),
            '[PresentCount]', str(present.num),
            '[TimeLimited]', str(present.time_limited),
            '[Message]', repr(present.text) if present.text else 'None',
            )

        actionlog.write('GIVE_PRESENT', player.pk if player else '0', record)

    @classmethod
    def write_give_present_error_log(cls, player, exc_info):
        '''
        プレゼントを贈ろうとしたが、送れなかった
        プレゼントの情報はGIVE_OFFICIAL_PRESENTを参照する方向で
        '''

        #長さ不明なので、念のためreprで
        record = (
            '[ExcInfoType]', repr(exc_info[0]),
            '[ExcInfoValue]', repr(exc_info[1]),
            '[ExcInfoTraceback]', repr(exc_info[2]),
            )

        actionlog.write('ERROR_GIVE_PRESENT', player.pk if player else '0', record)

    @classmethod
    def complete_gokujo_log(cls, player, base_place):
        '''
        極女コンプ
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[BasePlaceID]', str(base_place.pk),
            '[BasePlaceName]', repr(base_place.name),
            )

        actionlog.write('COMPLETE_GOKUJO', player.pk, record)

    @classmethod
    def complete_treasure_log(cls, player, treasure_category):
        '''
        秘宝コンプ
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[TreasureCategoryID]', str(treasure_category.pk),
            '[TreasureCategoryName]', repr(treasure_category.name),
            )

        actionlog.write('COMPLETE_GOKUJO', player.pk, record)

    @classmethod
    def append_wish_list_log(cls, player, yakuza):
        '''
        欲しいものリストに追加
        '''

        record = (
            '[YakuzaID]', str(yakuza.id),
            '[YakuzaName]', repr(yakuza.name),
            )

        actionlog.write('APPEND_WISH_LIST', player.pk, record)

    @classmethod
    def purchase_item_log(cls, player, item, is_equip, payment_obj):
        '''
        アイテム購入
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[IsEquipItem]', str(is_equip),
            '[ItemID]', str(item.pk),
            '[ItemName]', repr(item.name),
            #'[ItemCategory]', str(item.category),
            '[ItemPoint]', str(item.point),
            '[ItemCount]', str(payment_obj.quantity),
            '[AllPoint]', str(item.point * payment_obj.quantity),
            )

        actionlog.write('PURCHASE_ITEM', player.pk, record)

    @classmethod
    def purchase_item_timeout_log(cls, player, item, payment_obj):
        '''
        アイテム購入時のタイムアウトエラー
        '''

        record = (
            '[PlayerLevel]', str(player.level),
            '[ItemID]', str(item.pk),
            '[ItemName]', repr(item.name),
            #'[ItemCategory]', str(item.category),
            '[ItemPoint]', str(item.point),
            '[ItemCount]', str(payment_obj.quantity),
            '[AllPoint]', str(item.point * payment_obj.quantity),
            )

        actionlog.write('PURCHASE_ITEM_TIMEOUT', player.pk, record)


    @classmethod
    def yakuza_convert_money_log(cls, player, yakuza, money, before_money, after_money):
        '''
        舎弟売却
        '''

        record = (
            '[YakuzaID]', str(yakuza.pk),
            '[YakuzaName]', repr(yakuza.name),
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[Money]', str(money),
            )

        actionlog.write('YAKUZA_CONVERT_MONEY', player.pk, record)

    @classmethod
    def all_yakuza_convert_money_log(cls, player, yakuzas, money, before_money, after_money):
        '''
        一括舎弟売却
        '''

        record = (
            '[YakuzaIDs]', str(','.join(yakuzas)),
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[Money]', str(money),
            )

        actionlog.write('YAKUZA_ALL_CONVERT_MONEY', player.pk, record)

    @classmethod
    def yakuza_convert_exp_log(cls, player, base_yakuza, material_yakuza, exp, before_level, before_exp, before_attack, before_defence, skill_ids, skill_lvs, before_skill_lvs, material_player_yakuza):
        '''
        舎弟合成
        '''

        record = (
            '[BaseYakuzaID]', str(base_yakuza.yakuza.pk),
            '[BaseYakuzaName]', repr(base_yakuza.yakuza.name),
            '[BasePlayerYakuzaID]', str(base_yakuza.pk),
            '[MaterialYakuzaID]', str(material_yakuza.pk),
            '[MaterialYakuzaName]', repr(material_yakuza.name),
            '[MaterialPlayerYakuzaID]', str(material_player_yakuza.pk),
            '[MaterialYakuzaLevel]', str(material_player_yakuza.level),
            '[Exp]', str(exp),
            '[BeforeLevel]', str(before_level),
            '[AfterLevel]', str(base_yakuza.level),
            '[BeforeExp]', str(before_exp),
            '[AfterExp]', str(base_yakuza.exp),
            '[BeforeAttack]', str(before_attack),
            '[AfterAttack]', str(base_yakuza.attack),
            '[BeforeDefence]', str(before_defence),
            '[AfterDefence]', str(base_yakuza.defence),
            '[SkillID]',  str(skill_ids[0]),
            '[BeforeSkillLv]',  str(before_skill_lvs[0]),
            '[SkillLv]',  str(skill_lvs[0]),
            '[Skill2ID]', str(skill_ids[1]),
            '[BeforeSkill2Lv]',  str(before_skill_lvs[1]),
            '[Skill2Lv]', str(skill_lvs[1]),
            '[Skill3ID]', str(skill_ids[2]),
            '[BeforeSkill3Lv]',  str(before_skill_lvs[2]),
            '[Skill3Lv]', str(skill_lvs[2]),
            )

        actionlog.write('YAKUZA_CONVERT_EXP', player.pk, record)


    @classmethod
    def use_item_log(cls, player, item, before_num, after_num, spend_num):
        '''
        アイテム使用
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            )

        actionlog.write('USE_ITEM', player.pk, record)

    @classmethod
    def use_item_for_event_log(cls, player, item, before_num, after_num, spend_num):

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            )

        actionlog.write('USE_EVENT_ITEM', player.pk, record)

    @classmethod
    def use_equipment_log(cls, player, item, player_yakuza, before_num, after_num, spend_num, before_attack, before_defence, before_equipment):
        '''
        装備品使用
        '''

        record = (
            '[EquipItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[PlayerYakuzaID]', str(player_yakuza.pk),
            '[YakuzaID]', str(player_yakuza.yakuza.pk),
            '[YakuzaName]', repr(player_yakuza.yakuza.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            '[BeforeAttack]', str(before_attack),
            '[AfterAttack]', str(player_yakuza.attack),
            '[BeforeDefence]', str(before_defence),
            '[AfterDefence]', str(player_yakuza.defence),
            '[BeforeEquipCount]', str(before_equipment),
            '[AfterEquipCount]', str(player_yakuza.equip_count),
        )

        actionlog.write('USE_EQUIPMENT', player.pk, record)

    @classmethod
    def use_unequipment_log(cls, player, player_yakuza, before_attack, before_defence, before_equipment):
        '''
        装備品解除
        '''

        record = (
            '[PlayerYakuzaID]', str(player_yakuza.pk),
            '[YakuzaID]', str(player_yakuza.yakuza.pk),
            '[YakuzaName]', repr(player_yakuza.yakuza.name),
            '[BeforeAttack]', str(before_attack),
            '[AfterAttack]', str(player_yakuza.attack),
            '[BeforeDefence]', str(before_defence),
            '[AfterDefence]', str(player_yakuza.defence),
            '[BeforeEquipCount]', str(before_equipment),
            '[AfterEquipCount]', str(player_yakuza.equip_count),
        )

        actionlog.write('USE_UNEQUIPMENT', player.pk, record)


    @classmethod
    def use_sniper_log(cls, player, item, item_count, player_gokujo, before_num, after_num, spend_num):
        '''
        罠使用
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[ItemCount]', str(item_count),
            '[GokujoID]', str(player_gokujo.gokujo.pk),
            '[GokujoName]', repr(player_gokujo.gokujo.name),
            '[StoryLevel]', str(player_gokujo.story_level),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
        )

        actionlog.write('USE_SNIPER', player.pk, record)

    @classmethod
    def use_vipticket_log(cls, player, item, before_num, after_num, spend_num):
        '''
        アイテム使用
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            )

        actionlog.write('USE_VIPTICKET', player.pk, record)

    @classmethod
    def use_item_office_log(cls, player, item, before_num, after_num, spend_num, before_office_num, after_office_num, add_office_num):
        '''
        アイテム使用
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            '[BeforeOfficeNum]', str(before_office_num),
            '[AfterOfficeNum]', str(after_office_num),
            '[AddOfficeNum]', str(add_office_num),
            )

        actionlog.write('USE_ITEM_OFFICE', player.pk, record)

    @classmethod
    def use_changeitem_log(cls, player, item, before_num, after_num, spend_num, assign_item):
        '''
        アイテム交換
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            '[ChangeItemID]', str(assign_item.id),
            )

        actionlog.write('CHANGE_ITEM', player.pk, record)

    @classmethod
    def use_special_log(cls, player, item, before_num, after_num, spend_num, before_rest, after_rest):
        '''
        必殺技使用
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            '[BeforeDurability]', str(before_rest),
            '[AfterDurability]', str(after_rest),
            )

        actionlog.write('USE_SPECIAL', player.pk, record)

    @classmethod
    def use_gachaticket_log(cls, player, item, before_num, after_num, spend_num):
        '''
        ガチャチケット使用
        '''

        record = (
            '[ItemID]', str(item.id),
            '[ItemName]', repr(item.name),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[SpendNum]', str(spend_num),
            )

        actionlog.write('USE_GACHATICKET', player.pk, record)


    @classmethod
    def error_gachaticket_log(cls, player, gacha):
        '''
        ガチャチケット使用エラーログ
        '''
        record = (
            '[GachaID]', str(gacha.pk),
            '[GachaTicketItemID]', str(gacha.ticket_item_id),
            )

        actionlog.write('ERROR_USE_GACHATICKET', player.pk, record)


    @classmethod
    def write_application_friend_log(cls, player, target_player):
        '''
        極友申請をした
        '''

        record = (
            '[TargetPlayerID]', str(target_player.pk),
            )

        actionlog.write('APP_FRIEND', player.pk, record)

    @classmethod
    def write_friend_application_and_accept_log(cls, player, target_player, before_point, after_point, point_now, before_player_max_power,after_player_max_power,before_target_player_max_power,after_target_player_max_power):
        '''
        極友申請をしたら、相手がすでに申請していたので極友になった
        '''

        record = (
            '[TargetPlayerID]', str(target_player.pk),
            '[BeforeComPoint]', str(before_point),
            '[AfterComPoint]', str(after_point),
            '[GetComPoint]', str(point_now),
            '[BeforePlayerMaxPower]', str(before_player_max_power),
            '[AfterPlayerMaxPower]', str(after_player_max_power),
            '[BeforeTargetPlayerMaxPower]', str(before_target_player_max_power),
            '[AfterTargetPlayerMaxPower]', str(after_target_player_max_power),
            )

        actionlog.write('FRIEND_APP_ACCEPT', player.pk, record)

    @classmethod
    def write_application_cancel_log(cls, player, target_player):
        '''
        極友申請をしたけどやっぱりやめた
        '''

        record = (
            '[TargetPlayerID]', str(target_player.pk),
            )

        actionlog.write('APP_CANCEL', player.pk, record)

    @classmethod
    def write_friend_accept_log(cls, player, target_player, before_point, after_point, point_now, before_player_max_power,after_player_max_power,before_target_player_max_power,after_target_player_max_power):
        '''
        極友申請を許可した
        '''

        record = (
            '[TargetPlayerID]', str(target_player.pk),
            '[BeforeComPoint]', str(before_point),
            '[AfterComPoint]', str(after_point),
            '[GetComPoint]', str(point_now),
            '[BeforePlayerMaxPower]', str(before_player_max_power),
            '[AfterPlayerMaxPower]', str(after_player_max_power),
            '[BeforeTargetPlayerMaxPower]', str(before_target_player_max_power),
            '[AfterTargetPlayerMaxPower]', str(after_target_player_max_power),
            )

        actionlog.write('FRIEND_ACCEPT', player.pk, record)

    @classmethod
    def write_friend_cancel_log(cls, player, target_player):
        '''
        極友申請を拒否した
        '''

        record = (
            '[TargetPlayerID]', str(target_player.pk),
            )

        actionlog.write('FRIEND_CANCEL', player.pk, record)

    @classmethod
    def write_friend_remove_log(cls, player, target_player, before_point, after_point, point_now, before_player_max_power,after_player_max_power,before_target_player_max_power,after_target_player_max_power):
        '''
        極友を解除した
        '''
        record = (
            '[TargetPlayerID]', str(target_player.pk),
            '[BeforeComPoint]', str(before_point),
            '[AfterComPoint]', str(after_point),
            '[GetComPoint]', str(point_now),
            '[BeforePlayerMaxPower]', str(before_player_max_power),
            '[AfterPlayerMaxPower]', str(after_player_max_power),
            '[BeforeTargetPlayerMaxPower]', str(before_target_player_max_power),
            '[AfterTargetPlayerMaxPower]', str(after_target_player_max_power),
            )

        actionlog.write('FRIEND_REMOVE', player.pk, record)

    @classmethod
    def write_get_loginbonus_log(cls, player, old_money, new_money, bonus_money, bonus_item, login_bonus_count):
        '''
        ログインボーナス取得
        '''

        record = (
            '[BeforeMoney]', str(old_money),
            '[AfterMoney]', str(new_money),
            '[GetMoney]', str(bonus_money),
            '[LoginBonusCount]', str(login_bonus_count),
            '[GetItemID]', str(bonus_item.pk) if bonus_item else '0',
            )

        actionlog.write('LOGIN_BONUS', player.pk, record)

    @classmethod
    def write_get_slotbonus_log(cls, player, slotbonus, num):
        '''
        スロットボーナス取得
        '''

        record = (
            '[SlotBonusID]', str(slotbonus.pk),
            '[SlotBonusNum]', str(num),
            )

        actionlog.write('SLOT_BONUS', player.pk, record)

    @classmethod
    def write_get_loginbonus_friend_money_log(cls, player, friend_num,  money, before_money, after_money):
        '''
        フレンドログインボーナス取得
        '''

        record = (
            '[FriendNum]', str(friend_num),
            '[GetMoney]', str(money),
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            )

        actionlog.write('LOGIN_BONUS_FRIEND_MONEY', player.pk, record)

    @classmethod
    def write_invitation_get_log(cls, player, invite_num, get_yakuza, get_item1, get_item2):
        '''
        招待インセンティブによる入手アイテム
        '''
        yakuza_id = 0
        yakuza_name = 'None'
        if get_yakuza:
            yakuza_id = get_yakuza.pk
            yakuza_name = get_yakuza.name

        item_id1 = 0
        item_name1 = 'None'
        if get_item1:
            item_id1 = get_item1.pk
            item_name1 = get_item1.name

        item_id2 = 0
        item_name2 = 'None'
        if get_item2:
            item_id2 = get_item2.pk
            item_name2 = get_item2.name

        record = (
            '[PlayerID]', str(player.pk),
            '[InviteCount]', str(invite_num),
            '[YakuzaID]', str(yakuza_id),
            '[YakuzaName]', repr(yakuza_name),
            '[ItemID1]', str(item_id1),
            '[ItemName1]', repr(item_name1),
            '[ItemID2]', str(item_id2),
            '[ItemName2]', repr(item_name2),
            )

        actionlog.write('INVITATION_LOG', player.pk, record)

    @classmethod
    def write_invite_log(cls, player, invite_count):
        '''
        招待ログ
        '''

        record = (
            '[InviteCount]', str(invite_count),
            )

        actionlog.write('IN_GAME_INVITE', player.pk, record)

    @classmethod
    def write_invite_list_log(cls, player, invite_list):
        '''
        招待した人リスト
        '''

        record = (
            '[InviteMembers]', str(invite_list),
            )

        actionlog.write('IN_GAME_INVITE_LIST', player.pk, record)

    @classmethod
    def write_invitation_invite_log(cls, player, invite_num, get_yakuza, get_item1, get_item2):
        '''
        単純招待数によるインセンティブ
        '''
        yakuza_id = 0
        yakuza_name = 'None'
        if get_yakuza:
            yakuza_id = get_yakuza.pk
            yakuza_name = get_yakuza.name

        item_id1 = 0
        item_name1 = 'None'
        if get_item1:
            item_id1 = get_item1.pk
            item_name1 = get_item1.name

        item_id2 = 0
        item_name2 = 'None'
        if get_item2:
            item_id2 = get_item2.pk
            item_name2 = get_item2.name

        record = (
            '[PlayerID]', str(player.pk),
            '[InviteCount]', str(invite_num),
            '[YakuzaID]', str(yakuza_id),
            '[YakuzaName]', repr(yakuza_name),
            '[ItemID1]', str(item_id1),
            '[ItemName1]', repr(item_name1),
            '[ItemID2]', str(item_id2),
            '[ItemName2]', repr(item_name2),
            )

        actionlog.write('INVITATION_LOG', player.pk, record)


    @classmethod
    def write_gokujo_rescue_log(cls, player, rescue_count):
        '''
        極女を救い出してプレゼントをいただいた
        '''

        record = (
            '[RescueCount]', str(rescue_count),
            )

        actionlog.write('GOKUJO_RESCUE', player.pk, record)

    @classmethod
    def write_add_money_log(cls, player, money, before_money, after_money):
        '''
        お金獲得
        '''

        record = (
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[Money]', str(money),
            )

        actionlog.write('ADD_MONEY', player.pk, record)

    @classmethod
    def write_consume_money_log(cls, player, money, before_money, after_money):
        '''
        お金消費
        '''

        record = (
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[Money]', str(money),
            )

        actionlog.write('CONSUME_MONEY', player.pk, record)


    @classmethod
    def write_add_medal_log(cls, player, medal, before_medal, after_medal):
        '''
        メダル獲得
        '''

        record = (
            '[BeforeMedal]', str(before_medal),
            '[AfterMedal]', str(after_medal),
            '[Medal]', str(medal),
            )

        actionlog.write('ADD_MEDAL', player.pk, record)

    @classmethod
    def write_consume_medal_log(cls, player, medal, before_medal, after_medal):
        '''
        メダル消費
        '''

        record = (
            '[BeforeMedal]', str(before_medal),
            '[AfterMedal]', str(after_medal),
            '[Medal]', str(medal),
            )

        actionlog.write('CONSUME_MEDAL', player.pk, record)


    @classmethod
    def use_medal_item_log(cls, player, before_num, after_num, use_item_name):
        '''
        メダルアイテム使用
        '''

        record = (
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            '[ItemName]', repr(use_item_name),
            )

        actionlog.write('USE_MEDAL_ITEM', player.pk, record)

    @classmethod
    def write_trade_is_start_log(cls, player, player_trade):
        '''
        '''

        record = (
            '[PlayerTradeID]', str(player_trade.pk),
            '[FromPlayerID]', str(player_trade.from_player_id),
            '[ToPlayerID]', str(player_trade.to_player_id),
            )

        actionlog.write('TRADE_IS_START', player.pk, record)


    @classmethod
    def write_trade_is_apply_log(cls, player, player_trade, from_entrys):
        '''
        '''
        from trade.trade_util import get_object
        from common.static_values import StaticValues

        record = [
            '[PlayerTradeID]', str(player_trade.pk),
            '[FromPlayerID]', str(player_trade.from_player_id),
            '[ToPlayerID]', str(player_trade.to_player_id),
            ]

        for i,o in enumerate(from_entrys):
            record.append('[FROM_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[FROM_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[FROM_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[FROM_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        actionlog.write('TRADE_IS_APPLY', player.pk, record)


    @classmethod
    def write_trade_is_accept_log(cls, player, player_trade, from_entrys, to_entrys):
        '''
        '''
        from trade.trade_util import get_object
        from common.static_values import StaticValues

        record = [
            '[PlayerTradeID]', str(player_trade.pk),
            '[FromPlayerID]', str(player_trade.from_player_id),
            '[ToPlayerID]', str(player_trade.to_player_id),
            ]

        for i,o in enumerate(from_entrys):
            record.append('[FROM_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[FROM_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[FROM_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[FROM_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        for i,o in enumerate(to_entrys):
            record.append('[TO_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[TO_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[TO_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[TO_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        actionlog.write('TRADE_IS_ACCEPT', player.pk, record)


    @classmethod
    def write_trade_is_birth_log(cls, player, player_trade, from_entrys, to_entrys):
        '''
        '''
        from trade.trade_util import get_object
        from common.static_values import StaticValues

        record = [
            '[PlayerTradeID]', str(player_trade.pk),
            '[FromPlayerID]', str(player_trade.from_player_id),
            '[ToPlayerID]', str(player_trade.to_player_id),
            ]

        for i,o in enumerate(from_entrys):
            record.append('[FROM_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[FROM_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[FROM_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[FROM_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        for i,o in enumerate(to_entrys):
            record.append('[TO_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[TO_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[TO_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[TO_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        actionlog.write('TRADE_IS_BIRTH', player.pk, record)


    @classmethod
    def write_trade_is_finish_log(cls, player, player_trade, from_entrys, to_entrys):
        '''
        '''
        from trade.trade_util import get_object
        from common.static_values import StaticValues

        record = [
            '[PlayerTradeID]', str(player_trade.pk),
            '[FromPlayerID]', str(player_trade.from_player_id),
            '[ToPlayerID]', str(player_trade.to_player_id),
            ]

        for i,o in enumerate(from_entrys):
            record.append('[FROM_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[FROM_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[FROM_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[FROM_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        for i,o in enumerate(to_entrys):
            record.append('[TO_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[TO_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[TO_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[TO_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')

        actionlog.write('TRADE_IS_FINISH', player.pk, record)


    @classmethod
    def write_trade_is_cancel_log(cls, player, player_trade, from_entrys, to_entrys):
        '''
        '''
        from trade.trade_util import get_object
        from common.static_values import StaticValues

        record = [
            '[PlayerTradeID]', str(player_trade.pk),
            '[TradeStatus]', str(player_trade.status),
            '[FromPlayerID]', str(player_trade.from_player_id),
            '[ToPlayerID]', str(player_trade.to_player_id),
            ]

        for i,o in enumerate(from_entrys):
            record.append('[FROM_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[FROM_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[FROM_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[FROM_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')
        if not from_entrys:
            record.append('[FromEntry]')
            record.append('Nothing')

        for i,o in enumerate(to_entrys):
            record.append('[TO_ARTICLE_TYPE%d]' % (i+1))
            record.append(str(o.article_type))
            record.append('[TO_ARTICLE_KEY%d]' % (i+1))
            record.append(str(o.article_key))
            record.append('[TO_ARTICLE_VALUE%d]' % (i+1))
            record.append(str(o.article_value))
            record.append('[TO_ARTICLE_YAKUZA_ID%d]' % (i+1))# PlayerYakuzaの場合、YakuzaIDを表示する
            if int(o.article_type) == StaticValues.TYPE_CARD:
                obj = get_object(int(o.article_type), int(o.article_key), int(o.article_value))
                if obj:
                    record.append(str(obj.yakuza_id))
                else:
                    record.append('PlayerYakuzaNotFound')
            else:
                record.append('NotYakuza')
        if not to_entrys:
            record.append('[ToEntry]')
            record.append('Nothing')

        actionlog.write('TRADE_IS_CANCEL', player.pk, record)


    @classmethod
    def write_article_add_log(cls, player, player_trade, article_type, article, before_num, after_num):
        '''
        トレード品をプレイヤーから取り上げた
        '''
        from common.static_values import StaticValues
        from yakuza.models import PlayerYakuza
        from item.models import PlayerItem

        add_record_yakuza = None
        add_record_item = None

        if article_type == StaticValues.TYPE_CARD:
            article = article.pk
            add_record_yakuza = str(PlayerYakuza.get(article).get_yakuza().pk)
        elif article_type == StaticValues.TYPE_ITEM:
            article = article.pk
            add_record_item = str(PlayerItem.get(article).get_item().pk)
        elif article_type == StaticValues.TYPE_MONEY or article_type == StaticValues.TYPE_MEDAL:
            pass
        else:
            article = u'None'

        record = (
            '[PlayerTradeID]', str(player_trade.pk),
            '[TargetPlayerID]', str(player.pk),
            '[ArticleType]', str(article_type),
            '[ArticleValue]', str(article),
            '[ArticleYakuzaID]', str(add_record_yakuza),
            '[ArticleItemID]', str(add_record_item),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            )

        actionlog.write('TRADE_ARTICLE_REFISTRATION_ADD', player.pk, record)


    @classmethod
    def write_article_delete_log(cls, player, player_trade, article_type, article, before_num, after_num):
        '''
        トレード品をプレイヤーに返却
        '''
        from common.static_values import StaticValues
        from yakuza.models import PlayerYakuza
        from item.models import PlayerItem

        add_record_yakuza = None
        add_record_item = None

        if article_type == StaticValues.TYPE_CARD:
            article = article.pk
            add_record_yakuza = str(PlayerYakuza.get(article).get_yakuza().pk)
        elif article_type == StaticValues.TYPE_ITEM:
            article = article.pk
            add_record_item = str(PlayerItem.get(article).get_item().pk)
        elif article_type == StaticValues.TYPE_MONEY or article_type == StaticValues.TYPE_MEDAL:
            pass
        else:
            article = u'None'

        record = (
            '[PlayerTradeID]', str(player_trade.pk),
            '[TargetPlayerID]', str(player.pk),
            '[ArticleType]', str(article_type),
            '[ArticleValue]', str(article),
            '[ArticleYakuzaID]', str(add_record_yakuza),
            '[ArticleItemID]', str(add_record_item),
            '[BeforeNum]', str(before_num),
            '[AfterNum]', str(after_num),
            )

        actionlog.write('TRADE_ARTICLE_REFISTRATION_DELETE', player.pk, record)


    @classmethod
    def compose_evolution_log(cls, player, evolution_yakuza, base_yakuza, args, equip_attack, equip_defence, equip_count, composition_type):
        '''
        進化合成

        合成種別
        1 : CompositionTypeGrow(通常合成)
        2 : CompositionTypeEvolution(進化覚醒)
        3 : CompositionTypeEvolutionByLady(女極道の覚醒入魂)
        4 : CompositionTypeEvolutionByRaritySR(Sﾚｱの覚醒入魂)
        '''

        record = [
            '[EvolutionYakuzaID]', str(evolution_yakuza.get_yakuza().pk),
            '[EvolutionYakuzaName]', repr(evolution_yakuza.get_yakuza().name),
            '[EvolutionYakuzaEquipAttack]', repr(evolution_yakuza.equip_attack),
            '[EvolutionYakuzaEquipDefence]', repr(evolution_yakuza.equip_defence),
            '[EvolutionYakuzaEquipCount]', repr(evolution_yakuza.equip_count),
            '[BaseYakuzaID]', str(base_yakuza.get_yakuza().pk),
            '[BaseYakuzaName]', repr(base_yakuza.get_yakuza().name),
            '[BaseEquipAttack]', str(equip_attack),
            '[BaseEquipDefence]', str(equip_defence),
            '[BaseEquipCount]', str(equip_count),
            '[CompositionType]', str(composition_type)
            ]
        for o in args:
            record.append('[MaterialYakuzaID]')
            record.append(str(o.get_yakuza().pk))
            record.append('[MaterialYakuzaName]')
            record.append(repr(o.get_yakuza().name))

        actionlog.write('COMPOSE_EVOLUTION', player.pk, record)

    @classmethod
    def use_rare_mixer_log(cls, player, delete_yakuza_name_1, delete_yakuza_name_2):
        '''
        レアミキサー使用
        '''

        record = (
            '[DeleteYakuzaName1]', repr(delete_yakuza_name_1),
            '[DeleteYakuzaName2]', repr(delete_yakuza_name_2),
            )

        actionlog.write('USE_RARE_MIXER', player.pk, record)

    @classmethod
    def write_charge_medal_log(cls, player, shatei_list, before_medals, medals, after_medals):
        '''
        舎弟をメダルに交換する
        '''

        record = [
            '[BeforeMedal]', str(before_medals),
            '[GetMedal]', str(medals),
            '[AfterMedal]', str(after_medals),
            ]
        for i,o in enumerate(shatei_list):
            record.append('[DELETE_SHATEI_%d]' % (i+1))
            record.append(str(o.pk))
            record.append('[DELETE_SHATEI_%d_YAKUZA_ID]' % (i+1))
            record.append(str(o.yakuza_id))
            record.append('[DELETE_SHATEI_%d_YAKUZA_NAME]' % (i+1))
            record.append(repr(o.get_yakuza().name))

        actionlog.write('CHARGE_MEDAL', player.pk, record)

    @classmethod
    def write_medal_yakuzaequip_mixer_log(cls, player, delete1, delete2, present):
        '''
        装備ミキサーのログ（汎用的じゃねぇ〜））
        '''
        record = [
            '[DeleteEquipmentA]', str(delete1.equipment.pk),
            '[DeleteEquipmentB]', str(delete2.equipment.pk),
            '[PresentEquipment]', str(present.pk),
            ]
        actionlog.write('YAKUZAEQUIP_MIXER', player.osuser_id, record)

    @classmethod
    def write_exchange_medal_log(cls, player, cost, medal_master, entrys):
        '''
        メダルを景品に交換する
        '''

        record = [
            '[MedalCost]', str(cost),
            '[MedalMasterID]', str(medal_master.pk),
            ]
        for i,o in enumerate(entrys):
            record.append('[GET_ENTRY_TYPE]')
            if o.is_item:
                record.append("ITEM")
            elif o.is_yakuza:
                record.append("YAKUZA")
            elif o.is_instant:
                record.append("INSTANT")
            elif o.is_box:
                record.append("BOX")
            elif o.is_yakuzaequip:
                record.append("YAKUZAEQUIP")

            if o.is_instant:
                record.append('[USE_EFFECT_%d]' % (i+1))
                record.append(str(o.article))
                record.append('[EFFECT_NUM_%d]' % (i+1))
                record.append(repr(o.effect_num))
            elif o.is_box:
                pass
            else:
                record.append('[GET_ENTRY_%d_ID]' % (i+1))
                record.append(str(o.article.pk))
                record.append('[DELETE_SHATEI_%d_NAME]' % (i+1))
                record.append(repr(o.article_name))

        actionlog.write('EXCHANGE_MEDAL', player.pk, record)


    @classmethod
    def write_exchange_medal_mixer_banuser_log(cls, player):
        '''
        メダル利用禁止ユーザーがメダルミキサーを利用したログ
        '''

        record = (
            '[Player]', str(player.osuser_id),
            )

        actionlog.write('WRITE_EXCHANGE_MEADL_MIXER_BANUSER', player.osuser_id, record)


    @classmethod
    def write_kaizoku_incnetive_log(cls, player, inflow_id, outflow_id, course_id, result):
        '''
        任侠　→　海賊誘導インセンティブ用ログ
        '''

        record = (
            '[Player]', str(player.osuser_id),
            '[Outflow_Id]', str(outflow_id),
            '[Inflow_Id]', str(inflow_id),
            '[Course_Id]', str(course_id),
            '[result]', str(result),
            )

        actionlog.write('WRITE_KAIZOKU_INCENTIVE', player.osuser_id, record)

    @classmethod
    def write_battle_gacha_heavens_log(cls, player, action, lottery_time, finish_time, stop_time):
        '''
        BATTLE_GACHAの天国モード時間制御のログ
        '''

        if finish_time:
            finish_time = finish_time.strftime('%Y/%m/%d %H:%M:%S')

        if stop_time:
            stop_time = stop_time.strftime('%Y/%m/%d %H:%M:%S')

        record = (
            '[Player]', str(player.osuser_id),
            '[Action]', action,
            '[Lottery_time]', str(lottery_time),
            '[Finish_time]', str(finish_time),
            '[Stop_time]', str(stop_time),
            )

        actionlog.write('BATTLE_GACHA_HEAVENS', player.osuser_id, record)

    @classmethod
    def write_viptime_log(cls, player, action, vip_time, finish_time, stop_time):
        '''
        VIPTIMEの時間制御のログ
        '''

        if finish_time:
            finish_time = finish_time.strftime('%Y/%m/%d %H:%M:%S')

        if stop_time:
            stop_time = stop_time.strftime('%Y/%m/%d %H:%M:%S')

        record = (
            '[Player]', str(player.osuser_id),
            '[Action]', action,
            '[Vip_time]', str(vip_time),
            '[Finish_time]', str(finish_time),
            '[Stop_time]', str(stop_time),
            )

        actionlog.write('VIPTIME', player.osuser_id, record)

    @classmethod
    def write_bigtime_log(cls, player, action, vip_time, finish_time, stop_time):
        '''
        BIGTIMEの時間制御のログ
        '''

        if finish_time:
            finish_time = finish_time.strftime('%Y/%m/%d %H:%M:%S')

        if stop_time:
            stop_time = stop_time.strftime('%Y/%m/%d %H:%M:%S')

        record = (
            '[Player]', str(player.osuser_id),
            '[Action]', action,
            '[Vip_time]', str(vip_time),
            '[Finish_time]', str(finish_time),
            '[Stop_time]', str(stop_time),
            )

        actionlog.write('BIGTIME', player.osuser_id, record)


    @classmethod
    def write_exchange_event_point_log(cls, player, game_event, event_point, present_type, present, num, before_point, after_point):
        '''
        イベントポイントを報酬に交換する
        '''
        type = int(present_type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = present
            present_name = 'communication_point'
        elif type == 6:
            present_id = present
            present_name = 'medal'
        elif present:
            present_id = present.pk
            present_name = present.name
        else:
            present_id = 0
            present_name = "None"
        record = (
            '[GameEventId]', str(game_event.id),
            '[EventPoint]', str(event_point),
            '[PresentType]', str(present_type),
            '[PresentId]', str(present_id),
            '[PresentName]', repr(present_name),
            '[Num]', str(num),
            '[BeforePoint]', str(before_point),
            '[AfterPoint]', str(after_point),
            )
        actionlog.write('EXCHANGE_EVENT_POINT', player.pk, record)

    @classmethod
    def write_exchange_event_point_by_id_log(cls, player, game_event, event_point, event_point_reward_id, present_type, present, num, before_point, after_point):
        '''
        報酬IDを指定してイベントポイントを報酬に交換する
        '''
        type = int(present_type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = present
            present_name = 'communication_point'
        elif type == 6:
            present_id = present
            present_name = 'medal'
        elif present:
            present_id = present.pk
            present_name = present.name
        else:
            present_id = 0
            present_name = "None"
        record = (
            '[GameEventId]', str(game_event.id),
            '[EventPoint]', str(event_point),
            '[EventPointRewardId]', str(event_point_reward_id),
            '[PresentType]', str(present_type),
            '[PresentId]', str(present_id),
            '[PresentName]', repr(present_name),
            '[Num]', str(num),
            '[BeforePoint]', str(before_point),
            '[AfterPoint]', str(after_point),
            )
        actionlog.write('EXCHANGE_EVENT_POINT_BY_ID', player.pk, record)


    @classmethod
    def write_give_reward_event_point_log(cls, player, game_event, event_point, present_type, present, num, old_event_point, new_event_point):
        '''
        イベントポイントを報酬に交換する
        '''
        type = int(present_type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = present
            present_name = 'communication_point'
        elif type == 6:
            present_id = present
            present_name = 'medal'
        elif present:
            present_id = present.pk
            present_name = present.name
        else:
            present_id = 0
            present_name = "None"
        record = (
            '[GameEventId]', str(game_event.id),
            '[EventPoint]', str(event_point),
            '[PresentType]', str(present_type),
            '[PresentId]', str(present_id),
            '[PresentName]', repr(present_name),
            '[Num]', str(num),
            '[OldEventPoint]', str(old_event_point),
            '[NewEventPoint]', str(new_event_point),
            )
        actionlog.write('GIVE_REWARD_EVENT_POINT', player.pk, record)


    @classmethod
    def write_karuta_send_message_log(cls, player, receive_player_ids, send_id, old_point, new_point, get_point):
        '''
        カルタの送信ログ
        '''
        record = (
            '[SendPlayerId]', str(player.osuser_id),
            '[ReceivePlayerIds]', str(receive_player_ids),
            '[SendId]', str(send_id),
            '[OldPoint]', str(old_point),
            '[NewPoint]', str(new_point),
            '[GetPoint]', str(get_point),
            )
        actionlog.write('KARUTA_SEND_MESSAGE', player.osuser_id, record)


    @classmethod
    def write_karuta_receive_message_log(cls, player, send_player_id, send_id, old_point, new_point, get_point, get_money):
        '''
        カルタの受信ログ
        '''
        record = (
            '[ReceivePlayer]', str(player.osuser_id),
            '[SendPlayer]', str(send_player_id),
            '[SendId]', str(send_id),
            '[OldPoint]', str(old_point),
            '[NewPoint]', str(new_point),
            '[GetPoint]', str(get_point),
            '[GetMoney]', str(get_money),
            )
        actionlog.write('KARUTA_RECEIVE_MESSAGE', player.osuser_id, record)


    @classmethod
    def write_karuta_receive_unreceived_message_log(cls, player, num, sec):
        '''
        カルタの一括受信ログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[Num]', str(num),
            '[Sec]', str(sec),
            )
        actionlog.write('KARUTA_RECEIVE_UNRECEIVED_MESSAGE', player.osuser_id, record)


    @classmethod
    def write_karuta_receive_comp_reward_log(cls, player, picture_id, yakuza_number):
        '''
        カルタのコンプ報酬受け取りログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[PictureId]', str(picture_id),
            '[YakuzaNumber]', str(yakuza_number),
            )
        actionlog.write('KARUTA_RECEIVE_COMP_REWARD', player.osuser_id, record)


    @classmethod
    def write_karuta_receive_wallpaper_log(cls, player, picture_id, resolution):
        '''
        カルタの完成トレカ受け取りログ
        ※見られたかどうかだけで判断なので、集計時にユニークをとらんといけない
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[PictureId]', str(picture_id),
            '[Resolution]', str(resolution),
            )
        actionlog.write('KARUTA_RECEIVE_WALLPAPER', player.osuser_id, record)

    @classmethod
    def write_karuta_forced_requestid_log(cls, player, request_id, friend_player_ids):
        '''
        トレカリクエスト送信時にGREEでrequest_idが付与されなかった場合に、
        アプリ側で強制的にIDを付与したログ
        '''
        record = (
            '[SendPlayer]', str(player.osuser_id),
            '[RequestId]', str(request_id),
            '[TargetFriends]', str(",".join([str(v) for v in friend_player_ids])),
            )
        actionlog.write('KARUTA_FORCED_REQUEST_ID', player.osuser_id, record)

    @classmethod
    def write_karuta_send_not_auth_log(cls, player, send_player_id, receive_player_id):
        '''
        トレカで未認証のためギフトを送れなかったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            )

        actionlog.write('KARUTA_SEND_NOT_AUTH', player.osuser_id, record)

    @classmethod
    def write_comeback_log(cls, player, last_login_at, day):
        '''
        復帰キャンペーン、何日目かの報償を貰った
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[LastLogin]', str(last_login_at),
            '[Day]', str(day),
            )
        actionlog.write('COMEBACK', player.osuser_id, record)


    @classmethod
    def write_cabaret_receive_fullcomp_reward_log(cls, player, yakuza_number):
        '''
        ノックアウトラブのフルコンプ報酬受け取りログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[YakuzaNumber]', str(yakuza_number),
            )
        actionlog.write('CABARET_RECEIVE_FULLCOMP_REWARD', player.osuser_id, record)


    @classmethod
    def write_cabaret_force_encounter_stalker_log(cls, player, stalker_no):
        '''
        ノックアウトラブの直電したログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[StalkerNo]', str(stalker_no),
            )
        actionlog.write('CABARET_FORCE_ENCOUNTER_STALKER', player.osuser_id, record)


    @classmethod
    def write_cabaret_battle_stalker_win_log(cls, player, stalker_no, old_point, old_heart, is_comp, got_point, new_point):
        '''
        ノックアウトラブの勝利したログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[StalkerNo]', str(stalker_no),
            '[old_point]',str(old_point),
            '[old_heart]',str(old_heart),
            '[is_comp]',str(is_comp),
            '[got_point]',str(got_point),
            '[new_point]',str(new_point),
            )
        actionlog.write('CABARET_BATTLE_STALKER_WIN', player.osuser_id, record)


    @classmethod
    def write_cabaret_battle_stalker_lose_log(cls, player, stalker_no, current_point):
        '''
        ノックアウトラブの敗北したログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[StalkerNo]', str(stalker_no),
            '[CurrentPoint]', str(current_point),
            )
        actionlog.write('CABARET_BATTLE_STALKER_LOSE', player.osuser_id, record)


    @classmethod
    def write_received_reward_log(cls, player, meta, player_reward):
        '''
        報酬受取のログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[ClassName]', str(meta),
            '[PlayerRewardID]', str(player_reward.id),
            '[RewardName]', repr(player_reward.reward.name),
            )
        actionlog.write('RECEIVED_REWARD', player.osuser_id, record)


    @classmethod
    def write_use_serial_log(cls, player, promo, serial):
        '''
        シリアル利用ログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[PromoID]', str(promo.id),
            '[Serial]', str(serial),
            )
        actionlog.write('USE_SERIAL', player.osuser_id, record)

    @classmethod
    def write_delete_yakuza_log(cls, player_yakuza):
        '''
        PlayerYakuza削除ログ
        '''

        record = (
            '[PlayerID]', str(player_yakuza.player_id),
            '[PlayerYakuzaID]', str(player_yakuza.pk),
            '[YakuzaID]', str(player_yakuza.yakuza_id),
            '[Level]', str(player_yakuza.level),
            '[Exp]', str(player_yakuza.exp),
            '[Attack]', str(player_yakuza.attack),
            '[Defence]', str(player_yakuza.defence),
            '[EquipAttack]', str(player_yakuza.equip_attack),
            '[EquipDefence]', str(player_yakuza.equip_defence),
            '[EquipCount]', str(player_yakuza.equip_count),
            '[SkillID]', str(player_yakuza.skill_id) if player_yakuza.skill else '0',
            '[SkillLevel]', str(player_yakuza.skill_level),
            '[CreatedAt]', str(player_yakuza.created_at),
            '[UpdatedAt]', str(player_yakuza.updated_at),
            )
        actionlog.write('DELETE_YAKUZA', player_yakuza.player_id, record)

    @classmethod
    def write_pre_boss_battle_result_log(cls, player, place_id, success, use_count):
        '''
        ボスと戦った
        '''

        record = (
            '[BossID]', str(place_id),
            '[Success]', str(success),
            '[ItemID]', '1',
            '[SpendNum]', str(use_count),
            )

        actionlog.write('PRE_BOSS_RESULT', player.pk, record)

    @classmethod
    def write_stalker_pre_boss_battle_result_log(cls, player, stalker_id, success, use_count):
        '''
        ボスと戦った
        '''

        record = (
            '[StalkerID]', str(stalker_id),
            '[Success]', str(success),
            '[ItemID]', '1',
            '[SpendNum]', str(use_count),
            )

        actionlog.write('PRE_BOSS_RESULT_STALKER', player.pk, record)

    @classmethod
    def write_pre_boss_battle_result_tokonatsu_log(cls, player, place_id, success, boss_hp, max_boss_hp):
        '''
        ボスと戦った（常夏）
        '''

        record = (
            '[BossID]', str(place_id),
            '[Success]', str(success),
            '[ItemID]', '1',
            '[BossHP]', str(boss_hp),
            '[MaxBossHP]', str(max_boss_hp),
            )

        actionlog.write('PRE_BOSS_RESULT_ONI', player.pk, record)

    @classmethod
    def write_gacha_srot_result_log(cls, player, gacha_srot_osuser_id, srot_counter, is_chancebonus, chancebonus_counter, chancebonus_point, srot_result_one, srot_result_two, srot_result_threeunko):
        '''
        ガチャスロットの結果ログ
        '''

        record = (
            '[Gacha_Srot_Osuser_Id]', str(gacha_srot_osuser_id),
            '[Srot_Counter]', str(srot_counter),
            '[Is_Chancebonus]', str(is_chancebonus),
            '[Chancebonus_Counter]', str(chancebonus_counter),
            '[Chancebonus_Point]', str(chancebonus_point),
            '[Srot_Result_One]', str(srot_result_one),
            '[Srot_Result_Two]', str(srot_result_two),
            '[Srot_Result_Threeunko]', str(srot_result_threeunko),
        )

        actionlog.write('GACHA_SROT', player.pk, record)

    @classmethod
    def write_gacha_srot_bonus_point_log(cls, player, before_point, after_point, add_point, is_reward):
        '''
        ガチャスロットのボーナスポイントログ
        '''

        record = (
            '[Add_Point_Osuser_Id]', str(player.osuser_id),
            '[Before_Pint]', str(before_point),
            '[After_Point]', str(after_point),
            '[Add_Point]', str(add_point),
            '[Is_Reward]', str(is_reward),
        )

        actionlog.write('GACHA_SROT_BONUS_POINT', player.pk, record)

    @classmethod
    def write_signal_fire_log(cls, player):
        '''
        のろしをあげたログ
        '''

        record = (
            '[PlaceID]', str(player.event_tokonatsu.normal_floor_id),
            )

        actionlog.write('SIGNAL_FIRE', player.pk, record)

    @classmethod
    def write_rescue_signal_fire_log(cls, player, target_player):
        '''
        のろしをすくい上げたログ
        '''

        record = (
            '[PlaceID]', str(player.event_tokonatsu.normal_floor_id),
            '[TargetPlayerID]', str(target_player.pk),
            '[TargetPlayerPlaceID]', str(target_player.event_tokonatsu.normal_floor_id),
            )

        actionlog.write('RESCUE_SIGNAL_FIRE', player.pk, record)

    @classmethod
    def write_repair_error_place_log(cls, player, place_id):
        '''
        おかしなデータを修正したログ
        '''

        record = (
            '[PlaceID]', str(place_id),
            )

        actionlog.write('REPAIR_ERROR_PLACE', player.pk, record)

    @classmethod
    def write_raid_walk_log(cls, player, before_exp, after_exp, exp, before_money, after_money, money, before_power, after_power, power, before_achievement_level, after_achievement_level, achievement_level, pop_npc, raid_boss_battle, before_point, after_point, point):
        """
        地回りしたログ
        """

        record = (
            '[BeforeExp]', str(before_exp),
            '[AfterExp]', str(after_exp),
            '[GetExp]', str(exp),
            '[BeforeMoney]', str(before_money),
            '[AfterMoney]', str(after_money),
            '[GetMoney]', str(money),
            '[BeforePower]', str(before_power),
            '[AfterPower]', str(after_power),
            '[ConsumePower]', str(power),
            '[BeforeAchievementLevel]', str(before_achievement_level),
            '[AfterAchievementLevel]', str(after_achievement_level),
            '[AddAchievementLevel]', str(achievement_level),
            '[NpcClass]', str(pop_npc.__class__.__name__),
            '[NpcID]', str(pop_npc.pk) if pop_npc else 'None',
            '[RaidBossBattle]', str(raid_boss_battle.pk) if raid_boss_battle else 'None',
            '[BeforeCryptidPoint]', str(before_point),
            '[AfterCryptidPoint]', str(after_point),
            '[CryptidPoint]', str(point),
            )

        actionlog.write('RAID_WALK', player.pk, record)

    @classmethod
    def write_raid_join_log(cls, player, battle):
        '''
        レイドバトルをジョインログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[BattleId]', str(battle.pk),
            )
        actionlog.write('RAID_BATTLE_JOIN', player.osuser_id, record)

    @classmethod
    def write_raid_leave_log(cls, player, battle):
        '''
        レイドバトルを逃げるログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[BattleId]', str(battle.pk),
            )
        actionlog.write('RAID_BATTLE_LEAVE', player.osuser_id, record)

    @classmethod
    def write_raid_point_rewarded_log(cls, player, battle, points_rewarded):
        '''
        レイドのポイント割り当てログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[BattleId]', str(battle.pk),
            '[PointsRewarded]', str(points_rewarded),
            )
        actionlog.write('RAID_BATTLE_POINTS_REWARDED', player.osuser_id, record)

    @classmethod
    def write_raid_point_received_log(cls, player, battle, points_received, prev_points, after_points):
        '''
        レイドのポイント受けログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[BattleId]', str(battle.pk),
            '[PointsReceived]', str(points_received),
            '[PrevPoints]', str(prev_points),
            '[AfterPoints]', str(after_points),
            )
        actionlog.write('RAID_BATTLE_POINTS_RECEIVED', player.osuser_id, record)

    @classmethod
    def write_consume_event_hp_log(cls, player_id, before_hp, after_hp, consume_hp):
        '''
        イベントHPを消費したログ
        '''

        record = (
            '[BeforeHp]', str(before_hp),
            '[AfterHp]', str(after_hp),
            '[ConsumeHp]', str(consume_hp),
        )

        actionlog.write('CONSUME_EVENT_HP', player_id, record)

    @classmethod
    def write_raid_battle_log(cls, player, battle, boss_level, attack, defence, old_hp, old_hp_enemy, new_hp, new_hp_enemy):
        '''
        レイドバトル（１回）ログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[BattleId]', str(battle.pk),
            '[BossLevel]', str(boss_level),
            '[Attack]',str(attack),
            '[Defence]',str(defence),
            '[OldHp]',str(old_hp),
            '[OldHpEnemy]',str(old_hp_enemy),
            '[NewHp]',str(new_hp),
            '[NewHpEnemy]',str(new_hp_enemy),
            )
        actionlog.write('RAID_BATTLE_TURN', player.osuser_id, record)

    @classmethod
    def write_applink_insentive_received_log(cls, player, item_type, item, count):
        '''
        アプリ間リンクもらったもの
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[item_type]', str(item_type),
            '[item]', str(item),
            '[count]', str(count),
            )
        actionlog.write('APPLINK_INSENTIVE_RECEIVED', player.osuser_id, record)

    @classmethod
    def write_harem_battle_stalker_win_log(cls, player, deck_id, is_attack, partner_id, old_point, got_point, new_point, num_straight_wins):
        '''
        ハーレムの勝利したログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[DeckId]', str(deck_id),
            '[IsAttack]', str(is_attack),
            '[NumStraightWins]', str(num_straight_wins),
            '[PartnerId]', str(partner_id),
            '[old_point]',str(old_point),
            '[got_point]',str(got_point),
            '[new_point]',str(new_point),
            )
        actionlog.write('HAREM_BATTLE_STALKER_WIN', player.osuser_id, record)


    @classmethod
    def write_harem_battle_stalker_lose_log(cls, player, deck_id, is_attack, partner_id, old_point, got_point, new_point, num_straight_wins):
        '''
        ハーレムの敗北したログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[DeckId]', str(deck_id),
            '[IsAttack]', str(is_attack),
            '[NumStraightWins]', str(num_straight_wins),
            '[PartnerId]', str(partner_id),
            '[old_point]',str(old_point),
            '[got_point]',str(got_point),
            '[new_point]',str(new_point),
            )
        actionlog.write('HAREM_BATTLE_STALKER_LOSE', player.osuser_id, record)

    @classmethod
    def write_event_harem_log(cls, player, player_attack, target_player, target_player_defence, friend_player, friend_player_attack, is_win_attack, is_win_defence, old_pt, new_pt, reward_item_id, num_straight_wins):
        '''
        ハーレムイベントバトルログ
        '''

        is_friend = False
        friend_player_pk = None
        friend_player_name = None
        friend_player_level = None
        if friend_player:
            is_friend = True
            friend_player_pk = friend_player.pk
            friend_player_name = friend_player.name
            friend_player_level = friend_player.level

        record = (
                '[PlayerLevel]', str(player.level),
                '[TargetPlayerPk]', str(target_player.pk),
                '[TargetPlayerLevel]', str(target_player.level),
                '[Is_Friend]', str(is_friend),
                '[FriendPk]', str(friend_player_pk),
                '[FriendName]', repr(friend_player_name),
                '[FriendLevel]', str(friend_player_level),
                '[FriendAttackPoint]', str(friend_player_attack),
                '[IsWinAttack]', str(is_win_attack),
                '[IsWinDefence]', str(is_win_defence),
                '[PlayerAttackPoint]', str(player_attack),
                '[TargetPlayerDefencePoint]', str(target_player_defence),
                '[OldPT]', str(old_pt),
                '[NewPT]', str(new_pt),
                '[NumStraightWins]', str(num_straight_wins),
                '[reward_item_id]', str(reward_item_id),
        )
        actionlog.write('USER_BATTLE_HAREM', player.pk, record)

    @classmethod
    def write_harem_war_cry_log(cls, player, event_point):
        '''
        気合いのオタケピログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[point]', str(event_point),
            )
        actionlog.write('HAREM_WAR_CRY', player.osuser_id, record)

    @classmethod
    def write_harem_force_encounter_stalker_log(cls, player, battle_place, prev_power, after_power):
        '''
        ボスまでスキップログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[BattlePlace]', str(battle_place),
            '[PrevPower]', str(prev_power),
            '[AfterPower]', str(after_power),
            )
        actionlog.write('HAREM_FORCE_ENCOUNTER_STALKER', player.osuser_id, record)

    @classmethod
    def write_add_run_wild_point_log(cls, player, got_point, old_point, new_point, is_run_wild):
        '''
        ゲージpt追加ログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[IsRunWild]', str(is_run_wild),
            '[old_point]',str(old_point),
            '[got_point]',str(got_point),
            '[new_point]',str(new_point),
            )
        actionlog.write('HAREM_ADD_RUN_WILD_POINTS', player.osuser_id, record)

    @classmethod
    def write_signup_log(cls, osuser_id, step, is_user_flash=False, is_confirm=False, is_execute=False):
        '''
        チュートリアルログ
        '''
        record = (
            '[Step]', str(step),
            '[IsUserBattleFlash]', str(is_user_flash),
            '[IsFriendConfirm]', str(is_confirm),
            '[IsFriendExecute]', str(is_execute),
            )
        actionlog.write('TUTORIAL_STEP', osuser_id, record)

    @classmethod
    def write_create_box_log(cls, player, player_yakuza_box, player_yakuza_box_count):
        '''
        レンタル事務所作成
        '''
        record = (
            '[BOX_ID]', str(player_yakuza_box.pk),
            '[BOX_EXPRIED_AT]', str(player_yakuza_box.expired_at),
            '[PLAYER_BOX_COUNT]', str(player_yakuza_box_count),
            )

        actionlog.write('CREATE_BOX', player.osuser_id, record)

    @classmethod
    def write_add_box_log(cls, player, player_yakuza_box, player_yakuza):
        '''
        レンタル事務所に追加した舎弟
        '''
        record = (
            '[BOX_ID]', str(player_yakuza_box.pk),
            '[PLAYER_YAKUZA_ID]', str(player_yakuza.pk),
            '[YAKUZA_ID]', str(player_yakuza.get_yakuza().pk),
            )

        actionlog.write('ADD_BOX', player.osuser_id, record)

    @classmethod
    def write_remove_box_log(cls, player, player_yakuza_box, player_yakuza):
        '''
        レンタル事務所から取り出した舎弟
        '''
        record = (
            '[BOX_ID]', str(player_yakuza_box.pk),
            '[PLAYER_YAKUZA_ID]', str(player_yakuza.pk),
            '[YAKUZA_ID]', str(player_yakuza.get_yakuza().pk),
            )

        actionlog.write('REMOVE_BOX', player.osuser_id, record)

    @classmethod
    def write_accept_box_log(cls, player, player_yakuza_box_id, player_yakuza_box_entry_list):
        '''
        レンタル事務所の期限切れ舎弟受け取り
        '''
        record = [
            '[BOX_ID]', str(player_yakuza_box_id),
            ]

        for i,o in enumerate(player_yakuza_box_entry_list):
            record.append('[PLAYER_YAKUZA_ID_%d]' % (i+1))
            record.append(str(o.pk))
            record.append('[YAKUZA_ID_%d]' % (i+1))
            record.append(str(o.player_yakuza.get_yakuza().pk))

        actionlog.write('ACCEPT_BOX', player.osuser_id, record)

    @classmethod
    def write_extend_box_log(cls, player, player_yakuza_box, old_expired_at, new_expired_at, purchase_type):
        '''
        レンタル事務所を期間延長
        '''
        record = (
            '[BOX_ID]', str(player_yakuza_box.pk),
            '[OLD_EXPRIED_AT]', str(old_expired_at),
            '[NEW_EXPRIED_AT]', str(new_expired_at),
            '[PURCHASE_TYPE]', str(purchase_type),
            )

        actionlog.write('EXTEND_BOX', player.osuser_id, record)

    @classmethod
    def write_delete_shatei_from_box_log(cls, player, player_yakuza_box, player_yakuza):
        '''
        データ不整合が起きているレンタル事務所エントリーを削除
        '''
        record = (
            '[BOX_ID]', str(player_yakuza_box.pk),
            '[PLAYER_YAKUZA_ID]', str(player_yakuza.pk),
            )

        actionlog.write('DELETE_SHATEI_FROM_BOX', player.osuser_id, record)

    @classmethod
    def write_error_battle_member_log(cls, player, member_ids):
        '''
        データ不整合が起きているレンタル事務所エントリーを削除
        '''
        record = (
            '[MemberIDs]', str(','.join(member_ids)),
            )

        actionlog.write('ERROR_BATTLE_MEMBER', player.osuser_id, record)

    @classmethod
    def write_vote_log(cls, player, vote_id, entry_no):
        '''
        投票ログ
        '''
        record = (
            '[VOTE_ID]', str(vote_id),
            '[ENTRY_NO]', str(entry_no),
            )

        actionlog.write('VOTE', player.osuser_id, record)

    @classmethod
    def write_trade_not_match_card_log(cls, player, target_player, original_player_id):
        '''
        トレードで自分の所持舎弟以外をトレードしてる！ログ
        '''
        record = (
            '[Player]', str(player.osuser_id),
            '[TargetPlayer]', str(target_player.osuser_id),
            '[OriginalPlayer]', str(original_player_id),
            )

        actionlog.write('ERROR_TRADE_NOT_MATCH_CARD', player.osuser_id, record)

    @classmethod
    def write_battlemember_setting_log(cls, player, old_shatei, new_shatei, index, is_error=False):
        '''
        バトルメンバー設定ログ
        '''

        if old_shatei:
            record_old = [
            '[OldShateiPK]', str(old_shatei.pk),
            '[OldShateiPlayerID]', str(old_shatei.player_id),
            '[OldShateiYakuzaID]', str(old_shatei.yakuza_id),
            '[OldShateiLevel]', str(old_shatei.level),
            '[OldShateiExp]', str(old_shatei.exp),
            '[OldShateiAttack]', str(old_shatei.attack),
            '[OldShateiDefence]', str(old_shatei.defence),
            '[OldShateiEquipAttack]', str(old_shatei.equip_attack),
            '[OldShateiEquipDefence]', str(old_shatei.equip_defence),
            '[OldShateiEquipCount]', str(old_shatei.equip_count),
            '[OldShateiSkillID]', str(old_shatei.skill_id) if old_shatei.skill else '0',
            '[OldShateiSkillLevel]', str(old_shatei.skill_level),
            '[OldShateiCreatedAt]', str(old_shatei.created_at),
            '[OldShateiUpdatedAt]', str(old_shatei.updated_at),
                          ]
        else:
            record_old = []

        if new_shatei:
            record_new = [
            '[NewShateiPK]', str(new_shatei.pk),
            '[NewShateiPlayerID]', str(new_shatei.player_id),
            '[NewShateiYakuzaID]', str(new_shatei.yakuza_id),
            '[NewShateiLevel]', str(new_shatei.level),
            '[NewShateiExp]', str(new_shatei.exp),
            '[NewShateiAttack]', str(new_shatei.attack),
            '[NewShateiDefence]', str(new_shatei.defence),
            '[NewShateiEquipAttack]', str(new_shatei.equip_attack),
            '[NewShateiEquipDefence]', str(new_shatei.equip_defence),
            '[NewShateiEquipCount]', str(new_shatei.equip_count),
            '[NewShateiSkillID]', str(new_shatei.skill_id) if new_shatei.skill else '0',
            '[NewShateiSkillLevel]', str(new_shatei.skill_level),
            '[NewShateiCreatedAt]', str(new_shatei.created_at),
            '[NewShateiUpdatedAt]', str(new_shatei.updated_at),
                          ]
        else:
            record_new = []

        record = [
            '[SetIndex]', str(index),
            '[IsErrorSet]', '1' if is_error else '0',
            ]
        record.extend(record_old)
        record.extend(record_new)

        actionlog.write('BATTLEMEMBER_SETTING', player.osuser_id, record)

    @classmethod
    def write_battlemember_changing_log(cls, player, change_shatei_1, change_shatei_2, change_index_1, change_index_2):
        '''
        バトルメンバー入れ替えログ
        '''
        if change_shatei_1:
            record_old = [
            '[Change1ShateiPK]', str(change_shatei_1.pk),
            '[Change1ShateiPlayerID]', str(change_shatei_1.player_id),
            '[Change1ShateiYakuzaID]', str(change_shatei_1.yakuza_id),
            '[Change1ShateiLevel]', str(change_shatei_1.level),
            '[Change1ShateiExp]', str(change_shatei_1.exp),
            '[Change1ShateiAttack]', str(change_shatei_1.attack),
            '[Change1ShateiDefence]', str(change_shatei_1.defence),
            '[Change1ShateiEquipAttack]', str(change_shatei_1.equip_attack),
            '[Change1ShateiEquipDefence]', str(change_shatei_1.equip_defence),
            '[Change1ShateiEquipCount]', str(change_shatei_1.equip_count),
            '[Change1ShateiSkillID]', str(change_shatei_1.skill_id) if change_shatei_1.skill else '0',
            '[Change1ShateiSkillLevel]', str(change_shatei_1.skill_level),
            '[Change1ShateiCreatedAt]', str(change_shatei_1.created_at),
            '[Change1ShateiUpdatedAt]', str(change_shatei_1.updated_at),
                          ]
        else:
            record_old = []

        if change_shatei_2:
            record_new = [
            '[Change2ShateiPK]', str(change_shatei_2.pk),
            '[Change2ShateiPlayerID]', str(change_shatei_2.player_id),
            '[Change2ShateiYakuzaID]', str(change_shatei_2.yakuza_id),
            '[Change2ShateiLevel]', str(change_shatei_2.level),
            '[Change2ShateiExp]', str(change_shatei_2.exp),
            '[Change2ShateiAttack]', str(change_shatei_2.attack),
            '[Change2ShateiDefence]', str(change_shatei_2.defence),
            '[Change2ShateiEquipAttack]', str(change_shatei_2.equip_attack),
            '[Change2ShateiEquipDefence]', str(change_shatei_2.equip_defence),
            '[Change2ShateiEquipCount]', str(change_shatei_2.equip_count),
            '[Change2ShateiSkillID]', str(change_shatei_2.skill_id) if change_shatei_2.skill else '0',
            '[Change2ShateiSkillLevel]', str(change_shatei_2.skill_level),
            '[Change2ShateiCreatedAt]', str(change_shatei_2.created_at),
            '[Change2ShateiUpdatedAt]', str(change_shatei_2.updated_at),
                          ]
        else:
            record_new = []

        record = [
            '[ChangeIndex1]', str(change_index_1),
            '[ChangeIndex2]', str(change_index_2),
            ]
        record.extend(record_old)
        record.extend(record_new)

        actionlog.write('BATTLEMEMBER_CHANGING', player.osuser_id, record)

    @classmethod
    def write_yakuza_leader_setting_log(cls, player, player_yakuza):
        '''
        若頭を設定したログ
        '''
        record = (
            '[PlayerYakuzaID]', str(player_yakuza.pk),
            '[YakuzaID]', str(player_yakuza.yakuza_id),
            '[PlayerYakuza_PlayerID]', str(player_yakuza.player_id),
            )

        actionlog.write('YAKUZA_LEADER_SETTING', player.osuser_id, record)

    @classmethod
    def write_campaign_cure_log(cls, player, place_id, old_power, new_power):
        '''
        温泉キャンペーンで体力回復したログ
        '''
        record = (
            '[PlaceID]', str(place_id),
            '[OldPower]', str(old_power),
            '[AfterPower]', str(new_power),
            )

        actionlog.write('CAMPAIGN_CURE', player.osuser_id, record)

    @classmethod
    def write_gift_send_gift_log(cls, player, send_player_id, receive_player_id, gift_type, gift, quantity):
        '''
        節分キャンペーンでギフトを贈ったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            '[GiftType]', str(gift_type),
            '[Gift]', str(gift),
            '[Quantity]', str(quantity),
            )

        actionlog.write('GIFT_SEND_GIFT', player.osuser_id, record)

    @classmethod
    def write_gift_send_gift_duplicate_log(cls, player, send_player_id, receive_player_id):
        '''
        節分キャンペーンでギフトを送れなかったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            )

        actionlog.write('GIFT_SEND_GIFT_DUPLICATE', player.osuser_id, record)

    @classmethod
    def write_gift_receive_gift_log(cls, player, send_player_id, receive_player_id, gift_type, gift, quantity):
        '''
        節分キャンペーンでギフトを受け取ったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            '[GiftType]', str(gift_type),
            '[Gift]', str(gift),
            '[Quantity]', str(quantity),
            )

        actionlog.write('GIFT_RECEIVE_GIFT', player.osuser_id, record)

    @classmethod
    def write_gift_receive_time_log(cls, player, receive_player_id, num, sec):
        '''
        節分キャンペーンでギフトの受け取りに要した時間のログ
        '''
        record = (
            '[ReceivePlayer]', str(receive_player_id),
            '[Num]', str(num),
            '[Sec]', str(sec),
            )

        actionlog.write('GIFT_RECEIVE_GIFT_TIME', player.osuser_id, record)

    @classmethod
    def write_valentine_send_gift_log(cls, player, send_player_id, receive_player_id, is_friend, gift_type, gift, quantity, old_point, new_point, add_point):
        '''
        バレンタインキャンペーンでギフトを贈ったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            '[IsFriend]', str(is_friend),
            '[GiftType]', str(gift_type),
            '[Gift]', str(gift),
            '[Quantity]', str(quantity),
            '[OldPoint]', str(old_point),
            '[NewPoint]', str(new_point),
            '[AddPoint]', str(add_point),
            )

        actionlog.write('VALENTINE_SEND_GIFT', player.osuser_id, record)

    @classmethod
    def write_valentine_send_gift_duplicate_log(cls, player, send_player_id, receive_player_id):
        '''
        バレンタインキャンペーンでギフトを送れなかったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            )

        actionlog.write('VALENTINE_SEND_GIFT_DUPLICATE', player.osuser_id, record)

    @classmethod
    def write_valentine_receive_gift_log(cls, player, send_player_id, receive_player_id, gift_type, gift, quantity):
        '''
        バレンタインキャンペーンでギフトを受け取ったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            '[GiftType]', str(gift_type),
            '[Gift]', str(gift),
            '[Quantity]', str(quantity),
            )

        actionlog.write('VALENTINE_RECEIVE_GIFT', player.osuser_id, record)

    @classmethod
    def write_valentine_receive_time_log(cls, player, receive_player_id, num, sec):
        '''
        バレンタインキャンペーンでギフトの受け取りに要した時間のログ
        '''
        record = (
            '[ReceivePlayer]', str(receive_player_id),
            '[Num]', str(num),
            '[Sec]', str(sec),
            )

        actionlog.write('VALENTINE_RECEIVE_GIFT_TIME', player.osuser_id, record)

    @classmethod
    def write_valentine_send_not_auth_log(cls, player, send_player_id, receive_player_id):
        '''
        バレンタインキャンペーンで未認証のためギフトを送れなかったログ
        '''
        record = (
            '[SendPlayer]', str(send_player_id),
            '[ReceivePlayer]', str(receive_player_id),
            )

        actionlog.write('VALENTINE_SEND_NOT_AUTH', player.osuser_id, record)

    @classmethod
    def write_valentine_select_list_time_log(cls, player, category, proposed_num, list_num, sec):
        '''
        バレンタインキャンペーンで送信リストのデータ取得に要した時間のログ
        '''
        record = (
            '[Category]', str(category),
            '[ProposedNum]', str(proposed_num),
            '[ListNum]', str(list_num),
            '[Sec]', str(sec),
            )

        actionlog.write('VALENTINE_SELECT_LIST_TIME', player.osuser_id, record)

    @classmethod
    def write_valentine_forced_requestid_log(cls, player, request_id, friend_player_ids):
        '''
        バレンタインキャンペーントレカリクエスト送信時にGREEでrequest_idが付与されなかった場合に、
        アプリ側で強制的にIDを付与したログ
        '''
        record = (
            '[SendPlayer]', str(player.osuser_id),
            '[RequestId]', str(request_id),
            '[TargetFriends]', str(",".join([str(v) for v in friend_player_ids])),
            )
        actionlog.write('VALENTINE_FORCED_REQUEST_ID', player.osuser_id, record)


    @classmethod
    def write_tyokotto_hagure_pick_error_log(cls, player, values):
        '''
        ちょこっと!ﾁｮｺ狩りpick転換エラー
        '''
        record = (
            '[values]', str(values),
            )

        actionlog.write('TYOKOTTO_PICK_ERROR_VALUES', player.osuser_id, record)

    @classmethod
    def write_tyokotto_hagure_log(cls, player, rank, hp, number, all_number):
        '''
        ちょこっと!ﾁｮｺ狩りはぐれ出会った情報
        '''
        record = (
            '[rank]', str(rank),
            '[hp]', str(hp),
            '[number]', str(number),
            '[all_number]', str(all_number),
            )

        actionlog.write('TYOKOTTO_HAGURE', player.osuser_id, record)

    @classmethod
    def write_tyokotto_rank_log(cls, player, rank, automatic, all_number):
        '''
        ちょこっと!ﾁｮｺ狩りはぐれ出会った情報
        '''
        record = (
            '[rank]', str(rank),
            '[automatic]', str(automatic),
            '[all_number]', str(all_number),
            )

        actionlog.write('TYOKOTTO_RANK_UP', player.osuser_id, record)

    @classmethod
    def write_tyokotto_hagure_incentive_log(cls, player, item_id, result):
        '''
        ちょこっと!ﾁｮｺ狩りはぐれ出会った情報
        '''
        record = (
            '[item_id]', str(item_id),
            '[result]', str(result),
            )

        actionlog.write('TYOKOTTO_HAGURE_INCENTIVE', player.osuser_id, record)


    @classmethod
    def write_do_comp_succeess_log(cls, player, player_compsheet, target_yakuza_id):
        '''
        コンプシート対象assignログ
        '''
        record = (
            '[CompsheetCount]', str(player_compsheet.compsheet_count),
            '[CompsheetID]', str(player_compsheet.compsheet_id),
            '[YakuzaID]', str(target_yakuza_id),
        )

        actionlog.write('DO_COMPSHEET', str(player.pk), record)

    @classmethod
    def write_do_comp_countreward_log(cls, player, player_compsheet, present, type, target_get_count):
        '''
        コンプシート対象countrewardログ
        '''
        present_id = None
        present_name = None
        type = int(type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = 0
            present_name = 'communication_point'
        elif type == 6:
            present_id = 0
            present_name = 'medal'
        elif present:
            present_id = present.pk
            try:
                present_name = present.name
            except AttributeError:
                present_name = present.__class__.__name__
        else:
            present_id = 0
            present_name = present.__class__.__name__
        record = (
            '[CompsheetCount]', str(player_compsheet.compsheet_count),
            '[PlayerCompsheetID]', str(player_compsheet.pk),
            '[PresentID]', repr(present_id),
            '[Present]', repr(present_name),
            '[Type]', str(type),
            '[TargetGetCount]', str(target_get_count),
        )

        actionlog.write('DO_COMPCOUNT_REWARD', str(player.pk), record)

    @classmethod
    def write_do_complete_log(cls, player, compsheet_id, present, type, compsheet_count, is_multicomp):
        '''
        コンプシートcompleteログ
        '''
        present_id = None
        present_name = None
        type = int(type)
        if type == 4:
            present_id = present
            present_name = 'money'
        elif type == 5:
            present_id = 0
            present_name = 'communication_point'
        elif type == 6:
            present_id = 0
            present_name = 'medal'
        elif present:
            present_id = present.pk
            try:
                present_name = present.name
            except AttributeError:
                present_name = present.__class__.__name__
        else:
            present_id = 0
            present_name = present.__class__.__name__
        record = (
            '[CompsheetID]', str(compsheet_id),
            '[Present]', repr(present_name),
            '[Type]', str(type),
            '[CompsheetCount]', str(compsheet_count),
            '[IS_MultiComp]', str(is_multicomp),
        )

        actionlog.write('DO_COMPSHEET_REWARD', player.pk, record)

    @classmethod
    def write_is_multicomp_init_log(cls, player, compsheet_id):
        record = (
            '[CompsheetID]', str(compsheet_id),
        )

        actionlog.write('DO_MULTICOMP_INIT', player.pk, record)


    @classmethod
    def write_update_max_power_log(cls, player, before_max_power, after_max_power):
        '''
        体力最大を回復したログ
        '''

        record = (
            '[BeforeMaxPower]', str(before_max_power),
            '[AfterMaxPower]', str(after_max_power),
        )

        actionlog.write('UPDATE_MAX_POWER', player.pk, record)

    @classmethod
    def write_panel_gacha_log(cls, player, gacha_id, panel_num, present, present_type):
        '''
        パネルガチャログ
        '''
        from common.static_values import StaticValues

        present_log = None
        if present_type == StaticValues.TYPE_ITEM:
            present_log = present.pk
        elif present_type == StaticValues.TYPE_CARD:
            present_log = present.pk
        elif present_type == StaticValues.TYPE_POINT or present_type == StaticValues.TYPE_MEDAL:
            present_log = present
        elif present_type == StaticValues.TYPE_MONEY:
            present_log = present
        elif present_type == StaticValues.TYPE_YAKUZAEQUIP:
            present_log = present.pk

        record = (
            '[GACHA_ID]', str(gacha_id),
            '[PANEL_NUM]', str(panel_num),
            '[PRESENT_ID]', str(present_log),
            '[PRESENT_TYPE]', str(present_type),
        )

        actionlog.write('PANEL_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_panel_gacha_open_count_log(cls, player, gacha_id, open_count):
        '''
        パネルガチャオープン枚数ログ
        '''

        record = (
            '[GACHA_ID]', str(gacha_id),
            '[PANEL_OPEN_COUNT]', str(open_count),
        )

        actionlog.write('PANEL_GACHA_OPEN_COUNT', player.pk, record)



    @classmethod
    def write_limitation_gacha_log(cls, player, gacha_id, is_reset, yakuza=None, deck_types=[]):
        '''
        絞り込みガチャログ
        '''
        yakuza_id = 0
        yakuza_rarity = 0
        if yakuza:
            yakuza_id = yakuza.pk
            yakuza_rarity = yakuza.rarity

        record = (
            '[GachaID]', str(gacha_id),
            '[IsReset]', str(is_reset),
            '[YakuzaID]', str(yakuza_id),
            '[Rarity]', str(yakuza_rarity),
            '[DeckTypes]', str(deck_types),
        )
        actionlog.write('LIMITATION_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_fever_gacha_log(cls, player, gacha_id, yakuza_ids, result_type, present, present_type, present_num):
        '''
        フィーバーガチャログ
        '''
        present_id = 0
        if present:
            present_id = present.pk

        record = (
            '[GachaID]', str(gacha_id),
            '[YakuzaIDs]', str(yakuza_ids),
            '[ResultType]', str(result_type),
            '[PresentID]', str(present_id),
            '[PresentType]', str(present_type),
            '[PresentNum]', str(present_num),
        )
        actionlog.write('FEVER_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_parking_gacha_log(cls, player, gacha_id, is_reset, yakuza=None, current_parking=[], remaining_car={}):
        """パーキングガチャログ"""
        yakuza_info = {'id': 0, 'rarity': 0}
        if yakuza:
          yakuza_info = {'id': yakuza.pk, 'rarity': yakuza.rarity}

        record = (
            '[GachaID]', str(gacha_id),
            '[Yakuza]', str(yakuza_info),
            '[IsReset]', str(is_reset),
            '[CurrentParking]', str(current_parking),
            '[RemainingCar]', str(remaining_car),
        )
        actionlog.write('PARKING_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_levelup_gacha_log(cls, player, gacha_id, yakuza=None, current_level=1, before_level=1):
        """レベルアップガチャログ"""
        yakuza_info = {'id': 0, 'rarity': 0}
        if yakuza:
          yakuza_info = {'id': yakuza.pk, 'rarity': yakuza.rarity}

        record = (
            '[GachaID]', str(gacha_id),
            '[Yakuza]', str(yakuza_info),
            '[CurrentLevel]', str(current_level),
            '[BeforeLevel]', str(before_level),
        )
        actionlog.write('LEVELUP_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_bus_chase_gacha_log(cls, player, gacha_id, yakuzas=[], deck_keys=[]):
        """バスチェイスガチャログ"""

        record = (
            '[GachaID]', str(gacha_id),
            '[Yakuzas]', str(yakuzas),
            '[DeckKeys]', str(deck_keys),
        )
        actionlog.write('BUS_CHASE_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_retry_gacha_log(cls, player, gacha_id, yakuzas=[], retry_count=0, is_confirm=0):
        """引き直しガチャログ"""

        record = (
            '[GachaID]', str(gacha_id),
            '[Yakuzas]', str(yakuzas),
            '[RetryCount]', str(retry_count),
            '[Confirm]', str(is_confirm),
        )
        actionlog.write('RETRY_GACHA_RESULT', player.pk, record)

    @classmethod
    def write_treasure_gacha_log(cls, player, gacha_id, reward_id):
        """3連金庫ガチャログ"""

        record = (
            '[GachaID]', str(gacha_id),
            '[RewardID]', str(reward_id),
        )
        actionlog.write('TREASURE_GACHA_RESULT', player.pk, record)


    @classmethod
    def write_access_time_log(cls, player, return_id, func_time, others):
        '''
        アクセス処理時間ログ
        '''
        record = [
            '[return_id]', str(return_id),
            '[func_time]', str(func_time),
            ]

        record.extend(others)

        actionlog.write('MYROOM_FUNC_TIME', player.pk, record)

    @classmethod
    def write_fq_present_log(cls, player, trigger_key, reward):
        """
        ファルキューレ
        """

    @classmethod
    def write_bingo_count_log(cls, player_id, bingo_id, bingo_count):
        """ビンゴガチャのビンゴ回数ログ"""

        record = (
            '[BINGOID]', str(bingo_id),
            '[BingoCount]', str(bingo_count),
        )
        actionlog.write('BINGO_COUNT', player_id, record)

    @classmethod
    def write_add_shatei_count_log(cls, player, old, new):
        """
        舎弟枠増加
        """
        record = (
            '[OldShateiMaxCount]', str(old),
            '[NewShateiMaxCount]', str(new),
        )

        actionlog.write('OFFICE_ADD_MAX_COUNT', player.pk, record)

    @classmethod
    def write_box_reset_log(cls, player, gacha_id, deck_id):
        """ パッケージリセット
        """
        record = (
            '[GACHAID]', str(gacha_id),
            '[SetGachaDeckID]', str(deck_id),
        )

        actionlog.write('BOX_RESET', player.pk, record)

    @classmethod
    def write_three_select_deck_log(cls, player, gacha_id, gacha_count):
        """ 3択ガチャ、ガチャ時のデッキ
        gacha_count: GachaCountのcount値
        """
        record = (
            '[GACHAID]', str(gacha_id),
            '[GachaCount_Count]', str(gacha_count),
        )

        actionlog.write('SELECT_DECK_LOG', player.pk, record)

    @classmethod
    def write_pre_receive_present_log(cls, player, present_id):
        """
        プレゼント受け取り
        """
        record = (
            '[PresentID]', str(present_id),
        )

        actionlog.write('RECEIVE_VPRE_PRESENT', player.pk, record)

