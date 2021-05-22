#intervals now have a time t_i
#t_i is the amount of time needed to complete a job (contiguously)
#intervals also have a deadline d_i 
#lateness = l_i = f_i - d_i
#note late if f_i > d_i


import builtins
import random
from datetime import datetime

def createJobs(n,maxDeadline,maxTime):
    #jobs are tuples of the following form
    #job = (deadline, time required to complete job)
    random.seed(datetime.now()) #just to get new seed
    jobs = []
    for i in range(0,n):
        currDeadline = random.randint(1,maxDeadline)
        currTime = random.randint(1,maxTime)
        currJob = (currDeadline,currTime)
        jobs.append(currJob)
    return jobs

def earliestDeadline(n,maxDeadline,maxTime):
    #minimizes the lateness of some n set of jobs using earliest deadline first
    intervals = createJobs(n,maxDeadline,maxTime) #n time
    intervals.sort(key = lambda x:x[0]) #nlgn
    return intervals


def calculateLateness(schedule):
    #calculates the lateness of some schedule of jobs
    currTime = 0 #default start time to time zero
    maxLateness = 0
    for i in range(0,len(schedule)):
        currTime += schedule[i][1]
        if currTime > schedule[i][0]:
            maxLateness = max(currTime - schedule[i][0],maxLateness)
    return maxLateness
    

a = earliestDeadline(5,10,25)
print(a)
print(calculateLateness(a))
b = random.sample(a,len(a))
print(b)
print(calculateLateness(b))