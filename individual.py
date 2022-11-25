#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a1 = (int(input("team1 ")),"team1")
    a2 = (int(input("team2 ")),"team2")
    a3 = (int(input("team3 ")),"team3")
    m = [input(" 1 "),input(" 2 "),input(" 3 ")]
    p = True

    for i,val in enumerate(m):
        if m[i] == a1[1]:
            m[i] = int(a1[0])
        if m[i] == a2[1]:
            m[i] = int(a2[0])
        if m[i] == a3[1]:
            m[i] = int(a3[0])
    for i in range(0,1):
        if int(m[i]) < int(m[i+1]):
            p = False
        
    if  p == False:
        print("ne pravilno")
    else:
        print("pravilno")
   