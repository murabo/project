# -*- coding: utf-8 -*-

"""
ガチャデッキを全てリセット
"""

import optparse
from django.core.management.base import BaseCommand
from django.core.cache import cache
from gacha.models import Gacha, GachaDeck, GachaCount
from gacha.chasegacha.models import ChaseDeck,BusDeckGroup

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        optparse.make_option("--gacha_id", action="store", dest="gacha_id", default=None),
        optparse.make_option("--gacha_type", action="store", dest="gacha_type", default=None))

    def handle(self, *args, **options):
        # 事前にキャッシュクリア
        cache.clear()

        # ガチャIDがあれば、ガチャ回数に紐づいたデッキのみ初期化。なければ全デッキを初期化
        # ガチャ回数に紐づかないカーチェイスガチャなど、ガチャIDを指定せずにガチャタイプを指定して関連デッキを初期化

        if options["gacha_id"]:
            gacha_id = options["gacha_id"]
            # 通常ガチャ取得
            gacha = Gacha.get(int(gacha_id))
            # ガチャデッキ取得
            gacha_decks = GachaCount.objects.filter(gacha=gacha)
            if gacha_decks:
                for deck in gacha_decks:
                    _clear_deck(deck.gacha_deck)
            else:
                print u"failed get deck instance"

        elif options["gacha_type"]:
            # 特殊なガチャデッキの全初期化
            if options["gacha_type"] == 'chase':

                decks = []
                chasedecks = ChaseDeck.objects.all()
                decks.extend(chasedecks)

                chasedecks = BusDeckGroup.objects.all()
                decks.extend(chasedecks)

                deck_ids = [ deck.deck_id for deck in decks]
                deck_ids = list(set(deck_ids))
                deck_ids.sort()

                for deck_id in deck_ids:
                    deck = GachaDeck.get(deck_id)
                    _clear_deck(deck)
            else:
                print u"not authorizing gacha_type"
        else:
            #ガチャデッキの全初期化
            decks = GachaDeck.get_all()
            for deck in decks:
                _clear_deck(deck)

def _clear_deck(deck):
    # ガチャデッキを初期化
    if deck:
        deck.set_item_list_gacha('')
        print u"deck::%s init" % deck.id
    else:
        print u"failed get deck instance"