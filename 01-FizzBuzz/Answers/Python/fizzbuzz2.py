#!usr/bin/python
# -*- coding: UTF-8 -*-

# fizzbuzz2.py
# By kota ninomiya

def fizz_buzz(number:int) -> str:
    """fizzbuzzを判断し，その結果を返す．該当しない場合は数字を返す
    
    Args:
        number (int): 検証する値
    
    Returns:
        str: Fizz, Buzz, Fizz Buzz or numer
    """
    if number%15 == 0: return 'Fizz'
    if number%3 == 0: return 'Buzz'
    if number%5 == 0: return 'Fizz Buzz'
    return str(number)

def main():
    for i in range(1, 201):
        print(fizz_buzz(i))


if __name__ == '__main__':
    main()