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
        self.E=[]
        self.G=nx.MultiGraph()
        self.MainG=[]
        self.BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.deg={}
        self.MainEdge={}
        

    def add_v(self):

        colorMapEdge=[]
        for i in range(self.G.number_of_edges()):
            colorMapEdge.append('black')
        colorMapEdge.append('black')

        colorMapNode=[]
        for i in range (self.G.number_of_nodes()):
            colorMapNode.append('blue')
        colorMapNode.append('green')

        v0=self.BV[self.G.number_of_nodes()-1]
        self.G.add_node(v0)
        n=self.G.number_of_nodes()
        textNumbNodes.configure(text="kn = "+str(n))
        #print(n)

        for v in self.G.nodes():
            if(v!=v0):
                self.deg[v] = (self.G.degree(v)/(2*n-1))
            #print(self.deg[v])
        self.deg[v0] = 1/(2*n-1)

        

        
        
        V=[]
        ProbV = []
        for v in self.G.nodes():
            V.append(v)
            ProbV.append(self.deg[v])
        #print(ProbV)
        
        for i in range(len(V)):
            for j in range(len(V)-1):
                if (ProbV[j]<ProbV[j+1]):
                    a, b = V[j], ProbV[j]
                    V[j], ProbV[j] = V[j+1], ProbV[j+1]
                    V[j+1], ProbV[j+1] = a, b

        p=random.randint(0, 1000)/1000
        #print(ProbV)
        #print(p)
        pk=0
        for i in range(1, len(V)-1):
            if (p<ProbV[i-1])and(p>ProbV[i+1]):
                pk=i
            else:
                break
        
        #print(pk)
        self.G.add_edge(V[pk], v0)

        edgesG = []
        for ed in self.G.edges():
            edgesG.append(ed)

        self.V.append(v0)

        for i in range (len(edgesG)):
            if v0 in edgesG[i]:
                colorMapEdge[i]='red'

        nx.draw(self.G, node_color=colorMapNode ,edge_color = colorMapEdge,with_labels = True)
        plt.axis('on')
        plt.savefig("st.png")
        plt.clf()
        topImg1 = PhotoImage(file="st.png")
        panel.configure(image=topImg1)
        panel.image = topImg1

    def new_g(self):
        plt.clf()
        self.V=[]
        self.E=[]

        self.E=[]
        #self.G=nx.MultiGraph()
        self.MainG=[]
        self.BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.deg={}
        self.MainEdge={}
        
        self.deg={}
        
        self.G.clear()
        self.G.add_nodes_from(self.V)
        self.G.add_edges_from(self.E)


        nx.draw(self.G, with_labels = True)
        plt.axis('on')
        plt.savefig("st.png")
        plt.clf()
        
        topImg = PhotoImage(file="st.png")
        panel.configure(image=topImg)
        panel.image = topImg

    def break_graph(self):
        k=int(txtk.get())
        numG=self.G.number_of_nodes()//k
        V=[]
        E=[]
        
        for v in self.G.nodes():
            V.append(v)
        for e in self.G.edges():
            E.append(e)
        # for e in E:
        #     self.MainEdge[e] = 0

        print(V[0])
        print(E[0])
        otsech=0
        
        for i in range(numG):
            MainEdges = {}
            V1=[]
            E1=[]
            G1=nx.MultiGraph()
            for j in range (i*k, (i+1)*k):
                V1.append(V[j])
            G1.add_nodes_from(V1)
            for e in E:
                if ((e[0] in V1) and (e[1] in V1)):
                    E1.append(e)
            G1.add_edges_from(E1)

            self.MainG.append(G1)

            nx.draw(G1, with_labels = True)
            plt.axis('on')
            plt.show()
            plt.clf()
        print(len(self.MainG))
        for i in range(len(self.MainG)):
            for j in range(i, len(self.MainG)):
                self.MainEdge[tuple([i, j])] = 0
        for e in E:
            e1 = -1
            e2 = -1
            for i in range (len(self.MainG)):
                if e[0] in self.MainG[i]:
                    e1 = i
            for i in range (len(self.MainG)):
                if e[1] in self.MainG[i]:
                    e2 = i
            t = self.MainEdge[tuple([e1, e2])] + 1
            self.MainEdge[tuple([e1, e2])] = t
        print(self.MainEdge)
        ITOG = nx.MultiGraph()
        VI=[]
        loopstr = ""
        for i in range(len(self.MainG)):
            VI.append(str(i))
            loopstr+= (str(i)+" : "+str(self.MainG[i].number_of_edges())+"\n")
        textLoop.configure(text=loopstr)
        ITOG.add_nodes_from(VI)
        strMult = ""
        for dk in self.MainEdge:
            for i in range (self.MainEdge[dk]):
                ITOG.add_edge(str(dk[0]), str(dk[1]))
            strMult+=("("+str(dk[0])+','+str(dk[1])+') : '+str(self.MainEdge[dk])+'\n')
        textMult.configure(text=strMult)

        nx.draw(ITOG, with_labels = True)
        plt.axis('on')
        plt.savefig("stBRG.png")
        plt.clf()

        topImg = PhotoImage(file="stBRG.png")
        panel.configure(image=topImg)
        panel.image = topImg

        


root = Tk()
root.geometry('1500x2000')

colors={"bgr":'#2F4F4F', 'bfr': '#696969', 'bfr1' : '#808080', 'bent':'#C0C0C0'}
root["bg"] = colors['bgr']

g = GraphBarabasiAlbert()

img = ImageTk.PhotoImage(Image.open("start3.png"))
root.title("Модель случайного графа Боллобаша-Риордана")
panel = Label(root, image = img)
panel.grid(column=0, row=0)

panel = Label(root, image = img)
panel.grid(column=0, row=0)

NumbNodes = LabelFrame(text="колво вершин", width=225, height=80, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
NumbNodes.place(x=420, y=500)

textNumbNodes = Label(NumbNodes, text = "kn = 0", font='Arial 14 bold', background=colors['bfr'],foreground='#ffffff', width=17, height=2)
textNumbNodes.place(x=2, y=2)

EnterZnach = LabelFrame(text="ввод значений", width=400, height=80, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
EnterZnach.place(x=10, y=500)

EnterZnach1 = LabelFrame(EnterZnach, width=350, height=30, background=colors['bfr'])
EnterZnach1.place(x=10, y=10)

lbl = Label(EnterZnach1, text="k:", font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff')
lbl.place(x=0, y=0)
txtk = Entry(EnterZnach1, width=53, background=colors['bent'])
txtk.place(x=20, y=2)

btn1 = Button(root, text="заново", command=g.new_g, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn1.place(x=10, y=600)

btn2 = Button(root, text="добавить", command=g.add_v, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn2.place(x=200, y=600)

btn2 = Button(root, text="разбить", command=g.break_graph, width=10, height=1, font='Arial 20 bold', background='#DC143C', foreground='#FFFFFF')
btn2.place(x=10, y=680)

LoopNum = LabelFrame(text="колво петель/верш.", width=200, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
LoopNum.place(x=680, y=10)

textLoop = Label(LoopNum, text="",font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff', width=23, height=28)
textLoop.place(x=2, y=2)

MultNum = LabelFrame(text="колво кратных р.", width=200, height=480, background=colors['bfr1'],foreground='#ffffff', font='Arial 12 bold')
MultNum.place(x=890, y=10)

textMult = Label(MultNum, text="",font='Arial 10 bold', background=colors['bfr'],foreground='#ffffff', width=23, height=28)
textMult.place(x=2, y=2)

root.mainloop()