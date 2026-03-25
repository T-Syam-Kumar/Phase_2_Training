class Graph:
     def __init__(self,size):
         self.size = size
         self.graph = [[0]*size for i in range(size)]
         self.dic = {"S":0 ,"K":1 ,"P":2 ,"R":3 ,"H":4 ,"B":5 ,"C":6}

     def insert(self,s,d):
         row = self.dic[s]
         col = self.dic[d]
         self.graph[row][col] = 1
         self.graph[col][row] = 1


person1 = Graph(7)
route = [("S","K"),("S","P"),("S","R"),("K","P"),("R","H"),("R","C"),("H","B"),]

for s,d in route:
    person1.insert(s,d)

for i in range(7):
    print(person1.graph[i])




class Graph:
    def __init__(self):
        self.graph = {}

    def insert(self,s,d):
        for i in range(2):
            if s in self.graph:
                self.graph[s].append(d)
            else:
                self.graph[s] = [d]
            s  , d = d, s




person1 = Graph()
route = [("S","K"),("S","P"),("S","R"),("K","P"),("R","H"),("R","C"),("H","B"),]

for s,d in route:
    person1.insert(s,d)

print(person1.graph)
