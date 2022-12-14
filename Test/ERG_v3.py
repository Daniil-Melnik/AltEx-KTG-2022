import random
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
import shutil
from tkinter.ttk import Checkbutton
import math




def ERG():
    BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    E=[]
    n=int(txtn.get())
    # if (chk.get==0):
    #     us = False
    # else:
    #     us = True  
    us = chk.state()
    if (len(us)!=0):
        if (us[0] == 'selected'):
            k=1
        else:
            k=0
    else:
        k=0
    # print(k)
    if (k==0):
        #txtp.delete(first=0,last=END)
        p=float(txtp.get())
        txtс.delete(0, END)
        txtс.insert(0,'c')
        print (p)
    else:
        c=float(txtс.get())
        p=c*(math.log(n)/n)
        txtp.delete(first=0,last=END)
        txtp.insert(0, str(p))
        print(p) 
    #p=float(txtp.get())
    #p=0.5 
    V=[]
    for i in range(n*(n-1)//2):
        E.append([])

    for i in range (n):
        V.append(BV[i])
    m=0

    for i in range(n):
        for j in range(i+1, len(V)):
            E[m].append(V[i])
            E[m].append(V[j])
            m+=1

    # if (us):
    #     p=3*n/math.log(n)
    #     txtp.insert(0,str(p))
    # else:
    #     p=float(txtp.get())
    
    G = nx.Graph()
    G.add_nodes_from(V)
    for i in range (n*(n-1)//2):
        k=random.randint(0,1000)/1000
        if (k<=p):
            G.add_edge(E[i][0],E[i][1])
    # if (nx.check_planarity(G, counterexample=False)[0]==True):
    #     pl=1
    # else:
    #     pl=0

    # print(nx.check_planarity(G, counterexample=False))

    if (nx.check_planarity(G, counterexample=False)[0]==True):
        nx.draw_planar(G, with_labels = True)
    else:
        nx.draw_circular(G, with_labels = True)
    plt.axis('on')
    plt.savefig("st.png")
    plt.clf()

    topImg = PhotoImage(file="st.png")
    panel.configure(image=topImg)
    panel.image = topImg

root = Tk()

#Поле для n
txtn = Entry(root)
txtn.grid(column=2, row=0)
lbl = Label(root, text="Кол-во вершин")
lbl.grid(column=1, row=0)

#Поле для p
txtp = Entry(root)
txtp.grid(column=2, row=1)
lblp = Label(root, text="Вероятность")
lblp.grid(column=1, row=1)

#Поле для p
txtс = Entry(root)
txtс.grid(column=1, row=3)
lblс = Label(root, text="с = ")
lblс.grid(column=0, row=3)

#Формула вероятности при связности
chk_state = BooleanVar()  
chk_state.set(1)  # задайте проверку состояния чекбокса  
chk = Checkbutton(root, text='связность(теорема 13)', var=chk_state)  
chk.grid(column=0, row=2)


img = ImageTk.PhotoImage(Image.open("start.png"))

panel = Label(root, image = img)
panel.grid(column=0, row=0)

btn = Button(root, text="touch", command=ERG)
btn.grid(column=0, row=1)

root.mainloop()