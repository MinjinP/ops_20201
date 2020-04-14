#!/usr/bin/python3
import sys

if __name__=='__main__':
    num = int(input("fibonacci number? "))
    
    fiboList = [0, 1]
    
    if (num>2) :
        for i in range(2, num+1):
            y = fiboList[i-1]+fiboList[i-2]
            fiboList.append(y)

    for i in range(1, num+1) :
            print(fiboList[i], end=", ")

    print("")

    print("F%d = %d" % (num, fiboList[num]))
