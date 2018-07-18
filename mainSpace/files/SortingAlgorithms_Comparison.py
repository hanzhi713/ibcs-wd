import matplotlib.pyplot as plt
import random
import time

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1



## We compare the running time of the 3 basic algorithms.

def CompRunningTimeWithPlot():
    rng = random.Random()
    itemNum = 10
    base = 2
    timeSeqInsertion = []
    timeSeqSelection = []
    timeSeqBubble = []
    timeMerge = []
    for i in range(itemNum//2,itemNum):
        alist = list(range(base**i))
        rng.shuffle(alist)
        t0 = time.clock()
        insertionSort(alist)
        t1 = time.clock()
        print("The list has {} items, it takes {} seconds by insertion sort.".format(base**i, t1-t0))
        timeSeqInsertion.append(t1-t0)

        rng.shuffle(alist)
        t0 = time.clock()
        selectionSort(alist)
        t1 = time.clock()
        print("The list has {} items, it takes {} seconds by Selection sort.".format(base ** i, t1 - t0))
        timeSeqSelection.append(t1-t0)

        rng.shuffle(alist)
        t0 = time.clock()
        bubbleSort(alist)
        t1 = time.clock()
        print("The list has {} items, it takes {} seconds by Bubble sort.".format(base ** i, t1 - t0))
        timeSeqBubble.append(t1-t0)

        rng.shuffle(alist)
        t0 = time.clock()
        mergeSort(alist)
        t1 = time.clock()
        print("The list has {} items, it takes {} seconds by Bubble sort.".format(base ** i, t1 - t0))
        timeMerge.append(t1 - t0)

    plt.figure()
    plt.hold(True)
    plt.plot(list(range(itemNum//2,itemNum)), timeSeqInsertion,'r',label=u'insertion')
    plt.plot(list(range(itemNum//2,itemNum)), timeSeqSelection,'g',label=u'selection' )
    plt.plot(list(range(itemNum//2,itemNum)), timeSeqBubble,'b',label=u'bubble')
    plt.plot(list(range(itemNum // 2, itemNum)), timeMerge, 'm',label=u'merge')
    plt.legend(loc='upper center')
    plt.show()
### if your 3 basic sorting algorithms are ready, please uncomment the following statement
### to compare their running-time
CompRunningTimeWithPlot()
