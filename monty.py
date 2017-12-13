  
#-*- coding: utf-8 -*-
from __future__ import division
import logging
from matplotlib import pyplot as plt
import numpy as np
import random


class MontyHall(object):
    """docstring for MontyHall"""

    def __init__(self, num=3):
        """
        创建一个door列表
        0 代表关门
        1 表示后面有车
        -1 代表门被打开
        """
        super(MontyHall, self).__init__()
        self.doors = [0] * num
        self.doors[0] = 1
        self.choice = -1
        self.exclude_car = False
        self.shuffle()

    def shuffle(self):
        """  
        开始新游戏
        重新分配门后的东西
        """
        if self.exclude_car == True:
            self.doors[0] = 1
            self.exclude_car = False
        for i in xrange(len(self.doors)):
            if self.doors[i] == -1:
                self.doors[i] = 0
        random.shuffle(self.doors)

    def make_choice(self):
        """
        player随机选择一扇门
        """
        self.choice = random.randint(0, len(self.doors) - 1)
        logging.info("choice: %d" % self.choice)
        logging.info("original: %s" % self.doors)

    def exclude_doors(self):
        """
        主持人知道门后的情况排除门
        直到剩余两扇门
        """
        to_be_excluded = []
        for i in xrange(len(self.doors)):
            if self.doors[i] == 0 and self.choice != i:
                to_be_excluded.append(i)  
        random.shuffle(to_be_excluded)
        for i in xrange(len(self.doors) - 2):
            self.doors[to_be_excluded[i]] = -1
        logging.info("final: %s" % self.doors)

    def random_exclude_doors(self):
        """
        主持人并不知道门后面的情况随机的开门
        直到剩余两扇门
        """
        to_be_excluded = []
        for i in xrange(len(self.doors)):
            if self.doors[i] != -1 and i != self.choice:
                to_be_excluded.append(i)  
        random.shuffle(to_be_excluded)
        for i in xrange(len(self.doors) - 2):
            if self.doors[to_be_excluded[i]] == 1:
                self.exclude_car = True
            self.doors[to_be_excluded[i]] = -1
        logging.info("final: %s" % self.doors)

    def change_choice(self):
        """
        player改变选择
        """
        to_change = []
        for i in xrange(len(self.doors)):
            if self.doors[i] != -1 and i != self.choice:
                to_change.append(i)
        self.choice = random.choice(to_change)
        logging.info("choice changed: %d" % self.choice)

    def random_choice(self):
        """
        player 第二次随机选择门
        """
        to_select = []
        for i in xrange(len(self.doors)):
            if self.doors[i] != -1:
                to_select.append(i)
        self.choice = random.choice(to_select)
        logging.info("random choice : %d" % self.choice)


    def show_answer(self):
      
        """
        展示门后的情况
        """
        logging.info(self.doors)
        
    def check_result(self):
            """
            验证结果
            """
            got_it = False
            if self.doors[self.choice] == 1:
                got_it = True
            return got_it

    
        

def unknown_doors_choice_test(n):
    """
    主持人并不知道门后面的情况随机的开门
    交换选择的门
    """
    result = {}
    game = MontyHall()
    continue_count = 0
    for i in xrange(n):
            game.shuffle()
            game.make_choice()
            game.random_exclude_doors()
            game.change_choice()
            if game.exclude_car == False:
                continue_count += 1
            if game.check_result():
                result["yes"] = result.get("yes", 0) + 1
            else:
                result["no"] = result.get("no", 0) + 1
        #for key in result:
        #    print "%s: %d" % (key, result[key])
    logging.info("continue_count: %d" % continue_count)
    if continue_count == 0:
        return 0.0
    return result["yes"] / continue_count

    
           

        
if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO,
                        filename='myapp.log')
    results = []
    test_num = 10
    round_num = 10
    for x in xrange(0,round_num):
        results.append(unknown_doors_choice_test(test_num))
        
    print results
    
    

        