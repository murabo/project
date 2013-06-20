# -*- encoding: UTF-8 -*-

import unittest
from common.dynamic_import import DynamicImport, DynamicEventModuleImport
from common.static_values import StaticValues

class Testcase_001_DynamicImport(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_find_files(self):
        paths = DynamicImport.find_files('common', 'static_values')
        assert paths[0] == 'common/static_values.py'

    def test_002_import_module(self):
        paths = DynamicImport.find_files('common', 'static_values')
        SV = DynamicImport.import_module(paths[0], 'StaticValues')
        assert SV.TYPE_CARD == StaticValues.TYPE_CARD


class Testcase_002_DynamicEventModuleImport(unittest.TestCase):
    def setUp(self):
        #ひとまず現状で最新版を使う
        self.event_id = 157
        pass

    def tearDown(self):
        pass

    def test_001_find_files_by_id(self):
        path = DynamicEventModuleImport.find_files_by_id(0)
        assert path is None

        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        assert path == 'eventmodule/e%s_yakuzatree' % self.event_id

    def test_002_find_files_by_name(self):
        paths = DynamicEventModuleImport.find_files_by_name('yakuzatree')
        for path in paths:
            assert 'yakuzatree' in path

    def test_003_find_files_by_category(self):
        paths = DynamicEventModuleImport.find_files_by_category(StaticValues.EVENT_CATEGORY_TREE)
        for path in paths:
            assert 'yakuzatree' in path

    def test_004_get_templates_path(self):
        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        path1 = DynamicEventModuleImport.get_templates_path(path, True)
        assert 'mobile' in path1
        path2 = DynamicEventModuleImport.get_templates_path(path, False)
        assert 'smartphone' in path2

    def test_005_import_constants(self):
        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        esv = DynamicEventModuleImport.import_constants(path)
        assert esv.EVENT_ID == self.event_id

    def test_006_import_boss_constants(self):
        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        module = DynamicEventModuleImport.import_boss_constants(path)
        assert module.RESCUE_SEND_PLAYER_COUNT_MAX == 20

    def test_007_import_decorators(self):
        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        module = DynamicEventModuleImport.import_decorators(path, 'require_event_player')
        assert module.__class__.__name__ == 'function'

    def test_008_import_base_utils(self):
        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        module = DynamicEventModuleImport.import_base_utils(path, 'get_event_player_place')
        assert module.__class__.__name__ == 'function'

    def test_009_import_actionlog_util(self):
        path = DynamicEventModuleImport.find_files_by_id(self.event_id)
        module = DynamicEventModuleImport.import_actionlog_util(path, 'YakuzaTreeActionLogUtils')
        assert module.__class__.__name__ == 'type'
        assert  'write_city_execute_max' in dir(module)

if __name__ == "__main__":
        unittest.main()
