#CHAPTER 1
import random
from datetime import datetime

def createPeople(n):
    #creates an array of n people (could be men or women)
    #returns a list of list formatted in the following way
    #list index 0 represents person 0 
    #the list at index 0 represents person 0's preference ordering
    peopleList = [None] * n
    for i in range(0,n):
        peopleList[i] = createPrefList(n)
    return peopleList

def createPrefList(n):
    #creates a single random preference list of length n
    prefList = list(range(0,n))
    random.shuffle(prefList)
    return prefList

def findWomanEngagement(pairList,woman):
    for i in range(0,len(pairList)):
        if pairList[i][1] == woman:
            return pairList[i], i
    print("UH OH")
    return None

def createStableMatch(n):
    #creates a stable matching between a set of n women and a set of n men
    #n^2 time-ish
    #Gale-Shepley
    #men propose so men are preferred
    random.seed(datetime.now())
    men = createPeople(n)
    women = createPeople(n)
    menEngagementList = [0] * n
    womenEngagementList = [0] * n
    pairList = []
    #0 means a person is 'free' and 1 means a person is 'engaged'
    while 0 in menEngagementList: #while there is a 'free' man 
        currentMan = menEngagementList.index(0) #the first 'free' man appearing in the list
        for i in range(0,n):
            currentWoman = men[currentMan][i] #the ith preferred woman of currentMan
            if womenEngagementList[currentWoman] == 0: #if woman is 'free'
                #engage them
                engagementTuple = (currentMan,currentWoman)
                menEngagementList[currentMan] = 1
                womenEngagementList[currentWoman] = 1
                pairList.append(engagementTuple)
                break
            else:
                #check which man the woman prefers, either the man she is currently engaged to or this new man
                currentManRank = women[currentWoman].index(currentMan)
                currentEngagement, currentEngagementLoc = findWomanEngagement(pairList,currentWoman)
                currentEngagementMan = currentEngagement[0]
                currentEngagementRank = women[currentWoman].index(currentEngagementMan)
                if currentEngagementRank > currentManRank:
                    #woman prefers her current engagement to this man
                    continue
                else:
                    #woman would rather break off her current engagement
                    newEngagementTuple = (currentMan,currentWoman)
                    del pairList[currentEngagementLoc]
                    menEngagementList[currentMan] = 1
                    menEngagementList[currentEngagementMan] = 0
                    pairList.append(newEngagementTuple)
                    break
    return pairList, men, women

def verifyPerfect(matching):
    #a perfect matching contains each man and woman exactly once
    menSeen = []
    womenSeen = []
    for engagement in matching:
        if engagement[0] in menSeen:
            return False
        else:
            menSeen.append(engagement[0])
        if engagement[1] in womenSeen:
            return False
        else:
            womenSeen.append(engagement[1])
    return True


#NEED TO COME BACK TO THIS
def verifyStability(matching, men, women):
    for engagement in matching:
        currentMan = engagement[0]
        currentWoman = engagement[1]


    #a stable matching is perfect and there is no 'instability'
    return None

match1, men1, women1 = createStableMatch(5)
print(men1)
print(women1)
print(match1)
print(verifyPerfect(match1))