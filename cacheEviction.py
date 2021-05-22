#simplified cache eviction using farthest-in-future approach
import random
from datetime import datetime

resources = ['a','b','c','d','e','f']

def createMemRef(n):
    #creates a list of n random memory references
    #a memory reference is a list of requests for certain resources
    #resources here will be from the set {a,b,c,d,e,f}
    random.seed(datetime.now())
    refList = []
    for i in range(0,n):
        currResource = random.choice(resources)
        refList.append(currResource)
    return refList

def farthestInFuture(n,k):
    #creates a random memory reference list of len n
    #creates a cache of size k (k < n)
    #generates an eviction list that minimizes the number of cache misses
    #a miss occurs when a resource is requested that is not in the cache
    #typically initially fill the cache with random elements from resources
    #to make analysis easier assume cache always starts with first k letters of alphabet
    evictionList = []
    #the eviction list will consist of tuples of the following form
    #(time the eviction occured, element removed from cache, element added)
    currCache = []
    for i in range(0,k):
        currCache.append(resources[i])
    memList = createMemRef(n)
    print(memList)
    for i in range(0,len(memList)):
        if memList[i] in currCache:
            continue
        else:
            #find element in cache that is needed the farthest in the future from now
            farthestAwayTime = 0
            farthestAwayElement = currCache[0]
            for j in currCache:
                if j in memList[i+1:]:
                    currAwayTime = memList.index(j,i+1)
                else:
                    currAwayTime = 100 #if we never need this element again then we know it's very 'far' away
                if currAwayTime > farthestAwayTime:
                    farthestAwayTime = currAwayTime
                    farthestAwayElement = j
            currEviction = (i, farthestAwayElement, memList[i])
            currCache.remove(farthestAwayElement) #remove farthest element from cache
            currCache.append(memList[i]) #add newest element to cache
            evictionList.append(currEviction)
    return evictionList


a = farthestInFuture(7,3)
print(a)