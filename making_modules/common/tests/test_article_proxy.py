# -*- encoding: UTF-8 -*-

import unittest
from common.static_values import StaticValues
from common.article_proxy import BaseArticleProxy, ArticleProxy
from common.nose_util import create_player

from yakuza.models import Yakuza, PlayerYakuza
from item.models import GameItem, PlayerItem
from gokujo.models import Gokujo, PlayerGokujo
from present.models import PlayerPresent
from equipment.models import GokujoEquipmentItem, YakuzaEquipmentItem, PlayerGokujoEquipmentItem, PlayerYakuzaEquipmentItem


class Testcase_001_BaseArticleProxy(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_is_none(self):
        assert BaseArticleProxy.is_none(StaticValues.TYPE_NONE) is True
        assert BaseArticleProxy.is_none(StaticValues.TYPE_CARD) is False

    def test_002_is_card(self):
        assert BaseArticleProxy.is_card(StaticValues.TYPE_CARD) is True
        assert BaseArticleProxy.is_card(StaticValues.TYPE_NONE) is False

    def test_003_is_item(self):
        assert BaseArticleProxy.is_item(StaticValues.TYPE_ITEM) is True
        assert BaseArticleProxy.is_item(StaticValues.TYPE_NONE) is False

    def test_004_is_treasure(self):
        assert BaseArticleProxy.is_treasure(StaticValues.TYPE_TREASURE) is True
        assert BaseArticleProxy.is_treasure(StaticValues.TYPE_NONE) is False

    def test_005_is_money(self):
        assert BaseArticleProxy.is_money(StaticValues.TYPE_MONEY) is True
        assert BaseArticleProxy.is_money(StaticValues.TYPE_NONE) is False

    def test_006_is_point(self):
        assert BaseArticleProxy.is_point(StaticValues.TYPE_POINT) is True
        assert BaseArticleProxy.is_point(StaticValues.TYPE_NONE) is False

    def test_007_is_medal(self):
        assert BaseArticleProxy.is_medal(StaticValues.TYPE_MEDAL) is True
        assert BaseArticleProxy.is_medal(StaticValues.TYPE_NONE) is False

    def test_008_is_num(self):
        assert BaseArticleProxy.is_num(StaticValues.TYPE_MONEY) is True
        assert BaseArticleProxy.is_num(StaticValues.TYPE_POINT) is True
        assert BaseArticleProxy.is_num(StaticValues.TYPE_MEDAL) is True
        assert BaseArticleProxy.is_num(StaticValues.TYPE_NONE) is False

    def test_009_is_gokujoequip(self):
        assert BaseArticleProxy.is_gokujoequip(StaticValues.TYPE_GOKUJOEQUIP) is True
        assert BaseArticleProxy.is_gokujoequip(StaticValues.TYPE_NONE) is False

    def test_010_is_yakuzaequip(self):
        assert BaseArticleProxy.is_yakuzaequip(StaticValues.TYPE_YAKUZAEQUIP) is True
        assert BaseArticleProxy.is_yakuzaequip(StaticValues.TYPE_NONE) is False

    def test_011_is_equip(self):
        assert BaseArticleProxy.is_equip(StaticValues.TYPE_GOKUJOEQUIP) is True
        assert BaseArticleProxy.is_equip(StaticValues.TYPE_YAKUZAEQUIP) is True
        assert BaseArticleProxy.is_equip(StaticValues.TYPE_NONE) is False

    def test_012_get_class(self):
        obj = BaseArticleProxy.get_class(StaticValues.TYPE_NONE)
        assert obj is None

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_CARD)
        assert obj == Yakuza

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_ITEM)
        assert obj == GameItem

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_TREASURE)
        assert obj == Gokujo

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_MONEY)
        assert obj is None

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_POINT)
        assert obj is None

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_MEDAL)
        assert obj is None

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_GOKUJOEQUIP)
        assert obj == GokujoEquipmentItem

        obj = BaseArticleProxy.get_class(StaticValues.TYPE_YAKUZAEQUIP)
        assert obj == YakuzaEquipmentItem

    def test_013_get_object(self):
        obj = BaseArticleProxy.get_object(StaticValues.TYPE_NONE, 1)
        assert obj is None

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_CARD, 1)
        assert int(obj.id) == 1

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_ITEM, 1)
        assert int(obj.id) == 1

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_TREASURE, 1) #こっちは極女
        assert int(obj.id) == 1
        obj = BaseArticleProxy.get_object(StaticValues.TYPE_TREASURE, 25) #こっちは秘宝
        assert int(obj.id) == 25

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_MONEY, 1)
        assert obj == 1

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_POINT, 1)
        assert obj == 1

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_MEDAL, 1)
        assert obj == 1

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_GOKUJOEQUIP, 1)
        assert int(obj.id) == 1

        obj = BaseArticleProxy.get_object(StaticValues.TYPE_YAKUZAEQUIP, 1)
        assert int(obj.id) == 1

    def test_014_get_object_type_id(self):
        "実装を悩み中なので未テスト"
        pass

    def test_015_image_url(self):
        #TODO:パスが正しいかのテストはどうする?
        obj = BaseArticleProxy.image_url(StaticValues.TYPE_NONE)
        assert obj is None

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_CARD, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_ITEM, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_TREASURE, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_MONEY, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_POINT, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_MEDAL, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_GOKUJOEQUIP, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url(StaticValues.TYPE_YAKUZAEQUIP, 1)
        assert isinstance(obj, str)

    def test_016_image_url_m(self):
        #TODO:パスが正しいかのテストはどうする?
        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_NONE)
        assert obj is None

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_CARD, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_ITEM, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_TREASURE, 1)
        assert obj is None

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_MONEY, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_POINT, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_MEDAL, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_GOKUJOEQUIP, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_m(StaticValues.TYPE_YAKUZAEQUIP, 1)
        assert isinstance(obj, str)

    def test_017_image_url_comp(self):
        #TODO:パスが正しいかのテストはどうする?
        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_NONE)
        assert obj is None

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_CARD, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_ITEM, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_TREASURE, 1)
        assert obj is None

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_MONEY, 1)
        assert obj is None

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_POINT, 1)
        assert obj is None

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_MEDAL, 1)
        assert obj is None

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_GOKUJOEQUIP, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_comp(StaticValues.TYPE_YAKUZAEQUIP, 1)
        assert isinstance(obj, str)

    def test_018_image_url_s(self):
        #TODO:パスが正しいかのテストはどうする?
        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_NONE)
        assert obj is None

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_CARD, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_ITEM, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_TREASURE, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_MONEY, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_POINT, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_MEDAL, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_GOKUJOEQUIP, 1)
        assert isinstance(obj, str)

        obj = BaseArticleProxy.image_url_s(StaticValues.TYPE_YAKUZAEQUIP, 1)
        assert isinstance(obj, str)

    def test_019_name(self):
        obj = BaseArticleProxy.name(StaticValues.TYPE_NONE, 1)
        assert obj is None

        obj = BaseArticleProxy.name(StaticValues.TYPE_CARD, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_ITEM, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_TREASURE, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_MONEY, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_POINT, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_MEDAL, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_GOKUJOEQUIP, 1)
        assert isinstance(obj, unicode)

        obj = BaseArticleProxy.name(StaticValues.TYPE_YAKUZAEQUIP, 1)
        assert isinstance(obj, unicode)

