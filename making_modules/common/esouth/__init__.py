# coding: utf-8

'''
index_together で複合インデックスが貼れるようになる

class Meta:
    index_together = (("name", "short_name"), )

# setup

INSTALL_APPS = (
    "common.esouth",
)


'''

# from __future__ import absolute_import
# 姫は absolute_import 使うとコケる？

# db の Meta が index_together が使えるように
from django.db.models import options
options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('index_together', )

# south の meta が index_together が使えるように
from south.modelsinspector import meta_details
meta_details["index_together"] = ["index_together", {"default": []}]

# db の _meta が index_together を使えるように
from django.db.models.base import ModelBase
original = ModelBase.add_to_class
def proxy(cls, name, value):
    if name == "_meta":
        value.index_together =  []
    return original(cls, name, value)
ModelBase.add_to_class = proxy

# south の changes で index_together の変更処理
from south.management.commands import schemamigration
from common.esouth import changes
schemamigration.changes = changes
