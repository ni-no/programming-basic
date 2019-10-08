#!usr/bin/python
# -*- coding: UTF-8 -*-

# kuku2-ans.py
# By kota ninomiya

def create_kuku_table(number:int):
    """九九の表を作成する関数
    
    Args:
        number (int): 上限となる数字
    """
    message = ''
    for i in range(1, number): 
        for j in range(1, number):
            message += '{}*{}='.format(i, j)
            if i*j < 10: message += ' '
            message += '{}, '.format(i*j)
        message = message.rstrip(', ')
        message += '\n'

    print(message)


def main():
    create_kuku_table(10)
        


if __name__ == '__main__':
    main()