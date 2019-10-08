#!usr/bin/python
# -*- coding: UTF-8 -*-

# kuku2-ans.py
# By kota ninomiya

from math import floor, log10

def create_kuku_table_auto_format(number:int):
    """九九の表を作成する関数
    
    Args:
        number (int): 上限となる数字
    """
    message = ''
    term_digit = floor(log10(number-1))
    answer_digit = floor(log10((number-1)**2))
    for i in range(1, number): 
        for j in range(1, number):
            message += '{}{}*'.format(auto_format_digits(i, term_digit), i)
            message += '{}{}='.format(auto_format_digits(j, term_digit), j)
            message += '{}{}, '.format(auto_format_digits(i*j, answer_digit), i*j)
        message = message.rstrip(', ')
        message += '\n'
    print(message)


def auto_format_digits(verify_value:int, digit:int):
    """桁数をスペースで埋め合わせる関数
    
    Args:
        verify_value (int): 検証する値
        digit (int): 桁数
    """
    numOfFill = digit - floor(log10(verify_value))
    spaces  = ''
    for i in range(numOfFill):
        spaces += ' '
    return spaces


def main():
    create_kuku_table_auto_format(11)
        


if __name__ == '__main__':
    main()