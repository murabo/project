#coding:utf-8


class Post(object):
    def __init__(self ,player_id):
        self.key = 'key:%s' % player_id 
        self.redisapi = RedisApi()

    def get_postlist(self):
        self.redisapi.get_dict(self.key)

    def append_post(self, date):
        self.redisapi.append(self.key, date) 


class PostDetail(Object):
    def __init__(self):
        pass

    def get_merge_post(self, player_id):
        postlist = Post(player_id).get_postlist()
        friend_userids = player.get_friend_users()
        postlist2 =  

    















