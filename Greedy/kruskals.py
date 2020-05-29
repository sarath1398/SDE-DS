from networkx.exception import NetworkXNoCycle
import networkx as nx

G=nx.Graph() #Create a Graph

#Graph taken from Geeks for Geeks
connections = [(0, 1, 4), (0, 7, 8), (1, 7, 11),
               (1, 2, 8), (2, 8, 2), (7, 8, 7), 
               (7, 6, 1), (8, 6, 6), (2, 5, 4), 
               (6, 5, 2), (2, 3, 7), (3, 5, 14),
               (3, 4, 9), (5, 4, 10), ]

G.add_weighted_edges_from(connections)
count=G.number_of_nodes()
start=0
new_G=nx.Graph()
c=0
connections=sorted(connections,key=lambda tup: tup[2])

while c!=count-1:

    try:
        edge = [connections[start]]
        new_G.add_weighted_edges_from(edge)
        nx.find_cycle(new_G)
    
    except NetworkXNoCycle:
        c+=1
    
    else:
        new_G.remove_edge(edge[0][0],edge[0][1])
    
    start+=1

print(new_G.edges)
