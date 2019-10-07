#!usr/bin/python
# -*- coding: UTF-8 -*-

# fizzbuzz.py
# By kota ninomiya

def main():
    for i in range(1, 201):
        if i%3 == 0: 
            print('Fizz')
        elif i%5 == 0: 
            print('Buzz')
        elif i%15 == 0: 
            print('Fizz Buzz')
        else: 
            print(str(i))


if __name__ == '__main__':
    main()