#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def each_ascii(s):
    for ch in s:
        yield ord(ch)
    return '%s chars' % len(s)

def yield_from(s):
    r = yield from each_ascii(s)
    print(r)

def main():
    for x in each_ascii('abc'):
        print(x) # => 'a', 'b', 'c'
    it = each_ascii('xyz')
    try:
        while True:
            print(next(it)) # => 'x', 'y', 'z'
    except StopIteration as s:
        print(s.value) # => '3 chars'

    # using yield from in main() will change main() from function to generator:
    # r = yield from each_ascii('hello')

    for ch in yield_from('hello'):
        pass

main()

# 彻底理解Python中的yield ： https://www.jianshu.com/p/d09778f4e055
def triangles():
    N=[1]
    while True:
        yield N
        N.append(0)
        N=[N[i-1] + N[i] for i in range(len(N))]
n=0
for t in triangles():
    print(t)
    n=n+1
    if n == 10:
        break


def triangle():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]
n = 0
for t in triangle():
    print(t)
    n = n + 1
    if n == 10:
        break

