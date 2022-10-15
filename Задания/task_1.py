#!/usr/bin/env python3
# -*- coding: utf-8 -*

import math


def geo_mean(*values):
    if values:
        temp = 1
        for i in range(0, len(values)):
            temp = temp * values[i]
        return math.pow(temp, 1/len(values))
    else:
        return None


if __name__ == "__main__":
    print(geo_mean(1, 2, 3, 4, 5, 6))
