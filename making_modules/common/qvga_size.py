# -*- coding: utf-8 -*-

import re

#from common import logger

class QvgaSizeMiddleware(object):
    """
    
    qvga-width:60px
    qvga-height="200"
    
    などを検出して、VGA機ならサイズを2倍にする
    
    """
    
    #RE_QVGA_SIZE = re.compile(r"qvga-(width|height):(\d+)px", re.I)
    RE_QVGA_SIZE = re.compile(r"qvga-(width|height)(\s*:\s*|=)([\"\']*)(\d+)([\"\']*)(px|)", re.I)
    
    def process_response(self, request, response):
        
        if not request.path.startswith("/m/"):
            return response
        
        content = response.content
        
        if request.device.display.is_vga():
            #logger.debug("device is vga.")
            content = response.content
            
            def qvga_width_double(m):
                width = int(m.group(4))
                return "%s%s%s%s%s%s" % (m.group(1), m.group(2), m.group(3), width * 2, m.group(5), m.group(6))
            
            content = self.RE_QVGA_SIZE.sub(qvga_width_double, content)
        
        else:
            content = self.RE_QVGA_SIZE.sub(r'\1\2\3\4\5\6', content)
        
        response.content = content
        return response


'''
m = RE_QVGA_SIZE.search("qvga-width:200px")

m = RE_QVGA_SIZE.search("""qvga-width="200")""")

'''