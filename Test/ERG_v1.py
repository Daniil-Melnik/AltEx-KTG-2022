import random
import networkx as nx
import matplotlib.pyplot as plt

V=['a','b','c','d','e']

E = [[],[],[],[],[],[],[],[],[],[]]

m=0
for i in range(5):
    for j in range(i+1, len(V)):
        E[m].append(V[i])
        E[m].append(V[j])
        m+=1

p=0.5
for m in range (5):
    EW=[]
    for i in range (10):
        k=random.randint(0,1000)/1000
        if (k<=p):
            EW.append(E[i])

    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(EW)

    nx.draw_shell(G, with_labels = True)

    plt.axis('on')
    plt.savefig(str(m)+".png")
    plt.show()

    