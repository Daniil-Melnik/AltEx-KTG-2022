import random
import networkx as nx
import matplotlib.pyplot as plt

BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

V=['a','b','c','d']

G = nx.Graph()
G.add_nodes_from(V)

G.add_edge('a', 'b')
G.add_edge('c', 'b')
G.add_edge('d', 'b')
G.add_edge('d', 'c')

nx.draw_circular(G, with_labels = True)
plt.axis('on')
plt.show()

nAdd = 5
for i in range (nAdd):
    D=0
    for v in G.nodes():
        D+=G.degree(v)
    D=D//2
    ProbV = []
    v0=BV[len(V)+1]
    G.add_node(v0)

    for v in V:
        ProbV.append(G.degree(v)/(D*2))

    for i in range(len(V)):
        for j in range(len(V)-1):
            if (ProbV[j]<ProbV[j+1]):
                a, b = V[j], ProbV[j]
                V[j], ProbV[j] = V[j+1], ProbV[j+1]
                V[j+1], ProbV[j+1] = a, b

    m=random.randint(1,len(V))

    V.append(v0)
    for i in range(m):
        G.add_edge(V[i], v0)

    nx.draw_circular(G, with_labels = True)
    plt.axis('on')
    plt.show()

#m=random.randint(1,len(G.nodes()))



#nx.draw_random(G, with_labels = True)
#plt.axis('on')
#plt.show()