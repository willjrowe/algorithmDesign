#Use a version of Kruskal's algo and Union-Find structure to implement simple k-clustering
import random
from datetime import datetime
from unionFind import UnionFind

#note this is an undirected graph
def generateGraph(n):
    #this graph will be complete by necessity of k-cluter problem
    #graph is represented as a list of lists where each graph[i] represents a node
    #and each graph[i][j] represents the cost or distance between node i and j
    #clearly the graph will be symmetric and graph[i][i] = 0 (the distance to yourself is 0)
    random.seed(datetime.now())
    graph = [[None]*n for _ in range(n)]
    edgeList = []
    for i in range(0,n):
        graph[i][i] = 0 #distance to yourself is 0
        for j in range(i+1,n):
            currDist = random.randint(1,25)
            graph[i][j] = currDist
            graph[j][i] = currDist
            currEdge = (currDist,i,j) #each edge is a tuple of the form (cost,start,end) note start,end is arbitrary since undirected
            edgeList.append(currEdge)
    return graph, edgeList

def runKruskal(graph,edgeList,k):
    #runs kruskal to generate a k-clustering
    #aka groups nodes into k components such that maximizes the spacing between components
    unionFind = UnionFind(list(range(0,len(graph[0]))))
    edgeList.sort(key = lambda x:x[0]) #sort edge list by cost
    while (unionFind.numOfComponents > k):
        currEdge = edgeList.pop(0) #smallest available edge
        startComponent = unionFind.findComponent(currEdge[1]) #component of start node
        endComponent = unionFind.findComponent(currEdge[2])
        if (startComponent != endComponent):
            unionFind.union(startComponent,endComponent)
    cluster = unionFind.listComponents()
    return cluster

#plz ignore how ugly this is
def findSpacing(graph,cluster):
    minSpacing = 100 #start min spacing higher than highest possible edge weight
    for i in range(0,len(cluster)): #for each cluster
        for j in range(0,len(cluster[i])): #for each point in this cluster
            currPoint = cluster[i][j]
            for k in range(i+1,len(cluster)): #look at each other cluster
                for w in range(0,len(cluster[k])): #for each point in this other cluster
                    otherPoint = cluster[k][w]
                    if graph[currPoint][otherPoint] < minSpacing:
                        minSpacing = graph[currPoint][otherPoint]
    return minSpacing

def randomCluster(n,k):
    #generates some random cluster of n nodes into k components
    #use this to 'verify' that runKruskal() is optimal
    cluster = [[] for _ in range(k)]
    nodesUsed = []
    for i in range(0,k): #use this just to make sure each cluster gets at least one node
        currNode = random.randint(0,n-1)
        while (currNode in nodesUsed): #make sure we havent already used this node
            currNode = random.randint(0,n-1)
        nodesUsed.append(currNode)
        cluster[i].append(currNode)
    #randomly distribute the remaining nodes
    for i in range(0,n):
        if i not in nodesUsed:
            nodesUsed.append(i)
            currCluster = random.randint(0,k-1)
            cluster[currCluster].append(i)
    return cluster

a,b = generateGraph(5)
print(a)
c = runKruskal(a,b,2)
print(c)
print(findSpacing(a,c))
d = randomCluster(5,2)
print(d)
print(findSpacing(a,d))
