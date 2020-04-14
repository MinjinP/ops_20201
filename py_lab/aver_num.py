if __name__ == '__main__':
    num = int(input("N = "))

    numList=[]

    for a in range(num):
        numList.append(int(input("input : ")))
        
    sum=0

    for a in numList:
        sum+=a

    ave = sum/num

    print("ave = %d" %ave)
