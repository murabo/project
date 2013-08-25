# encoding:utf-8

from gu.models import GuPost

class ajax_api(object):
    
    @classmethod
    def insert_post(cls, request):

        if request.user:
            user_id = request.user.id

            message = request.POST.message

            if message:
                try:
                    GuPost(user_id = user_id, body_text = message, )
                except:
                    result_code = 2
                    
                GuPost.save()
                result_code = 1

        else:
            result_code = 2

        ctxt = {"result_code": result_code,
                }
        return ctxt

