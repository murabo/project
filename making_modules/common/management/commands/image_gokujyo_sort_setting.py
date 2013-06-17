# -*- coding: utf-8 -*-
"""
任侠 極女・秘宝画像振り分け
"""
import os
import shutil
from PIL import Image
from django.core.management.base import BaseCommand
from django.conf import settings

#任侠の画像ディレクトリへコピー
#ディレクトリ名、拡張子、幅px,　高さが一致するかチェックする

#コピー元の【ルートディレクトリ名】が、コピー先の画像ディレクトリ以下に存在する名前だと動かない
#「納品」など被らない名前に
#python manage.py image_gokujyo_sort_setting ~/Downloads/納品/ --settings=settings_local

image_size_list = [
    # 基準パス, ディレクトリ名, 拡張子, 幅px, 高さpx
    ('images',  '40', 'GIF',  40,  40),
    ('images', '70', 'GIF',  70, 70),
    ('images', '150_zukan', 'GIF', 140, 140),
    ('images', '240', 'GIF', 240, 200),
    ('images', '240_zukan', 'GIF', 240, 200),
    ('images', 'batting/50', 'GIF', 50, 70),
    ('images', 'batting/175', 'GIF', 175, 200),
    ('images', 'substory', 'GIF', 180, 180),
    ('images', 'treasure', 'GIF', 100, 100),
    ]
file_paths = []


def reprDirInfo(dirpath, indent=0):
    global file_paths
    for path in os.listdir(dirpath):
        full = os.path.join(dirpath,path)
        if os.path.isdir(full):
            reprDirInfo(full,indent+4)
        elif os.path.isfile(full):
            file_paths.append(full)

def getDirPath(file_path, dir_name):

    hierarchy = dir_name.count('/')
    image_dir_list = os.path.dirname(file_path).rsplit('/',1+hierarchy)[1:]

    return "/".join(image_dir_list)

def checkDuplicationPath(src_dir):

    for t in image_size_list:
        if src_dir == t[1]:
            print u"コピー元ルートディレクトリ名を変更してください"
            return False
    return True

def checkAbsolutePath(src_path):

    if src_path.count('/') < 2:
        print u"コピー元ディレクトリは絶対パスで指定してください"
        return False
    return True

def usage():
    print u"コピー元ディレクトリを指定してください"
    print "python ./manage.py image_gokudo_sort_setting [src_dir]"
    return

class Command(BaseCommand):

    def handle(self, *args, **options):
        global file_paths
        if not args:
            usage()
            return

        src_path = args[0]
        reprDirInfo(src_path)

        root_path = "%s" % (settings.MEDIA_ROOT + '/')

        if not checkAbsolutePath(src_path):
            return

        src_dir = os.path.dirname(src_path).rsplit('/',1)[1]

        if not checkDuplicationPath(src_dir):
            return

        for file_path in file_paths:

            try:
                image = Image.open(file_path)
            except IOError:
                #print "IO Error %s" % file_path
                continue

            for category, dir_name, ext, width, height in image_size_list:

                image_dir = getDirPath(file_path, dir_name)

                if image_dir == dir_name and image.size[0] == width and image.size[1] == height and image.format == ext:
                    image_root_path = '%s/%s/gokujo/%s/' % (root_path, category, dir_name)
                    shutil.copy(file_path, image_root_path)
                    print "copy %s to %s" % (file_path, image_root_path)
                    pass
                else:
                    pass