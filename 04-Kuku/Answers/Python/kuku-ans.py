#!usr/bin/python
# -*- coding: UTF-8 -*-

# kuku-ans.py
# By kota ninomiya

def main():
    message = ''
    for i in range(1, 10): 
        for j in range(1, 10):
            message += '{}*{}='.format(i, j)
            if i*j < 10: message += ' '
            message += '{}, '.format(i*j)
        message = message.rstrip(', ')
        message += '\n'

    print(message)
        


if __name__ == '__main__':
    main()