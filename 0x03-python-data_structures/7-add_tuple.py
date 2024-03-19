#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tpl_len1 = len(tuple_a)
    tpl_len2 = len(tuple_b)
    tuple_a = tuple_a[:2] if tpl_len1 > 2 else tuple_a + (0,) * (2 - tpl_len1)
    tuple_b = tuple_b[:2] if tpl_len2 > 2 else tuple_b + (0,) * (2 - tpl_len2)
    tuple_total1 = tuple_a[0] + tuple_b[0]
    tuple_total2 = tuple_a[1] + tuple_b[1]

    return tuple_total1, tuple_total2
