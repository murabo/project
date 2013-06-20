# -*- coding: utf-8 -*-

# import os
# from django.core.management.base import BaseCommand
# from django.db.models import get_app, get_apps, get_models, get_model

# from django.core.management.commands.sqlclear import Command
# from south.migration import Migration, Migrations
# from south.exceptions import NoMigrations
#import  south.management.commands.migrate.Command as SouthCommand
from south.models import MigrationHistory
from south.migration.utils import get_app_label
#from django.core.management.sql import sql_delete
from django.core.management.base import AppCommand
from django.db import connections, DEFAULT_DB_ALIAS
from django.db import models
from django.db.utils import IntegrityError
from django.core.management.color import no_style

def sql_delete(app, style, connection):
    "Returns a list of the DROP TABLE SQL statements for the given app."

    # This should work even if a connection isn't available
    try:
        cursor = connection.cursor()
    except:
        cursor = None

    # Figure out which tables already exist
    if cursor:
        table_names = connection.introspection.get_table_list(cursor)
    else:
        table_names = []

    output = []

    # Output DROP TABLE statements for standard application tables.
    to_delete = set()

    references_to_delete = {}
    app_models = models.get_models(app, include_auto_created=True)
    for model in app_models:
        if cursor and connection.introspection.table_name_converter(model._meta.db_table) in table_names:
            # The table exists, so it needs to be dropped
            opts = model._meta
            for f in opts.local_fields:
                if f.rel and f.rel.to not in to_delete:
                    references_to_delete.setdefault(f.rel.to, []).append( (model, f) )

            to_delete.add(model)

    for model in app_models:
        if connection.introspection.table_name_converter(model._meta.db_table) in table_names:
            output.extend(connection.creation.sql_destroy_model(model, references_to_delete, style))
            print connection.creation.sql_destroy_model(model, references_to_delete, style)
            try:
                cursor.execute(connection.creation.sql_destroy_model(model, references_to_delete, style)[0])
            except IntegrityError:
                # IntegrityErrorがでたら後回し
                app_models.append(model)
                print "Delay retry {}".format(model)
                # print connection.creation.sql_destroy_model(model, references_to_delete, style)

    # Close database connection explicitly, in case this output is being piped
    # directly into a database client, to avoid locking issues.
    if cursor:
        cursor.close()
        connection.close()

    return output[::-1] # Reverse it, to deal with table dependencies.


class Command(AppCommand):
    help = "DROP TABLE and DELETE Migration history for <app>"
    
    def handle_app(self, app, **options):
        sql_delete(app, no_style(), connections[options.get('database', DEFAULT_DB_ALIAS)])
        # print "\n".join(sql_delete(app, no_style(), connections[options.get('database', DEFAULT_DB_ALIAS)]))

        applied_migrations = MigrationHistory.objects.filter(app_name = get_app_label(app))
        for migration in applied_migrations:
            print "DELETE FROM south_migrationhistory WHERE id = %s; " % migration
            migration.delete()


