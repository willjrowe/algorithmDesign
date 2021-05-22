import random
from datetime import datetime

def createIntervals(n,start,finish):
    random.seed(datetime.now()) #just to get new seed
    intervals = []
    for i in range(0,n):
        currStart = random.randint(start,finish-1)
        currFinish = random.randint(currStart+1,finish)
        currInterval = (currStart,currFinish)
        intervals.append(currInterval)
    return intervals


def earliestFinishTime(n,start,finish):
    #generates n intervals between start and finish
    #finds the maximum # of intervals that can be scheduled and are 'compatible' in the standard sense
    #n^2 time because I was lazy 
    #to get nlgn use auxillary array to track start times and iterate that once, then sorting dominates
    intervals = createIntervals(n,start,finish) #n time
    intervals.sort(key = lambda x:x[1]) #nlgn
    solution = []
    print(intervals)
    while len(intervals) > 0: #while there still is a valid interval
        currInterval = intervals[0] #choose earliest finishtime
        solution.append(currInterval)
        toDelete = [0] #just to track which elements to delete
        for i in range(1,len(intervals)): #n
            if intervals[i][0] < currInterval[1]:
                toDelete.insert(0,i)
        for x in toDelete:
            del intervals[x]
    return solution


print(earliestFinishTime(6,1,10))