import random
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image
import shutil
from tkinter.ttk import Checkbutton
import math

class GraphBarabasiAlbert:
    

    def __init__(self):
        self.V=[]
        self.E=[]
        self.G=nx.MultiGraph()
        self.ME={}
        self.LN={}
        self.deg={}
        

    def add_v(self):
        
        for v in self.V:
            self.deg[v]= self.G.degree(v) - self.LN[v] - self.ME[v]
        #print(self.deg)
        us = selected.get()
        #print(us)
        sumDeg=0 
        edgesCount=int(txtn.get())
        #print(self.V)
        
        for v in self.G.nodes():
            sumDeg+=self.deg[v]

        sumDeg=sumDeg//2
        ProbV = []
        #v0=self.BV[len(self.V)+1]
        v0 = str(self.G.number_of_nodes())
        print(self.G.nodes())
        
        colorMapNode=[]
        for v in self.V:
            colorMapNode.append('blue')
        self.G.add_node(v0)
        self.LN[v0]=0
        self.ME[v0]=0
        colorMapNode.append('green')

        strAddEdge = ""
        
        if ((us == 2)or(us == 4)):
            loop=random.randint(0, edgesCount-1)
            for i in range(loop):
                self.G.add_edge(v0, v0)
                strAddEdge+=(v0+'-'+v0+'\n')
                nn=self.LN[v0]+2
                self.LN[v0] = nn
            edgesCount-=loop
        #print(self.LN)

        #print(self.V)

             
        for v in self.V:
             ProbV.append(self.deg[v]/(sumDeg*2))
           
        for i in range(len(self.V)):
            for j in range(len(self.V)-1):
                if (ProbV[j]<ProbV[j+1]):
                    a, b = self.V[j], ProbV[j]
                    self.V[j], ProbV[j] = self.V[j+1], ProbV[j+1]
                    self.V[j+1], ProbV[j+1] = a, b
        
        
        
        if ((us==3)or(us==4)):
            L=edgesCount
            for i in range(edgesCount):
                if (L>0):
                    mult = random.randint(0, L-1)
                    for j in range(mult):
                        self.G.add_edge(self.V[i], v0)
                        nn1 = self.ME[self.V[i]]+1
                        self.ME[self.V[i]] = nn1
                        nn1 = self.ME[v0]+1
                        self.ME[v0] = nn1
                    L-=mult
            #print(self.ME)
        
        if ((us==1)or(us==2)):
            for i in range(edgesCount):
                self.G.add_edge(self.V[i], v0)
                strAddEdge+=(self.V[i]+'-'+v0+'\n')
        # if(us==1)and(('f','f') in (self.G.edges())):
        #     self.G.remove_edge('f','f')
        
        
        colorMapEdge=[]
        for i in range(self.G.number_of_edges()):
            colorMapEdge.append('black')

        #print(self.G.edges())
        edgesG = []
        for ed in self.G.edges():
            edgesG.append(ed)
        #print(self.G.edges())
        #print(colorMapEdge)
        for i in range (len(edgesG)):
            if v0 in edgesG[i]:
                colorMapEdge[i]='red'
        self.V.append(v0)
        strFactDeg=""
        strConnDeg=""


        LoopText = ""

        nx.draw_circular(self.G,node_color=colorMapNode,edge_color = colorMapEdge ,with_labels = True)
        plt.axis('on')
        plt.savefig("st.png", dpi = 164)
        plt.clf()
        topImg1 = PhotoImage(file="st.png")
        panel1.configure(image=topImg1)
        panel1.image = topImg1

        #print(self.LN)

    def new_g(self):
        us1 = selected1.get()
        plt.clf()
        self.V=[]
        self.E=[]
        if (us1 == 1):
            nodes=nx.read_adjlist("nodes1.txt")
            edges=nx.read_edgelist('edges1.txt')
        
        elif (us1 == 2):
            nodes=nx.read_adjlist("nodes2.txt")
            edges=nx.read_edgelist('edges2.txt')

        elif (us1 == 3):
            nodes=nx.read_adjlist("nodes3.txt")
            edges=nx.read_edgelist('edges3.txt')
        
        elif (us1 == 4):
            nodes=nx.read_adjlist("nodes4.txt")
            edges=nx.read_edgelist('edges4.txt')
        
        self.G.clear()
        self.G.add_nodes_from(nodes)
        self.G.add_edges_from(edges.edges())
        for v in self.G.nodes():
            self.V.append(v)
        print(self.G.edges())
        for e in self.G.edges():
            self.E.append(e)
        strFactDeg=""
        strConnDeg=""
        for v in self.G.nodes():
            self.LN[v]=0
            self.ME[v]=0
        nx.draw(self.G, with_labels = True)
        plt.axis('on')
        plt.savefig("st.png", dpi = 164)
        plt.clf()
        topImg = PhotoImage(file="st.png")
        panel1.configure(image=topImg)
        panel1.image = topImg

