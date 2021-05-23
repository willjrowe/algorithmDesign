class UnionFind:
    #simple array implementation could be improved using a pointer system, but im lazy and don't want to do handles

    def __init__(self,S) -> None:
        #Takes some set S of n nodes
        #Analogous to MakeUnionFind
        component = [None] * len(S)
        for i in range(0,len(S)):
            component[i] = S[i]
        self.size = [1] * len(S)
        self.component = component
        self.numOfComponents = len(S)

    #constant time lookup
    def find(self,u):
        #u is some node
        #assume u is identified by an int between 0 and n (uniquely)
        return self.component[u]

    def findComponent(self,u):
        A = [u]
        uComponent = self.find(u)
        for i in range(0,len(self.component)):
            if i!= u and uComponent == self.find(i):
                A.append(i)
        return A

    def listComponents(self):
        labeling = {}
        components = []
        for i in range(0,len(self.component)):
            currComponent = self.find(i)
            if currComponent in labeling:
                components[labeling[currComponent]].append(i)
            else:
                components.append([i])
                labeling[currComponent] = len(components) - 1
        return components

    #linear time
    def union(self,A,B):
        #A, B are sets of nodes (assume non empty)
        #sets here are lists of ints where each int represents a unique node
        Asize = self.size[A[0]]
        Bsize = self.size[B[0]]
        totalSize = Asize + Bsize
        if Asize > Bsize:
            Aname = self.component[A[0]]
            for node in B:
                self.component[node] = Aname
        else:
            Bname = self.component[B[0]]
            for node in A:
                self.component[node] = Bname
        for node in A:
            self.size[node] = totalSize
        for node in B:
            self.size[node] = totalSize
        self.numOfComponents = self.numOfComponents - 1
        return True

    def printAll(self):
        print("Components")
        print(self.component)
        print("Size")
        print(self.size)
    

# S = list(range(0,10))
# a = UnionFind(S)
# a.union([1],[2])
# a.union([1,2],[7])
# a.printAll()
# print(a.find(7))

    