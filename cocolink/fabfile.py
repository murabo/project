# encoding:utf-8
from datetime import datetime
from fabric.api import local, run, put, env, cd, settings, execute, require
from fabric.decorators import parallel, runs_once
POOL_SIZE = 8

GIT_NAME = 'cocolink.git'
GIT_URL = 'https://github.com/murabo/project.git'
NOW = str(datetime.today().strftime('%Y-%m-%d_%H:%M:%S'))

"""
二回も調べてしまったので、ここに記載
requireは、左のオブジェクトに、右のオブジェクトが入っているかのチェック。
無駄な時間を・・・・
"""

def staging():
    """
    staging env create
    """
    env.application_name = 'cocolink'
    env.base_dir = '/var/webapp/%s' % env.application_name
    env.nfs_repo = '%s/%s' % (env.base_dir, GIT_NAME)
    env.history_file = '%s%s' % (env.base_dir, '/history.txt')
    env.app_repo = '%s%s' % (env.base_dir, '/repo')
    env.user = "cocouser"
    env.branch = 'master'
    env.nfs_host = '157.7.129.122:49494'
    env.hosts = ['157.7.129.122:49494']
    env.password = 'passcoco'
    print env.app_repo

#def staging():
#    """
#    任侠道（無印）用サーバーリスト
#    """
#    env.user = "webapp"

@parallel(pool_size = POOL_SIZE)
def restart():
    """
    Add webserver restart code here
    """
    require('app_repo', provided_by=('staging', 'production'))
    with cd(env.app_repo):
        run('touch scripts/*.wsgi')


def _is_sha1(branch):
    """
    check branch is sha1 or not
    """
    try:
        int(branch, 16)
        return True
    except ValueError:
        return False





@parallel(pool_size = POOL_SIZE)
def update_repo():
    """
    Update or create git repo from nfs server
    """
#    require('nfs_host',provided_by=('staging', 'production'))
#    require('nfs_repo', provided_by=('staging', 'production'))
    require('app_repo', provided_by=('staging', 'production'))
    with settings(warn_only = True):
        if run(' test -d %s' % env.app_repo).failed:
            print "?"
            run('git clone https://murabo:murakami408@github.com/murabo/project.git %s' % (
                                           env.app_repo))
        else:
            print "???"
            with cd(env.app_repo):
                print "!!"
                run('git fetch')


@parallel(pool_size = POOL_SIZE)
def checkout(branch = ''):
    """
    checkout to a specific version in deployed server
    """
    require('branch', provided_by=('staging', 'production'))
    require('app_repo', provided_by=('staging', 'production'))
    require('history_file', provided_by=('staging', 'production'))
    require('base_dir', provided_by=('staging', 'production'))
    if not branch:
        branch = env.branch
    with settings(warn_only = True):
        if run('test -d %s' % env.app_repo).succeeded:
            print "1"
            with cd(env.app_repo):
                if _is_sha1(branch):
                    print "2"
                    run('git checkout %s' % branch)
                elif run('git show-ref origin/%s' % branch):
                    print "3"
                    run('git checkout origin/%s' % branch) # branch
                else:
                    print "4"
                    run('git checkout %s' % branch) # TAG
                run('git submodule update -i')
                sha1 = run('git rev-parse HEAD')
                run('echo %s %s>>%s' % (NOW, sha1, env.history_file))
                run('rm %s/%s' % (env.base_dir, 'current'))
                run('ln -sF %s %s/%s' % (env.app_repo, env.base_dir, 'current'))


@runs_once
def deploy(branch = ''):
    """
    Do all in one command
    """
    execute(update_repo)
    execute(checkout, branch)
    execute(restart)







def hello():
    run("uname -s")
    with cd('/etc/'):
        run('pwd')
        with settings(warn_only = True):
            if run('test -d /var/www/cocolink/').failed:
                print "ファイルが無いのでgit clone --mirrorします"


"""
@parallel(pool_size = POOL_SIZE)
def checkout(branch = ''):
    if not branch:
        branch = env.branch
    with settings(warn_only = True):
        with cd('/var/www/'):
            if run('git show-ref origin/%s' % branch):
                run('git checkout origin/%s' % branch)
            else:
                run('git checkout %s' % branch)
"""





