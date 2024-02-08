#Problème du Voyageur de commerce :
#Comment trouver le trajet de coût minimal ?
#Les noeuds du graphe sont des villes, les arêtes les routes empruntables munies d'un poids representant le temps de transport

#%%
import networkx as nx
import matplotlib.pyplot as plt

#créer un graphe orienté
G = nx.DiGraph()

#ajouter des arêtes pondérées à un graphe orienté
G.add_edge(0, 1, weight=3)
G.add_edge(0, 2, weight=9)
G.add_edge(0, 3, weight=9)
G.add_edge(1, 2, weight=5)
G.add_edge(1, 4, weight=22)
G.add_edge(2, 4, weight=13)
G.add_edge(2,5, weight=26)
G.add_edge(2, 6, weight=12)
G.add_edge(3, 6, weight=12)
G.add_edge(4, 5, weight=11)
G.add_edge(4, 7, weight=5)
G.add_edge(4, 8, weight=9)

G.add_edge(5, 9, weight=12)
G.add_edge(5, 10, weight=1)
G.add_edge(6, 11, weight=4)

G.add_edge(7, 12, weight=12)
G.add_edge(7, 8, weight=3)
G.add_edge(8, 12, weight=8)
G.add_edge(8, 14, weight=25)

G.add_edge(9, 8, weight=19)
G.add_edge(9, 15, weight=21)
G.add_edge(10, 16, weight=16)

G.add_edge(11, 17, weight=14)
G.add_edge(12, 13, weight=14)

G.add_edge(13, 14, weight=6)
G.add_edge(14, 15, weight=5)

G.add_edge(15, 16, weight=6)
G.add_edge(17, 18, weight=17)

G.add_edge(18, 16, weight=9)

G.add_edge(16, 19, weight=6)
G.add_edge(15, 19, weight=8)

#On ajoute le nom des villes aux noeuds du graphe :
names = {0:"Bourg-en-Vol",1:"Clementi-Ville",2:"Rosyeres",3:"Merouville",4:"Myokara",5:"Lavandia",6:"Poivressel",
         7:"Vergazon",8:"Vermilava",9:"Cimetronelle",
        10:"Autequia",11:"Site Meteore",12:"Algatia",13:"Nenucrique",14:"Atalanopolis",15:"Route Victoire",16:"Pacifiville",
        17:"Piste cyclable", 18:"Epicea", 19:"Eternara"}
G =nx.relabel_nodes(G,names)

#%%
#Algo qui calcule les positions des noeuds dans le graphe G et qui minimise les croisements d'arêtes en simulant des forces de répulsion et d'attraction entre les noeuds.
pos = nx.fruchterman_reingold_layout(G)

plt.figure(figsize = (20, 10))
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, edge_color = "#75DFC1")
nx.draw_networkx_labels(G, pos)

plt.show();

#%%
#Solution problème voyageur de commerce = Algorithme de Dijkstra :

# Affiche l'ensemble des plus courts chemin depuis le premier noeud du graphe:
chemins_optis_from_1 = nx.shortest_path(G, source="Clementi-Ville", weight='weight')

# Affiche l'ensemble des plus court chemin reliant le premier au 10 ème sommet
chemin_1to10 = nx.shortest_path(G, source="Clementi-Ville", target="Cimetronelle", weight='weight')

# Affiche la longueur des plus court chemin reliant le premier au 10 ème sommet
dist_min_1to10 = nx.shortest_path_length(G, source="Clementi-Ville", target="Cimetronelle", weight='weight')

print("All shortest paths from 1: " , chemins_optis_from_1)
print("Shortest path from 1 to 10: ", chemin_1to10)
print("Length of the shortest path: " ,dist_min_1to10)


#%%
#Affichage de la solution du probleme du plus court chemin :
plt.figure(figsize = (20, 10))
nx.draw(G,pos,node_color='blue',edge_color="#75DFC1",with_labels=True)

# plus court chemin dessiné en rouge :
chemin_min = nx.shortest_path(G,source="Bourg-en-Vol",target="Eternara")
chemin_min_edges = list(zip(chemin_min,chemin_min[1:]))

nx.draw_networkx_nodes(G,pos,nodelist=chemin_min,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=chemin_min_edges,edge_color='r',width=5)
plt.axis('equal')
plt.show()