root1 = Tk()
root1.geometry('1500x2000')

colors={"bgr":'#2F4F4F', 'bfr': '#696969', 'bfr1' : '#808080', 'bent':'#C0C0C0'}
root1["bg"] = colors['bgr']

g = GraphBarabasiAlbert()

img = ImageTk.PhotoImage(Image.open("start2big.png"))
root1.title("Модель случайного графа Барабаши-Альберт")

panel1 = Label(root1, image = img)
panel1.grid(column=0, row=0)

panel1 = Label(root1, image = img)
panel1.grid(column=0, row=0)

seedOpt = LabelFrame(text="затравка", width=400, height=170, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
seedOpt.place(x=1095, y=280)

seedOpt1 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])
seedOpt2 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])
seedOpt3 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])
seedOpt4 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])

seedOpt1.place(x=10, y=10)
seedOpt2.place(x=10, y=40)
seedOpt3.place(x=10, y=70)
seedOpt4.place(x=10, y=100)

selected1 = IntVar()

seedRad1 = Radiobutton(seedOpt1,text='10 вершин', value=1, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
seedRad2 = Radiobutton(seedOpt2,text='15 вершин', value=2, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
seedRad3 = Radiobutton(seedOpt3,text='20 вершин', value=3, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
seedRad4 = Radiobutton(seedOpt4,text='100 вершин', value=4, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')

seedRad1.place(x=5, y=0)
seedRad2.place(x=5, y=0)
seedRad3.place(x=5, y=0)
seedRad4.place(x=5, y=0)

EnterZnach = LabelFrame(text="ввод значений", width=400, height=80, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
EnterZnach.place(x=1095, y=5)

EnterZnach1 = LabelFrame(EnterZnach, width=350, height=30, background=colors['bfr'])
EnterZnach1.place(x=10, y=10)

TypeGraph = LabelFrame(text="способы работы", width=400, height=170, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
TypeGraph.place(x=1095, y=97)

TypeGraph1 = LabelFrame(TypeGraph, width=350, height=30, background=colors['bfr'])
TypeGraph2 = LabelFrame(TypeGraph, width=350, height=30, background=colors['bfr'])
TypeGraph3 = LabelFrame(TypeGraph, width=350, height=30, background=colors['bfr'])
TypeGraph4 = LabelFrame(TypeGraph, width=350, height=30, background=colors['bfr'])

TypeGraph1.place(x=10, y=10)
TypeGraph2.place(x=10, y=40)
TypeGraph3.place(x=10, y=70)
TypeGraph4.place(x=10, y=100)

#Количество вершин
lbl = Label(EnterZnach1, text="колво рёбер:", font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff')
lbl.place(x=0, y=0)
txtn = Entry(EnterZnach1, width=40, background=colors['bent'])
txtn.place(x=100, y=2)

selected = IntVar()

btn1 = Button(root1, text="заново", command=g.new_g, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn1.place(x=1095, y=462)

btn2 = Button(root1, text="добавить", command=g.add_v, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn2.place(x=1318, y=462)

rad1 = Radiobutton(TypeGraph1,text='граф', value=1, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad1.place(x=5, y=0)

#Связность графа
rad2 = Radiobutton(TypeGraph2,text='псевдограф', value=2, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad2.place(x=5, y=0) 

#Планарность графа
rad3 = Radiobutton(TypeGraph3,text='мультиграф', value=3, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad3.place(x=5, y=0)

#Присутствие треугольников
rad4 = Radiobutton(TypeGraph4,text='псевдомультиграф', value=4, variable=selected, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
rad4.place(x=5, y=0)

root1.mainloop()