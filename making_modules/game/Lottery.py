#coding:utf-8

class Lottery(object):
    def __init__(self, lucky_point):
        self.lucky_point = lucky_point
        self.lines = {
            'ab':[],
            'bc':[],
            'cd':[],
        }
        self.position = {
            'line': None,
            'height': 0,
        }

    def write_line(self, position, height_flg):
        self.lines[position].append(height_flg)

    def execute(self, choice_line):
        for value in self.lines.values():
            if not value:
                print '線引き忘れてるで'
                raise

        self.position['line'] = choice_line
        self.position_sort()
        exists_next_position = True
        while exists_next_position:
            exists_next_position = self.set_next_position()
        is_lucky = self.result()
        return is_lucky

    def set_next_position(self):
        exists_next_position = False
        next_line, next_height = self.get_next_position()
        if next_height:
            self.set_position(next_line, next_height)
            exists_next_position = True
        return exists_next_position

    def get_line_name(self, key):
        line_name = (key.strip(self.position['line'].lower())).upper()
        return line_name

    def get_next_position(self):
        next_height_dict = {}
        next_height = None
        line = self.position['line'].lower()
        
        for key in self.lines.keys():
            if line in key:
                for height in self.lines[key]:
                　　if self.position['height'] < height:
                        next_height_dict[key] = height
                        break
        if next_height_dict:
            for key, value in next_height_dict.items():
                if next_height == None or value < next_height:
                    line = self.get_line_name(key)
                    next_height = value
        return line, next_height
    
    def set_position(self, line, height):
        self.position['line'] = line
        self.position['height'] = height

    def position_sort(self):
        for key in self.lines.keys():
            self.lines[key].sort()

    def result(self):
        if self.position['line'] == self.lucky_point.upper():
            return True
        return False

    def make_line(self):
        self.write_line('ab',1)
        self.write_line('ab',2)
        self.write_line('bc',3)
        self.write_line('cd',4)

if __name__ =='__main__':
    Lottery = Lottery('b')
    Lottery.make_line()
    is_lucky = Lottery.execute('A')
    print 'is_lucky %s' % is_lucky
