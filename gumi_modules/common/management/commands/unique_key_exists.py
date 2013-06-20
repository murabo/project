# -*- coding: utf-8 -*-

"""
モデルの unique_together が、実際にDBに存在するかをチェックするマネジメントコマンド

※マイグレーションスクリプトではなく、実際のDBをチェックする

./manage.py unique_key_exists --settings=developer.yotsuyanagi.settings
とすれば、全INSTALLED_APPSを対象にチェックを行う。

./manage.py unique_key_exists item --settings=developer.yotsuyanagi.settings
とすれば、item のみを対象にチェックする。

ユニーク制約がなければ、赤字で "NO EXISTS! ...." と表示される

--verbose オプションで、メッセージの冗長出力
"""



from optparse import make_option

from django.core.management.base import BaseCommand
from django.db import models
from django.utils.encoding import smart_str
from django.db import connection

from django.conf import settings
from django.utils.importlib import import_module


class Command(BaseCommand):
    help = "Chech unique-key in db on <app>"
    args = '<app_name>'
    
    option_list = BaseCommand.option_list + (
        make_option('--verbose',
            action='store_true',
            dest='verbose',
            default=False,
            help=u'メッセージ出力の冗長化'),
    )
    
    def echo(self, message):
        """
        例: self.echo(self.style.NOTICE('NG!'))
        """
        print message
#         self.stdout.write(smart_str(message, errors='ignore'))
#         self.stdout.write('\n')
#         self.stdout.flush()
    
    
    def echo_verbose(self, message):
        if self._verbose:
            return self.echo(message)
    
    
    def handle(self, app_label=None, **options):
        
        self._verbose=options.get('verbose', False)
        
        # APPをインポート
        for app_name in settings.INSTALLED_APPS:
            try:
                import_module('.management', app_name)
            except ImportError, exc:
                msg = exc.args[0]
                if not msg.startswith('No module named') or 'management' not in msg:
                    raise
        
        if app_label:
            app_list = [models.get_app(app_label)]
        else:
            app_list = models.get_apps()
        
        for app in app_list:
            if not app_label:
                self.echo_verbose('App: %s' % app)
            
            app_models = models.get_models(app)
            
            cursor = connection.cursor()
            
            if not app_models:
                self.echo_verbose('No app models.')
            
            for app_model in app_models:
                #if not hasattr(app_model, '_meta'):
                #    self.echo_verbose('No _meta: %s' % (app_model.__name__))
                #    continue
                
                # Django上のユニークキー
                unique_together_all = getattr(app_model._meta, 'unique_together', None)
                #self.echo(unique_together_all)
                # DB上
                sql = '''SHOW INDEX FROM %s WHERE Key_name != 'PRIMARY' AND Non_unique = '0' ''' % app_model._meta.db_table
                # このSQLで、Seq_in_index が昇順で出てくるという前提。
                # SHOW INDEX では ORDER_BY は使えない
                cursor.execute(sql)
                unique_key_in_db = {}
                for record in cursor.fetchall():
                    #self.echo(str(record))
                    key_name = record[2]
                    #seq_in_index = record[3]
                    column_name = record[4]
                    
                    if not key_name in unique_key_in_db:
                        unique_key_in_db[key_name] = []
                    unique_key_in_db[key_name].append(column_name)
                
                if unique_together_all:
                    for unique_together in unique_together_all:
                        self.echo('Checking: %s %s' % (app_model.__name__, unique_together))
                        
                        is_hit = False
                        for k, v in unique_key_in_db.iteritems():
                            #self.echo("unique_together=%s, v=%s" % (unique_together, v))
                            all_field_equals = True
                            if len(unique_together) == len(v):
                                for i in xrange(len(unique_together)):
                                    if v[i].startswith(unique_together[i]): #osuser_id とかになる場合があるので
                                        pass
                                    else:
                                        all_field_equals = False
                                if all_field_equals:
                                    self.echo("    exists. key_name=%s" % k)
                                    is_hit = True
                        
                        if is_hit:
                            #self.echo("Hit!")
                            pass
                        else:
                            self.echo(self.style.NOTICE('    NO EXISTS! check sql: "SHOW CREATE TABLE %s;", or "SHOW INDEX FROM %s;"' % (app_model._meta.db_table, app_model._meta.db_table)))
                
                else:
                    self.echo_verbose('No unique-together in django model: %s' % (app_model.__name__))
