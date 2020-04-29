#!/usr/bin/python3
import re

def unisection():
    a = input('lst list: ')
    b = input('2nd list: ')
    
    A = re.sub('[-=+,#/\?:^$.@*’\'\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', a)
    B = re.sub('[-=+,#/\?:^$.@*’\'\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', b)
    
    A = A.split()
    B = B.split()

    set1 = set(A)
    set2 = set(B)

    print("=> union ", set1|set2)
    print("=> intersection ", set1&set2)
