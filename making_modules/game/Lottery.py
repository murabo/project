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

    def get_lucky_result(self, choice_line)
        self.position['line'] = choice_line
        while self.get_next_line(choice_line):
            # 移動

    def get_next_line(self, choice_line):
        if choice_line == 'A':
            lines = self.lines['ab']
        elif choice_line == 'B':
            lines = self.lines['bc']
        elif choice_line == 'C':
            lines = self.lines['cd']
        elif choice_line == 'D':
            lines = self.lines['cd']

if __name__ =='__main__':
    Lottery = Lottery('a')
    Lottery.write_line('ab',1)
    Lottery.write_line('bc',2)
    Lottery.write_line('cd',3)
    is_lucky = Lottery.get_lucky_result('C')






