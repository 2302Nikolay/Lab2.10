#!/usr/bin/env python3
# -*- coding: utf-8 -*


def mean_gar(*values):
    print(values)
    if values:
        temp = 0
        for i in range(0, len(values)):
            temp = temp + 1/values[i]
        return len(values)/temp
    else:
        return None


if __name__ == "__main__":
    print(mean_gar(1, 2, 3, 4, 5, 6))
