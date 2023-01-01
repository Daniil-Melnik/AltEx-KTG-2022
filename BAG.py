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
        self.BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
        v0=self.BV[len(self.V)+1]
        
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
                        strAddEdge+=(self.V[i]+'-'+v0+'\n')
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

        for v in self.V:
            strFactDeg+=(v+' : '+str(self.G.degree(v))+'\n')
        textFactDeg.configure(text=strFactDeg)

        for v in self.V:
            strConnDeg+=(v+' : '+str(self.G.degree(v)-self.LN[v]-self.ME[v])+'\n')
        textConnDeg.configure(text=strConnDeg)

        textAddEdge.configure(text=strAddEdge)

        LoopText = ""
        for v in self.V:
            LoopText+=(v+' : '+str(self.LN[v]//2)+'\n')
        textLoop.configure(text=LoopText)

        nx.draw_circular(self.G,node_color=colorMapNode,edge_color = colorMapEdge ,with_labels = True)
        plt.axis('on')
        plt.savefig("st.png")
        plt.clf()
        topImg1 = PhotoImage(file="st.png")
        panel.configure(image=topImg1)
        panel.image = topImg1
        #print(self.LN)

    def new_g(self):
        us1 = selected1.get()
        plt.clf()
        if (us1 == 1):
            self.V=['a','b']
            self.E=[('a', 'b')]
        
        elif (us1 == 2):
            self.V=['a','b','c']
            self.E=[('a', 'b'),('c', 'b'),('a','c')]

        elif (us1 == 3):
            self.V=['a','b','c','d']
            self.E=[('a', 'b'),('c', 'b'),('d', 'b'),('d', 'c')]
        
        self.G.clear()
        self.G.add_nodes_from(self.V)
        self.G.add_edges_from(self.E)
        strFactDeg=""
        strConnDeg=""
        for v in self.G.nodes():
            self.LN[v]=0
            self.ME[v]=0
        for v in self.V:
            strFactDeg+=(v+' : '+str(self.G.degree(v))+'\n')
        textFactDeg.configure(text=strFactDeg)
        for v in self.V:
            strConnDeg+=(v+' : '+str(self.G.degree(v)-self.LN[v]-self.ME[v])+'\n')
        textConnDeg.configure(text=strConnDeg)
        LoopText = ""
        for v in self.V:
            LoopText+=(v+' : '+str(self.LN[v]//2)+'\n')
        textLoop.configure(text=LoopText)
        nx.draw(self.G, with_labels = True)
        plt.axis('on')
        plt.savefig("st.png")
        plt.clf()
        
        topImg = PhotoImage(file="st.png")
        panel.configure(image=topImg)
        panel.image = topImg

root = Tk()
root.geometry('1500x2000')

colors={"bgr":'#2F4F4F', 'bfr': '#696969', 'bfr1' : '#808080', 'bent':'#C0C0C0'}
root["bg"] = colors['bgr']

g = GraphBarabasiAlbert()

# img = ImageTk.PhotoImage(Image.open("Assets/Images/BAG.png"))
img = None
root.title("Модель случайного графа Барабаши-Альберт")
panel = Label(root, image = img)
panel.grid(column=0, row=0)

panel = Label(root, image = img)
panel.grid(column=0, row=0)

FactDeg = LabelFrame(text="факт. степени вершин", width=200, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
FactDeg.place(x = 660, y=10)

textFactDeg = Label(FactDeg, text="",font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff', width=23, height=28)
textFactDeg.place(x=2, y=2)

ConnDeg = LabelFrame(text="связ. степени вершин", width=200, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
ConnDeg.place(x = 870, y=10)

textConnDeg = Label(ConnDeg, text="",font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff', width=23, height=28)
textConnDeg.place(x=2, y=2)

AddEdge = LabelFrame(text="добавленные рёбра", width=200, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
AddEdge.place(x = 1080, y=10)

textAddEdge = Label(AddEdge, text="",font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff', width=23, height=28)
textAddEdge.place(x=2, y=2)

LoopNum = LabelFrame(text="колво петель/верш.", width=200, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
LoopNum.place(x=1290, y=10)

textLoop = Label(LoopNum, text="",font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff', width=23, height=28)
textLoop.place(x=2, y=2)

seedOpt = LabelFrame(text="затравка", width=400, height=170, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
seedOpt.place(x=840, y=500)

seedOpt1 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])
seedOpt2 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])
seedOpt3 = LabelFrame(seedOpt, width=350, height=30, background=colors['bfr'])

seedOpt1.place(x=10, y=10)
seedOpt2.place(x=10, y=40)
seedOpt3.place(x=10, y=70)

selected1 = IntVar()

seedRad1 = Radiobutton(seedOpt1,text='степени 1-1', value=1, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
seedRad2 = Radiobutton(seedOpt2,text='степени 2-2-2', value=2, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')
seedRad3 = Radiobutton(seedOpt3,text='степени 1-2-2-3', value=3, variable=selected1, background=colors['bfr'],foreground='#ffffff', font='Arial 10 bold')

seedRad1.place(x=5, y=0)
seedRad2.place(x=5, y=0)
seedRad3.place(x=5, y=0)

EnterZnach = LabelFrame(text="ввод значений", width=400, height=80, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
EnterZnach.place(x=10, y=500)

EnterZnach1 = LabelFrame(EnterZnach, width=350, height=30, background=colors['bfr'])
EnterZnach1.place(x=10, y=10)

TypeGraph = LabelFrame(text="способы работы", width=400, height=170, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
TypeGraph.place(x=420, y=500)

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

btn1 = Button(root, text="заново", command=g.new_g, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn1.place(x=10, y=600)

btn2 = Button(root, text="добавить", command=g.add_v, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn2.place(x=200, y=600)

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

root.mainloop()