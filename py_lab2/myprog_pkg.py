#!/usr/bin/python3
import conversion as cv
import unisection as us
if __name__ == "__main__":

    n=int(input('Select menu: 1) conversion 2) union/intersection 3) exit? '))
    
    while n!=3:
        if n==1:
            a = int(input("input binary number : "), 2)
            cv.conversion(a)

        if n==2:
            us.unisection()

        n=int(input('Select menu: 1) conversion 2) union/intersection 3) exit? '))

    if n==3:
        print("exit the program...")
