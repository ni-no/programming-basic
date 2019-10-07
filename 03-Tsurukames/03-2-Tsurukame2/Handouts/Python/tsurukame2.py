#!usr/bin/python
# -*- coding: UTF-8 -*-

# tsurukame2.py
# By kota ninomiya

from random import randint

def main():
    for i in range(100):
        total_head = randint(2, 20)
        total_legs = randint(total_head*2, 100)
        crane_legs = randint(1, 3)
        turtle_legs = randint(4, 6)
        num_crane = 0
        num_turtle = 0
        
        # 以下にプログラムを作成せよ
        
        # 最後の出力(if文の条件も埋めよ)
        print('頭が{head}個で，足が{legs}本で'.format(head=total_head, legs=total_legs))
        print('つるの足が{crane}本で，かめの足が{turtle}本のとき'.format(crane=crane_legs, turtle=total_legs))
        if """ 条件を記載 """:
            print('そんな状況はありません')
        else:
            print('鶴は{crane}匹，亀は{turtle}匹です'.format(crane=num_crane, turtle=num_turtle))
        print('\n')
    


if __name__ == '__main__':
    main()