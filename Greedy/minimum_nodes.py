import networkx as nx 
from networkx.algorithms.shortest_paths.weighted import dijkstra_path 

G=nx.Graph()

connections = [ (0, 1, 1), (0, 7, 1), (1, 7, 1),
                (1, 2, 1), (2, 8, 1), (7, 8, 1),
                (7, 6, 1), (8, 6, 1), (2, 5, 1),
                (6, 5, 1), (2, 3, 1), (3, 5, 1),
                (3, 4, 1), (5, 4, 1), ] #Assume Weight=1 for all connected vertices 

G.add_weighted_edges_from(connections)

src, dest = map(int, input().split())

distance=dijkstra_path(G,src,dest)

print(len(distance)-1)



