class Node(object):
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def add_connection(self, child, distance):
        self.children.append((child,distance))

    def get_children(self):
        return self.children
    
    def __repr__(self):
        return self.name

E = Node("E")
A = Node("A")
D = Node("D")
C = Node("C")
B = Node("B")
mini = [E,A,C,B,D]
E.add_connection(A,7)
D.add_connection(A,60)
A.add_connection(C,12)
C.add_connection(B,20)
B.add_connection(A,10)
C.add_connection(D,32)


London = Node("London")
Southampton = Node("Southampton")
Dover = Node("Dover")
Calais = Node("Calais")
Lille = Node("Lille")
Paris = Node("Paris")
LeHavre = Node("Le Havre")
Brussels = Node("Brussels")
Luxembourg = Node("Luxembourg")
Metz = Node("Metz")
Genz = Node("Genz")
Antwerp = Node("Antwerp")
Rotterdam = Node("Rotterdam")
Dijon = Node("Dijon")
Strasbourg = Node("Strasbourg")

cities = [London,Southampton,Dover,Calais,Lille,Paris,LeHavre,Brussels,Luxembourg,Strasbourg,Genz,Antwerp,Rotterdam,Dijon,Metz]

London.add_connection(Southampton,127)
London.add_connection(Dover,122)
Dover.add_connection(Calais,87)
Calais.add_connection(Lille,109)
Lille.add_connection(Paris,250)
Paris.add_connection(LeHavre,197)
Paris.add_connection(Metz,360)
Lille.add_connection(Brussels,118)
Brussels.add_connection(Antwerp,55)
Antwerp.add_connection(Rotterdam,100)
Brussels.add_connection(Luxembourg,120)
Luxembourg.add_connection(Metz,95)
Metz.add_connection(Dijon,269)
Metz.add_connection(Strasbourg,166)


def run_dijkstra(nodes):
    Q = [((nodes[0],),0)]
    while Q != []:
        imin = 0
        vmin = None
        for i in range(len(Q)):
            if vmin is None or Q[i][1] < vmin:
                vmin = Q[i][1]
                imin = i
        path, dist = Q.pop(imin)
        curr = path[-1]
        for child, next_dist in curr.get_children():
            if child == nodes[-1]:
                return path+(child,)
            elif child not in path:
                new_path = path+(child,)
                Q.append((new_path,dist+next_dist))
    return None

pos = run_dijkstra(mini)
print(pos)

pos = run_dijkstra(cities)
print(pos)
