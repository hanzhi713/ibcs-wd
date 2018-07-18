import matplotlib.pyplot as plt
import random
import time

def insertionSort(alist):
### Pseudo-code :  Arr: An Array which is one-based
### for our python implementation, it should be zero-based!!!
### when we call insertionSort(alist), the alist is sorted in itself.
# N = LENGTH(Arr)
# FOR i = 2 TO N
# 	CurValue = Arr[i]
# 	j = i
# 	WHILE j > 1 AND  CurValue < Arr[j-1]
# 		Arr[j] = Arr[j-1]
# 		j = j -1
# 	ENDWHILE
# 	Arr[j] = CurValue
# ENDFOR
### References: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html?highlight=insertion%20sort
    return None


def selectionSort(alist):
### Pseudo-code :  Arr: An Array which is one-based
### for our python implementation, it should be zero-based!!!
### when we call selectionSort(alist), the alist is sorted in itself.
# N = LENGTH(Arr)
# FOR i = 1 TO N-1
# 	MinSub = i
# 	FOR j = i + 1 TO N
# 		IF  Arr[j] < Arr[MinSub]
# 			MinSub = j
# 		ENDIF
# 	ENDFOR
# 	Temp = Arr[i]
# 	Arr[i] = Arr[MinSub]
# 	Arr[MinSub] = Temp
# ENDFOR
### http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html?highlight=selection%20sort
   return None

def bubbleSort(alist):
### Pseudo-code :  Arr: An Array which is one-based
### for our python implementation, it should be zero-based!!!
### when we call bubbleSort(alist), the alist is sorted in itself.
# N = LENGTH(Arr)
# FOR i = 1 TO N-1
# 	FOR j = 1 To N-i
# 		IF Arr[j] > Arr[j+1]
# 			Temp = Arr[j]
# 			Arr[j] = Arr[j+1]
# 			Arr[j+1] = Temp
# 		ENDIF
# 	ENDFOR
# ENDFOR
    return None

## simple test
alist = [54,26,93,17,77,31,44,55,20]
print("original List:", alist)
insertionSort(alist)
print("insertion sort result:",alist)

alist = [54,26,93,17,77,31,44,55,20]
print("original List:", alist)
selectionSort(alist)
print("insertion sort result:",alist)

alist = [54,26,93,17,77,31,44,55,20]
print("original List:", alist)
bubbleSort(alist)
print("insertion sort result:",alist)


## We compare the running time of the 3 basic algorithms.

def CompRunningTimeWithPlot():
    rng = random.Random()
    itemNum = 10
    base = 2
    timeSeqInsertion = []
    timeSeqSelection = []
    timeSeqBubble = []

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

    plt.figure()
    plt.hold(True)
    plt.plot(list(range(itemNum//2,itemNum)), timeSeqInsertion,'r')
    plt.plot(list(range(itemNum//2,itemNum)), timeSeqSelection,'g')
    plt.plot(list(range(itemNum//2,itemNum)), timeSeqBubble,'b')
    plt.show()
### if your 3 basic sorting algorithms are ready, please uncomment the following statement
### to compare their running-time
#CompRunningTimeWithPlot()
