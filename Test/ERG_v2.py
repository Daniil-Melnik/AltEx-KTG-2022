import random
import networkx as nx
import matplotlib.pyplot as plt

BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

E=[]
n=5
V=[]

for i in range(n*(n-1)//2):
    E.append([])

for i in range (n):
    V.append(BV[i])

print (V)
m=0

for i in range(n):
    for j in range(i+1, len(V)):
        E[m].append(V[i])
        E[m].append(V[j])
        m+=1

p=0.5

for m in range (5):
    G = nx.Graph()
    G.add_nodes_from(V)
    for i in range (n*(n-1)//2):
        k=random.randint(0,1000)/1000
        if (k<=p):
            G.add_edge(E[i][0],E[i][1])

    nx.draw_circular(G, with_labels = True)

    plt.axis('on')
    plt.savefig(str(m)+".png")
    #plt.show()