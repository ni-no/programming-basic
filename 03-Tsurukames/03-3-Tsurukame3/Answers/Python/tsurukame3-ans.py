#!usr/bin/python
# -*- coding: UTF-8 -*-

# tsurukame3-ans.py
# By kota ninomiya

from random import randint

def checkCraneAndTurtle(total_legs:int, total_head:int, crane_legs:int, turtle_legs:int):
    """Count the number of cranes and turtles.
    
    Args:
        total_legs (int): The number of total legs.
        total_head (int): The number of total heads.
        crane_legs (int): The number of crane's legs.
        turtle_legs (int): The number of tutle's legs.
    """
    print('頭が{head}個で，足が{legs}本で'.format(head=total_head, legs=total_legs))
    print('つるの足が{crane}本で，かめの足が{turtle}本のとき'.format(crane=crane_legs, turtle=total_legs))
    num_of_pairs = 0
    
    # ここに色々処理を書く
    # 以下にプログラムを作成せよ
    num_crane = 0
    while num_crane < total_head:
        num_turtle = total_head - num_crane
        if num_crane*crane_legs + num_turtle*turtle_legs == total_legs:
            num_of_pairs += 1
        num_crane += 1
    
    if num_of_pairs == 1:
        print('鶴は{crane}匹，亀は{turtle}匹です'.format(crane=num_crane, turtle=num_turtle))
    else :
        print('そんな状況はありません')
    print('\n')


def main():
    checkCraneAndTurtle( 10, 32, 2, 4 ) # 「鶴が4匹，亀が6匹」と出力
    checkCraneAndTurtle( 65, 52, 18, 76 ) # 「そんな状況はありません」と出力
    checkCraneAndTurtle( 90, 8, 46, 47 ) # 「そんな状況はありません」と出力
    checkCraneAndTurtle( 4, 12,3, 3 ) # 「そんな状況はありません」と出力
    checkCraneAndTurtle( 2, 2, 1, 1 ) # 「鶴が1匹，亀が1匹」と出力
    for i in range(100):
        _total_head = randint(2, 20)
        _total_legs = randint(2, 50)
        _crane_legs = randint(1, 10)
        _turtle_legs = randint(1, 10)
        checkCraneAndTurtle(_total_head, _total_legs, _crane_legs, _turtle_legs)
        
    


if __name__ == '__main__':
    main()