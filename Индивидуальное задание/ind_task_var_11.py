#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


def sum_positive(*values):
    """""
    Сумму аргументов, расположенных 
    после первого положительного аргумента.
    """""
    if values:
        pos = 0
        temp = 0
        print(values)
        for i in values:
                if i > 0:
                    pos = i
        for i in values[pos+1:]:
            temp += i
        return temp
    else:
        return None


if __name__ == '__main__':
    print(sum_positive(-1, -1, -2, -3, -4, -5, 6, 7, 8, 5, -1))
