# -*- coding: utf-8 -*-

from optparse import make_option
from django.core.management.base import BaseCommand
from player.models import Player

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        SILVER_PLAYERS = [
            31776992,
            23883794,
            26130894,
            49785055,
            45025049,
            4240633,
            8828398,
            44223695,
            11344454,
            29453929,
            29453929,
            15208704,
            44101510,
            45025049,
            33329760,
            34294294,
            49001773,
            39469329,
            34167645,
            21304032,
            7919365,
            52950076,
            19042257,
            16884222,
            57368734,
            44225730,
            30414047,
            15422263,
            37883326,
            37883326,
            17094103,
            15732637,
            9193914,
            17541837,
            45923385,
            785381,
            15980801,
            24987608,
            14990495,
            43046261,
            51448498,
            21395507,
            46848693,
            49350821,
            39566025,
            30042469,
            20292089,
            20292089,
            48670871,
            43393447,
            56989465,
            5539098,
            36812113,
            48350746,
            26846223,
            49785055,
            47633030,
            16464623,
            48849291,
            22822406,
            13893978,
            26801339,
            3441673,
            6976943,
            3341837,
            45025049,
            48284200,
            2737538,
            47395200,
            42077237,
            51509757,
            5622022,
            50832868,
            42111853,
            ]

        print "******SEIRYUU*****"
        bakuto_seiryuu = []
        interi_seiryuu = []

        for player_id in SILVER_PLAYERS:
            target_player = Player.get(str(player_id))
            if target_player:
                if target_player.category == 2:
                    bakuto_seiryuu.append(target_player)
                elif target_player.category == 3:
                    interi_seiryuu.append(target_player)

        print "******BAKUTO******"
        for x in bakuto_seiryuu:
            print x.pk
        print "******INTERI******"
        for x in interi_seiryuu:
            print x.pk

        GOLD_PLAYERS = [
            49785055,
            32555880,
            43774979,
            15738609,
            54096735,
            47267272,
            46994564,
            15980801,
            46985357,
            53359526,
            58897914,
            23122213,
            14202019,
            47329211,
            31034618,
            29453929,
            17007660,
            54923884,
            30042469,
            15212962,
            ]

        print "******SUZAKU******"
        bakuto_suzaku = []
        interi_suzaku = []

        for player_id in GOLD_PLAYERS:
            target_player = Player.get(str(player_id))
            if target_player:
                if target_player.category == 2:
                    bakuto_suzaku.append(target_player)
                elif target_player.category == 3:
                    interi_suzaku.append(target_player)

        print "******BAKUTO******"
        for x in bakuto_suzaku:
            print x.pk
        print "******INTERI******"
        for x in interi_suzaku:
            print x.pk
