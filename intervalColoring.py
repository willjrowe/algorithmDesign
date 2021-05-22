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


def earliestStartTime(n,start,finish):
    #generates n intervals between start and finish
    #finds minimum # of resources required to handle all requests
    #returns a list of lists where each list represents a unique resource
    #and the elements in each list representing the intervals they handle
    #n^2 time because I was lazy 
    intervals = createIntervals(n,start,finish) #n time
    intervals.sort(key = lambda x:x[0]) #nlgn
    print(intervals)
    solution = []
    for i in range(0,n):
        validResources = []
        currInterval = intervals[i]
        for j in range(0,len(solution)):
            currValid = True
            for k in range(0,len(solution[j])):
                if currInterval[0] < solution[j][k][1]:
                    currValid = False
            if currValid:
                validResources.append(j)
        if len(validResources) > 0:
            solution[validResources[0]].append(currInterval)
        else:
            solution.append([currInterval])
    return solution


print(earliestStartTime(6,1,10))