# 16. Ученик выучил в первый день 5 английских слов. В каждый следующий день он выучивал на
# 2 слова больше, чем в предыдущий. Сколько английских слов выучит ученик в 10-ый день
# занятий.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    a = 1
    s = 5
    d = s
    while a < 10:
        d += 2
        s += d
        a += 1
    print(s)
