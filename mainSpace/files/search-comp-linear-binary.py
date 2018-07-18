import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for i in range(len(xs)):
       if xs[i]== target:
           return i
    return -1

def search_binary_iter(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:   # If region of interest (ROI) becomes empty
           return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2   #

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #        .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index      # Found it!
        if item_at_mid < target:
            lb = mid_index + 1    # Use upper half of ROI next time
        else:
            ub = mid_index        # Use lower half of ROI next time

# def search_binary_recur(xs, target):
#     if len(xs) == 0:
#         return -1
#     else:
#         mid_index = len(xs)//2
#         if xs[mid_index]==target:
#              return mid_index
#         else:
#             if target<xs[mid_index]:
#                 return search_binary_recur(xs[:mid_index],target)
#             else:
#                 return search_binary_recur(xs[mid_index+1:],target)

def search_binary_recur(xs, target,lb, ub):
   # if ub == None: ub = len(xs)-1
    if lb == ub:
        return -1
    mid_index = lb + (ub - lb) // 2
    if xs[mid_index] == target:
        # print("recur ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub - lb, xs[mid_index], target))
        return mid_index
    else:
        if xs[mid_index]<target:
            lb = mid_index+1
            return search_binary_recur(xs,target,lb, ub)
        else:
            ub = mid_index - 1
            return search_binary_recur(xs,target,lb,ub)


def test():
    global testSeq
    # print(testSeq)
    target = random.choice(testSeq)
    search_linear(testSeq, target)

def test_binary_iter():
    global testSeq
    # print(testSeq)
    target = random.choice(testSeq)
    search_binary_iter(testSeq, target)

def test_binary_recur():
    global testSeq
    # print(testSeq)
    target = random.choice(testSeq)
    search_binary_recur(testSeq, target,0,len(testSeq)-1)

if __name__=='__main__':
    global testSeq
    testNumber = 1000
    NumList = list(range(10000, 11000, 1000))
    # t1 = timeit.Timer("test()","from __main__ import test")
    # print(t1.timeit(1000))
    timeList = []
    timeList_bin_recur = []
    timeList_bin_iter = []

    for TotalNum in NumList:
        testSeq = list(range(TotalNum))
     #   random.shuffle(testSeq)

        timeList.append(timeit.timeit("test()","from __main__ import test",  number=testNumber))
        timeList_bin_recur.append(timeit.timeit("test_binary_recur()", "from __main__ import test_binary_recur", number=testNumber))
        timeList_bin_iter.append(timeit.timeit("test_binary_iter()", "from __main__ import test_binary_iter", number=testNumber))

    plt.figure(1)
  #  plt.title('')
    plot1 = plt.plot(NumList, timeList, 'ro',markersize = 15,label = 'linear')
    plt.plot(NumList, timeList, 'r')
    plot2 = plt.plot(NumList, timeList_bin_recur, 'g*',markersize = 15,label = 'binary_recur')
    plt.plot(NumList, timeList_bin_recur, 'g')
    plot2 = plt.plot(NumList, timeList_bin_iter, 'bx',markersize = 15,label = 'binary_iter')
    plt.plot(NumList, timeList_bin_iter, 'b')
    plt.xlabel('length of searching lists')
    plt.ylabel('running time (s)')
    plt.axis([0, round(max(NumList),-1)*1.1, 0, max(timeList)*1.1])
    plt.legend(loc='upper left', numpoints=1)
    plt.show()
