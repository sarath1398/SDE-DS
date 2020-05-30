import random
import networkx as nx 

G=nx.Graph() #Create a Graph
New_G=nx.Graph()

#Graph taken from Geeks for Geeks
connections = [(0, 1, 4), (0, 7, 8), (1, 7, 11),
               (1, 2, 8), (2, 8, 2), (7, 8, 7), 
               (7, 6, 1), (8, 6, 6), (2, 5, 4), 
               (6, 5, 2), (2, 3, 7), (3, 5, 14),
               (3, 4, 9), (5, 4, 10), ]

G.add_weighted_edges_from(connections)
INF = 9999999
V = G.number_of_nodes()

selected = [0]*V
no_edge = 0
selected[0] = True

while (no_edge < V - 1):

    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                try:
                    if ((not selected[j]) and G[i][j]['weight']):
                        if minimum > G[i][j]['weight']:
                            minimum = G[i][j]['weight']
                            x = i
                            y = j

                except KeyError:
                    continue

    New_G.add_weighted_edges_from([(x,y,G[x][y]['weight'])])
    selected[y] = True
    no_edge += 1

print(New_G.edges)

