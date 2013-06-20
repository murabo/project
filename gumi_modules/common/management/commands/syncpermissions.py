# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.management import update_all_contenttypes
from django.contrib.auth.management import create_permissions
from django.db.models import get_apps


"""
パーミッションを更新する
"""
class Command(BaseCommand):
    def handle(self, *args, **options):

        # Add any missing content types
        update_all_contenttypes()

        # Add any missing permissions
        for app in get_apps():
            create_permissions(app, None, 2)

