# encoding:utf-8

from cocolink.post.models import Post

class ajax_api(object):
    
    @classmethod
    def insert_post(cls, request):

        if request.user:
            user_id = request.user.id


            message = request.POST.message

            if message:
                try:
                    Post(user_id = user_id, body_text = message, )
                except:
                    result_code = 2
                    
                Post.save()
                result_code = 1
        else:
            result_code = 2

        ctxt = {"result_code": result_code,
                }
        return ctxt

