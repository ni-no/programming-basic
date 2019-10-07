#!usr/bin/python
# -*- coding: UTF-8 -*-

# tsurukame1-ans.py
# By kota ninomiya

from random import randint

def main():
    for i in range(100):
        total_head = randint(2, 30)
        total_legs = randint(total_head*2, 100)
        num_crane = 0
        num_turtle = 0
        isError = True
        
        # 以下にプログラムを作成せよ
        while num_crane < total_head:
            num_turtle = total_head - num_crane
            if num_crane*2 + num_turtle*4 == total_legs:
                isError = False
                break
            num_crane += 1
        
        # 最後の出力(if文の条件も埋めよ)
        print('頭が{head}個で，足が{legs}本のとき'.format(head=total_head, legs=total_legs))
        if isError:
            print('そんな状況はありません')
        else:
            print('鶴は{crane}匹，亀は{turtle}匹です'.format(crane=num_crane, turtle=num_turtle))
        print('\n')
    


if __name__ == '__main__':
    main()