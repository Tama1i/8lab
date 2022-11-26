#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    a = ((int(input("team1 ")),"team1"),(int(input("team2 ")),"team2"),(int(input("team3 ")),"team3"))
    m = [input(" 1 "),input(" 2 "),input(" 3 ")]
    p = True
    k = 0
    
    for i,val in enumerate(m):
        for j in a:
            if m[i] == j[1]:
                m[i] = int(j[0])
            
    for i,val in enumerate(m):
        if int(k < int(val)):
            p = False
        k = m[i]
        
    if  p == False:
        print("ne pravilno")
    else:
        print("pravilno")
   