class Testcase_002_ArticleProxy(unittest.TestCase):
    def setUp(self):
        self.player = create_player(5000)

    def tearDown(self):
        objs = PlayerPresent.objects.all()
        for obj in objs:
            obj.delete()

        objs = PlayerYakuza.objects.all()
        for obj in objs:
            obj.delete()

        objs = PlayerItem.objects.all()
        for obj in objs:
            obj.delete()

        objs = PlayerGokujo.objects.all()
        for obj in objs:
            obj.delete()

        objs = PlayerGokujoEquipmentItem.objects.all()
        for obj in objs:
            obj.delete()

        objs = PlayerYakuzaEquipmentItem.objects.all()
        for obj in objs:
            obj.delete()

        self.player.delete()

    def test_001_give_official_present(self):
        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_NONE, 1, u"test")
        assert ret is None

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_CARD, 1, u"test")
        assert isinstance(ret, PlayerPresent)

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_ITEM, 1, u"test")
        assert isinstance(ret, PlayerPresent)

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_TREASURE, 1, u"test")
        assert ret is None

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_TREASURE, 25, u"test")
        assert isinstance(ret, PlayerPresent)

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_MONEY, 1, u"test")
        assert isinstance(ret, PlayerPresent)

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_POINT, 1, u"test")
        assert isinstance(ret, PlayerPresent)

        ret = ArticleProxy.give_official_present(self.player, StaticValues.TYPE_MEDAL, 1, u"test")
        assert isinstance(ret, PlayerPresent)

    def test_002_assign(self):
        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_NONE, 1)
        assert ret is None

        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_CARD, 1)
        assert isinstance(ret, PlayerYakuza)

        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_ITEM, 1)
        assert isinstance(ret, PlayerItem)

        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_TREASURE, 25)
        assert ret is True

        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_MONEY, 1)
        assert ret == 1

        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_POINT, 1)
        assert ret == 1

        ret = ArticleProxy.assign(self.player, StaticValues.TYPE_MEDAL, 1)
        assert ret == 1

if __name__ == "__main__":
        unittest.main()
