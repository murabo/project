#coding:utf-8

class Lottery(object):
    def __init__(self, lucky_point):
        self.lucky_point = None
        self.lines = {
            'ab':[],
            'bc':[],
            'cd':[],
        }
        self.position = {
            'line': None,
            'height': None,
        }

    def write_line(self, position, height_flg):
        self.lines[position].append(height_flg)

    def execute(self, choice_line)
        self.position['line'] = choice_line
        while self.get_next_line(choice_line):
            # 移動
        is_lucky = self.judge_lucky_result()
        return is_lucky

    def get_next_line(self, choice_line):
        line = choice_line.lower()
        for key in self.lines.keys():
            if line in key:
                #次のラインを取得
                if next_position == None or self.position[height] > get_next_height():
                    self.set_position(line,height)

    def set_position(self, line, height):
        self.position['line'] = line
        self.position['height'] = height

    def judge_lucky_result(self):
        if self.position['line'] == self.lucky_point.upper():
            return True
        return False
        

if __name__ =='__main__':
    Lottery = Lottery('a')
    Lottery.write_line('ab',1)
    Lottery.write_line('bc',2)
    Lottery.write_line('cd',3)
    is_lucky = Lottery.get_lucky_result('C')






