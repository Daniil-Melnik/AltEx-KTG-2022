import os
import math
import random
import customtkinter
import networkx as nx
import matplotlib.pyplot as plt

from tkinter import *
from types import CellType
from PIL import Image, ImageTk
from tkinter.ttk import Checkbutton




#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#  BAG
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
       
class BAG:
    def __init__(self):
        self.Vertex=[]
        self.Graph=nx.MultiGraph()
        self.BaseVertex=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.Vertex=[]
        self.Edges=[]
        self.Graph=nx.MultiGraph()
        self.ME={}
        self.LN={}
        self.deg={}
        
    def addVertex(self):
        for vertex in self.Vertex:
            self.deg[vertex]= self.Graph.degree(vertex) - self.LN[vertex] - self.ME[vertex]
        #print(deg)
        selected = app.BAGselected.get()
        #print(us)
        sumDeg=0
        edgesCount=int(app.BAGsliderEdges.get())
        #print(V)
        for vertex in self.Graph.nodes():
            sumDeg+=self.deg[vertex]
        sumDeg=sumDeg//2
        ProbVertex = []
        v0=self.BaseVertex[len(self.Vertex)+1]
        colorMapNode=[]
        for vertex in self.Vertex:
            colorMapNode.append('blue')
        self.Graph.add_node(v0)
        self.LN[v0]=0
        self.ME[v0]=0
        colorMapNode.append('green')
        strAddEdge = ""
        if ((selected == 1)or(selected == 3)):
            loop=random.randint(0, edgesCount-1)
            for i in range(loop):
                self.Graph.add_edge(v0, v0)
                strAddEdge+=(v0+'-'+v0+'\n')
                nn=self.LN[v0]+2
                self.LN[v0] = nn
            edgesCount-=loop
        for vertex in self.Vertex:
                ProbVertex.append(self.deg[vertex]/(sumDeg*2))
        for i in range(len(self.Vertex)):
            for j in range(len(self.Vertex)-1):
                if (ProbVertex[j]<ProbVertex[j+1]):
                    a, b = self.Vertex[j], ProbVertex[j]
                    self.Vertex[j], ProbVertex[j] = self.Vertex[j+1], ProbVertex[j+1]
                    self.Vertex[j+1], ProbVertex[j+1] = a, b
        if ((selected==2)or(selected==3)):
            L=edgesCount
            for i in range(edgesCount):
                if (L>0):
                    mult = random.randint(0, L-1)
                    for j in range(mult):
                        self.Graph.add_edge(self.Vertex[i], v0)
                        strAddEdge+=(self.Vertex[i]+'-'+v0+'\n')
                        nn1 = self.ME[self.Vertex[i]]+1
                        self.ME[self.Vertex[i]] = nn1
                        nn1 = self.ME[v0]+1
                        self.ME[v0] = nn1
                    L-=mult
        if ((selected==0)or(selected==1)):
            for i in range(edgesCount):
                self.Graph.add_edge(self.Vertex[i], v0)
                strAddEdge+=(self.Vertex[i]+'-'+v0+'\n')
        colorMapEdge=[]
        for i in range(self.Graph.number_of_edges()):
            colorMapEdge.append('black')
        edgesG = []
        for ed in self.Graph.edges():
            edgesG.append(ed)
        for i in range (len(edgesG)):
            if v0 in edgesG[i]:
                colorMapEdge[i]='red'
        self.Vertex.append(v0)
        strFactDeg=""
        strConnDeg=""
        for vertex in self.Vertex:
            strFactDeg+=(vertex+' : '+str(self.Graph.degree(vertex))+'\n')
        app.BAGgraphDeg.configure(text=strFactDeg)
        for vertex in self.Vertex:
            strConnDeg+=(vertex+' : '+str(self.Graph.degree(vertex)-self.LN[vertex]-self.ME[vertex])+'\n')
        app.BAGgraphConnDeg.configure(text=strConnDeg)
        app.BAGgraphAddedEdges.configure(text=strAddEdge)
        LoopText = ""
        for vertex in self.Vertex:
            LoopText+=(vertex+' : '+str(self.LN[vertex]//2)+'\n')
        app.BAGgraphLoopCount.configure(text=LoopText)
        nx.draw_circular(self.Graph,node_color=colorMapNode,edge_color = colorMapEdge ,with_labels = True)
        plt.savefig("BAG.png", dpi=110) # 704x528
        plt.clf()
        topImg = customtkinter.CTkImage(light_image=Image.open(os.path.join("BAG.png")), dark_image=Image.open(os.path.join("BAG.png")),size=(app.S_GRAPH_WIDTH,app.S_GRAPH_HEIGHT))
        app.BAGgraphImage.configure(image=topImg)

    def newGraph(self):        
        selectedSeed = app.BAGselectedSeed.get()
        plt.clf()
        if (selectedSeed == 0):
            self.Vertex=['a','b']
            self.Edges=[('a', 'b')]
        elif (selectedSeed == 1):
            self.Vertex=['a','b','c']
            self.Edges=[('a', 'b'),('c', 'b'),('a','c')]
        elif (selectedSeed == 2):
            self.Vertex=['a','b','c','d']
            self.Edges=[('a', 'b'),('c', 'b'),('d', 'b'),('d', 'c')]
        self.Graph.clear()
        self.Graph.add_nodes_from(self.Vertex)
        self.Graph.add_edges_from(self.Edges)
        strFactDeg=""
        strConnDeg=""
        for v in self.Graph.nodes():
            self.LN[v]=0
            self.ME[v]=0
        for v in self.Vertex:
            strFactDeg+=(v+' : '+str(self.Graph.degree(v))+'\n')
        app.BAGgraphDeg.configure(text=strFactDeg)
        for v in self.Vertex:
            strConnDeg+=(v+' : '+str(self.Graph.degree(v)-self.LN[v]-self.ME[v])+'\n')
        app.BAGgraphConnDeg.configure(text=strConnDeg)
        LoopText = ""
        for v in self.Vertex:
            LoopText+=(v+' : '+str(self.LN[v]//2)+'\n')
        app.BAGgraphLoopCount.configure(text=LoopText)
        nx.draw(self.Graph, with_labels = True)
        plt.savefig("BAG.png", dpi=110) # 704x528
        plt.clf()
        topImg = customtkinter.CTkImage(light_image=Image.open(os.path.join("BAG.png")), dark_image=Image.open(os.path.join("BAG.png")),size=(app.S_GRAPH_WIDTH,app.S_GRAPH_HEIGHT))
        app.BAGgraphImage.configure(image=topImg)



#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#  ERG Algorithm
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
def ERG():
    # sourcery skip: extract-duplicate-method, for-append-to-extend, for-index-underscore, list-comprehension, move-assign-in-block, simplify-len-comparison, use-named-expression
    #######################
    #                     #
    #    Инициализация    #
    #                     #
    #######################
    Edges = []
    BaseVertex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    valMap = {}
    vertexCount=int(app.ERGsliderVertex.get())
    selectedRadioButton=app.ERGselected.get()
    ############################
    #    Вероятностный граф    #
    ############################
    if (selectedRadioButton==0):
        propability=float(app.ERGsliderPropability.get())
    ################################
    #    Связность (теорема 13)    #
    ################################
    elif (selectedRadioButton==1):
        constantC=float(app.ERGsliderCConstant.get())
        propability=constantC*(math.log(vertexCount)/vertexCount)
        app.ERGsliderPropability.set(propability)
        app.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(propability))}")
    ##################################
    #    Планарность (теорема 26)    #
    ##################################
    elif (selectedRadioButton==2):
        constantC=float(app.ERGsliderCConstant.get())
        propability=constantC/vertexCount
        app.ERGsliderPropability.set(propability)
        app.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(propability))}")
    ################################################
    #    Присутствие треугольников (теорема 12)    #
    ################################################
    elif (selectedRadioButton==3):
        w=vertexCount/math.log(vertexCount)
        propability=w/vertexCount
        app.ERGsliderPropability.set(propability)
        app.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(propability))}")
     ###############################################
     #    Отсутствие треугольников (теорема 10)    #
     ###############################################
    elif (selectedRadioButton==4):
        a=1/vertexCount
        propability=a/vertexCount
        app.ERGsliderPropability.set(propability) 
        app.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(propability))}")
    ##############################################
    #    Феодальная раздробленность (стр. 48)    #
    ##############################################
    elif (selectedRadioButton==5):
        propability=1/(vertexCount**3)
        app.ERGsliderPropability.set(propability) 
        app.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(propability))}")
    ###########################
    #    Империя (стр. 48)    #
    ###########################
    elif (selectedRadioButton==6):
        propability=vertexCount*math.log(vertexCount)/vertexCount
        app.ERGsliderPropability.set(propability) 
        app.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(propability))}")
    #########################################
    #    Гигантская компонента связности    #
    #########################################
    elif (selectedRadioButton==7):
        propability=float(app.ERGsliderPropability.get())
    ##############################################
    #                                            #
    #    постинициализация и вывод результата    #
    #                                            #
    ##############################################
    Vertex=[]
    for i in range(vertexCount*(vertexCount-1)//2):
        Edges.append([])
    for i in range(vertexCount):
        Vertex.append(BaseVertex[i])
        valMap[BaseVertex[i]]=1.0
    m=0
    for i in range(vertexCount):
        for j in range(i+1, len(Vertex)):
            Edges[m].append(Vertex[i])
            Edges[m].append(Vertex[j])
            m+=1
    Graph = nx.Graph()
    Graph.add_nodes_from(Vertex)
    for i in range (vertexCount*(vertexCount-1)//2):
        randValue=random.randint(0,100)/100
        if (randValue<=propability):
            Graph.add_edge(Edges[i][0],Edges[i][1])
    if (selectedRadioButton==4):
        all_cliques = nx.enumerate_all_cliques(Graph)
        triad_cliques=[x for x in all_cliques if len(x)==3 ]
        if (len(triad_cliques)!=0):
            for v in triad_cliques[0]:
                valMap[v]=0.1
    all_cliques= nx.enumerate_all_cliques(Graph)
    ###########################################
    #    проверка на налицие треугольников    #
    ###########################################
    if triad_cliques := [x for x in all_cliques if len(x) == 3]:
        app.ERGlabelTrianglesPresence.configure(fg_color=App.Colors.graphInfoTrue)
    else:
        app.ERGlabelTrianglesPresence.configure(fg_color=App.Colors.graphInfoFalse)
    if (selectedRadioButton==8):
        for v in (max(nx.connected_components(Graph))):
            valMap[v]=0.1
    values = [valMap.get(node, 0.25) for node in Graph.nodes()]
    plt.clf()
    #################################
    #    проверка на планарность    #
    #################################
    if (nx.check_planarity(Graph, counterexample=False)[0]==True):
        nx.draw_planar(Graph, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        app.ERGlabelPlanarity.configure(fg_color=App.Colors.graphInfoTrue)
    else:
        nx.draw_circular(Graph, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        app.ERGlabelPlanarity.configure(fg_color=App.Colors.graphInfoFalse)
    ###############################
    #    проверка на связность    #
    ###############################
    if (nx.is_connected(Graph)):
        app.ERGlabelConnectivity.configure(fg_color=App.Colors.graphInfoTrue)
    else:
        app.ERGlabelConnectivity.configure(fg_color=App.Colors.graphInfoFalse)
    # print(max(nx.connected_components(Graph)))
    plt.savefig("ERG.png", dpi=150) # 960x720
    topImg = customtkinter.CTkImage(light_image=Image.open(os.path.join("ERG.png")), dark_image=Image.open(os.path.join("ERG.png")),size=(app.GRAPH_WIDTH,app.GRAPH_HEIGHT))
    app.ERGgraphImage.configure(image=topImg)




#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
#  Setting initial main window parameters
#################################################################################################################################################################################
#################################################################################################################################################################################
#################################################################################################################################################################################
class App(customtkinter.CTk):
    ######################################################################
    #    Setting the parameters and the class for working with colors    #
    ######################################################################
    WIDTH = 1760
    HEIGHT = 830
    GRAPH_WIDTH = 960   # if dpi is set to 150
    GRAPH_HEIGHT = 720  # if dpi is set to 150
    S_GRAPH_WIDTH = 704   # if dpi is set to 110
    S_GRAPH_HEIGHT = 528  # if dpi is set to 110
    CORNER_RADIUS = 10
    # color class
    class Colors:
        graphInfoTrue = "#84a98c"
        graphInfoFalse = "#9b2226"
        graphBackground = "#9b2226"
        sliderEnabled = "#2a9d8f"
        sliderWarning = "#ff9e00"
        sliderDisabled = "#780000"

    def __init__(self): 
        super().__init__()

        self.resizable(False, False)
        self.title("Модели случайных графов")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        #############################
        #    set grid layout 1x2    #
        #############################х
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ####################################################
        #    load images with light and dark mode image    #
        ####################################################
        self.imageLogo = customtkinter.CTkImage(Image.open("Assets/Icons/leti.png"), size=(32, 32))

        #################################
        #    create navigation frame    #
        #################################
        self.Menu = customtkinter.CTkFrame(self, corner_radius=0)
        self.MenuLabel = customtkinter.CTkLabel(self.Menu, text="  Случайные графы", image=self.imageLogo, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.MenuButtonERG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Эрдёша-Реньи", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonERG_event)
        self.MenuButtonBAG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Барабаши-Альберт", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonBAG_event)
        self.MenuButtonBRG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Баллобаша-Риордана", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonBRG_event)
        self.switcherTheme = customtkinter.CTkSwitch(master=self.Menu, text="Темная тема ", command=self.changeThemeMode) # Dark theme switcher
        #plotting elements
        self.Menu.grid(row=0, column=0, sticky="nsew")
        self.Menu.grid_rowconfigure(4, weight=1)
        self.MenuLabel.grid(row=0, column=0, padx=20, pady=20)
        self.MenuButtonERG.grid(row=1, column=0, sticky="nswe")
        self.MenuButtonBAG.grid(row=2, column=0, sticky="nswe")
        self.MenuButtonBRG.grid(row=3, column=0, sticky="nswe")
        self.switcherTheme.grid(row=9, column=0, padx=10, pady=10, sticky="nswe")

        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create ERG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        
        self.FrameERG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FrameERG.rowconfigure(14, weight=10)
        self.FrameERG.columnconfigure(0, weight=1)
        # Frame window - left one
        self.ERGgraphFrame = customtkinter.CTkFrame(master=self.FrameERG, width=self.GRAPH_WIDTH+20, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.ERGgraphVisualizeFrame = customtkinter.CTkFrame(master=self.ERGgraphFrame, width=self.GRAPH_WIDTH, height=self.GRAPH_HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.ERGgraphInfoFrame = customtkinter.CTkFrame(master=self.ERGgraphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.ERGgraphFrame.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.ERGgraphVisualizeFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGgraphInfoFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        # Parameters window - right one
        self.ERGparametersFrame = customtkinter.CTkFrame(master=self.FrameERG, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.ERGoptionsFrame = customtkinter.CTkFrame(master=self.ERGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.ERGinputFrame = customtkinter.CTkFrame(master=self.ERGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.ERGbuttonsFrame = customtkinter.CTkFrame(master=self.ERGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.ERGparametersFrame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.ERGoptionsFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGinputFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGbuttonsFrame.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        
        ##########################################
        #    creating elements for graphFrame    #
        ##########################################
        graph = customtkinter.CTkImage(light_image=Image.open(os.path.join("Assets/Images/ERG.png")), dark_image=Image.open(os.path.join("Assets/Images/ERG.png")), size=(self.GRAPH_WIDTH,self.GRAPH_HEIGHT))
        self.ERGgraphImage = customtkinter.CTkLabel(master=self.ERGgraphVisualizeFrame,width=self.GRAPH_HEIGHT-10,height=self.GRAPH_HEIGHT-10,text="",image=graph)
        self.ERGlabelConnectivity = customtkinter.CTkLabel(master=self.ERGgraphInfoFrame,width=(self.GRAPH_WIDTH/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Связность")
        self.ERGlabelPlanarity = customtkinter.CTkLabel(master=self.ERGgraphInfoFrame,width=(self.GRAPH_WIDTH/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Планарность")
        self.ERGlabelTrianglesPresence= customtkinter.CTkLabel(master=self.ERGgraphInfoFrame,width=(self.GRAPH_WIDTH/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Наличие треугольников")
        self.ERGgraphImage.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.ERGlabelConnectivity.grid(row=0, column=0, sticky="nswe", padx=5, pady=0)
        self.ERGlabelPlanarity.grid(row=0, column=1, sticky="nswe", padx=5, pady=0)
        self.ERGlabelTrianglesPresence.grid(row=0, column=2, sticky="nswe", padx=5, pady=0)
        
        ############################################
        #    creating elements for optionsFrame    #
        ############################################
        self.ERGlabedRad = customtkinter.CTkLabel(master=self.ERGoptionsFrame,anchor=customtkinter.W,text='Способы задания графа:')
        self.ERGselected = IntVar(value=0)
        #radiobuttons
        self.ERGradProbability = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Вероятностный граф', 
            value=0, variable=self.ERGselected, command = lambda v=0: self.updateSliders(v))
        self.ERGradConnectivity = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Связность (теорема 13)', 
            value=1, variable=self.ERGselected, command = lambda v=1: self.updateSliders(v))
        self.ERGradPlanarity = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Планарность (теорема 26)', 
            value=2, variable=self.ERGselected, command = lambda v=2: self.updateSliders(v))
        self.ERGradNonTriangle = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Присутствие треугольников (теорема 12)', 
            value=3, variable=self.ERGselected, command = lambda v=3: self.updateSliders(v))
        self.ERGradTriangle = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Отсутствие треугольников (теорема 10)', 
            value=4, variable=self.ERGselected, command = lambda v=4: self.updateSliders(v))
        self.ERGradFeudalFrag = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Феодальная раздробленность (стр. 48)', 
            value=5, variable=self.ERGselected, command = lambda v=5: self.updateSliders(v))
        self.ERGradEmpire = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Империя (стр. 48)', 
            value=6, variable=self.ERGselected, command = lambda v=6: self.updateSliders(v))
        self.ERGradGiantConnComp = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Гигантская компонента связности', 
            value=7, variable=self.ERGselected, command = lambda v=7: self.updateSliders(v))
        #plotting elements
        self.ERGlabedRad.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradProbability.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradConnectivity.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradPlanarity.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradNonTriangle.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradTriangle.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradFeudalFrag.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradEmpire.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGradGiantConnComp.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)

        ##########################################
        #    creating elements for inputFrame    #
        ##########################################
        self.vertexCount = 8
        self.propability = 0.5
        self.constantC = 1
        self.ERGlabelVertex = customtkinter.CTkLabel(master=self.ERGinputFrame,height=20,anchor=customtkinter.W,text=f"Количество вершин в графе: {self.vertexCount}")
        self.ERGlabelPropability = customtkinter.CTkLabel(master=self.ERGinputFrame,height=20,anchor=customtkinter.W,text=f"Вероятность появления ребер в графе: {self.propability}")
        self.ERGlabelCConst = customtkinter.CTkLabel(master=self.ERGinputFrame,height=20,anchor=customtkinter.W,text=f"Константа C: {self.constantC}")
        self.ERGsliderVertex = customtkinter.CTkSlider(master=self.ERGinputFrame,height=25,width=480,from_=1, to=26, number_of_steps=25)
        self.ERGsliderPropability = customtkinter.CTkSlider(master=self.ERGinputFrame,height=25,width=480,from_=0, to=1, number_of_steps=100)
        self.ERGsliderCConstant = customtkinter.CTkSlider(master=self.ERGinputFrame,height=25,width=480,from_=0, to=10, number_of_steps=1000)
        self.ERGsliderVertex.set(self.vertexCount)
        self.ERGsliderPropability.set(self.propability)
        self.ERGsliderCConstant.set(self.constantC)
        self.ERGsliderVertex.configure(command = lambda v=self.vertexCount: self.updateCountSliderLabel(v))
        self.ERGsliderPropability.configure(command = lambda v=self.propability: self.updatePropSliderLabel(v))
        self.ERGsliderCConstant.configure(command = lambda v=self.constantC: self.updateConstSliderLabel(v))
        #plotting elements
        self.ERGlabelVertex.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGlabelPropability.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGlabelCConst.grid(row=4, column=0, sticky="nswe",padx=10, pady=10)
        self.ERGsliderVertex.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGsliderPropability.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGsliderCConstant.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        
        ############################################
        #    creating elements for buttonsFrame    #
        ############################################
        self.ERGbtnCreate = customtkinter.CTkButton(master=self.ERGbuttonsFrame,text="Построить граф",height=35,width=480,command=ERG)
        self.ERGbtnCreate.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create BAG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################

        self.FrameBAG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FrameBAG.rowconfigure(14, weight=10)
        self.FrameBAG.columnconfigure(14, weight=10)
        # graph window
        graph = customtkinter.CTkImage(light_image=Image.open(os.path.join("Assets/Images/BAG.png")), dark_image=Image.open(os.path.join("Assets/Images/BAG.png")), size=(self.S_GRAPH_WIDTH,self.S_GRAPH_HEIGHT))
        self.BAGgraph = customtkinter.CTkFrame(master=self.FrameBAG, width=self.S_GRAPH_WIDTH+20, height=self.S_GRAPH_HEIGHT+20, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphVisualizer = customtkinter.CTkFrame(master=self.BAGgraph, width=self.S_GRAPH_WIDTH, height=self.S_GRAPH_HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphImage = customtkinter.CTkLabel(master=self.BAGgraphVisualizer,text="",image=graph)
        self.BAGgraphInfo = customtkinter.CTkFrame(master=self.BAGgraph, width=720, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphInfoDegLabel = customtkinter.CTkLabel(master=self.BAGgraphInfo,anchor=customtkinter.CENTER,text='Факт. степени вершин:',height=20)
        self.BAGgraphInfoConnDegLabel = customtkinter.CTkLabel(master=self.BAGgraphInfo,anchor=customtkinter.CENTER,text='Связ. степени вершин:',height=20)
        self.BAGgraphInfoAddedEdgesLabel = customtkinter.CTkLabel(master=self.BAGgraphInfo,anchor=customtkinter.CENTER,text='Добавленные ребра:',height=20)
        self.BAGgraphInfoLoopCountLabel = customtkinter.CTkLabel(master=self.BAGgraphInfo,anchor=customtkinter.CENTER,text='Количество петель:',height=20)
        self.BAGgraphInfoDeg = customtkinter.CTkFrame(master=self.BAGgraphInfo, width=185, height=self.S_GRAPH_HEIGHT-50, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphInfoConnDeg = customtkinter.CTkFrame(master=self.BAGgraphInfo, width=185, height=self.S_GRAPH_HEIGHT-50, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphInfoAddedEdges = customtkinter.CTkFrame(master=self.BAGgraphInfo, width=185, height=self.S_GRAPH_HEIGHT-50, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphInfoLoopCount = customtkinter.CTkFrame(master=self.BAGgraphInfo, width=185, height=self.S_GRAPH_HEIGHT-50, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphDeg = customtkinter.CTkLabel(master=self.BAGgraphInfoDeg,width=175,height=self.S_GRAPH_HEIGHT-70,anchor=customtkinter.CENTER,text='')
        self.BAGgraphConnDeg = customtkinter.CTkLabel(master=self.BAGgraphInfoConnDeg,width=175,height=self.S_GRAPH_HEIGHT-70,anchor=customtkinter.CENTER,text='')
        self.BAGgraphAddedEdges = customtkinter.CTkLabel(master=self.BAGgraphInfoAddedEdges,width=175,height=self.S_GRAPH_HEIGHT-70,anchor=customtkinter.CENTER,text='')
        self.BAGgraphLoopCount = customtkinter.CTkLabel(master=self.BAGgraphInfoLoopCount,width=175,height=self.S_GRAPH_HEIGHT-70,anchor=customtkinter.CENTER,text='')
        self.BAGgraph.grid(row=0, column=0, sticky="nswe", padx=(10,10), pady=(10,0))
        self.BAGgraphVisualizer.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphImage.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.BAGgraphInfo.grid(row=0, column=1, sticky="nswe", padx=(8,10), pady=(10,10))
        self.BAGgraphInfoDegLabel.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,0))
        self.BAGgraphInfoConnDegLabel.grid(row=0, column=1, sticky="nswe", padx=(10,0), pady=(10,0))
        self.BAGgraphInfoAddedEdgesLabel.grid(row=0, column=2, sticky="nswe", padx=(10,0), pady=(10,0))
        self.BAGgraphInfoLoopCountLabel.grid(row=0, column=3, sticky="nswe", padx=(10,10), pady=(10,0))
        self.BAGgraphInfoDeg.grid(row=1, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphInfoConnDeg.grid(row=1, column=1, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphInfoAddedEdges.grid(row=1, column=2, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphInfoLoopCount.grid(row=1, column=3, sticky="nswe", padx=(10,10), pady=(10,10))
        self.BAGgraphDeg.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphConnDeg.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphAddedEdges.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGgraphLoopCount.grid(row=0, column=0, sticky="nswe", padx=(10,10), pady=(10,10))
        # parameters window
        self.BAGoptions = customtkinter.CTkFrame(master=self.FrameBAG, height=210, width=1500, corner_radius=self.CORNER_RADIUS)
        self.BAGparam = customtkinter.CTkFrame(master=self.BAGoptions, height=200, width=490, corner_radius=self.CORNER_RADIUS)
        self.BAGseed = customtkinter.CTkFrame(master=self.BAGoptions, height=200, width=490, corner_radius=self.CORNER_RADIUS)
        self.BAGbuttons = customtkinter.CTkFrame(master=self.BAGoptions, height=200, width=490, corner_radius=self.CORNER_RADIUS)
        self.BAGoptions.grid(row=1, column=0, sticky="nswe", padx=(10,10), pady=(10,10))
        self.BAGparam.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGseed.grid(row=0, column=1, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BAGbuttons.grid(row=0, column=2, sticky="nswe", padx=(10,10), pady=(10,10))
        
        ######################
        #    radiobuttons    #
        ######################
        self.BAGlabedParam = customtkinter.CTkLabel(master=self.BAGparam,anchor=customtkinter.W,text='Способы задания графа:')
        self.BAGselected = IntVar(value=0)
        self.BAGradGraph = customtkinter.CTkRadioButton(master=self.BAGparam,width=460,text='Граф', 
            value=0, variable=self.BAGselected, command = lambda v=0: self.updateSliders(v))
        self.BAGradPseudograph = customtkinter.CTkRadioButton(master=self.BAGparam,width=460,text='Псевдограф',
            value=1, variable=self.BAGselected, command = lambda v=1: self.updateSliders(v))
        self.BAGradMultiGraph = customtkinter.CTkRadioButton(master=self.BAGparam,width=460,text='Мультиграф', 
            value=2, variable=self.BAGselected, command = lambda v=2: self.updateSliders(v))
        self.BAGradPseudoMultiGraph = customtkinter.CTkRadioButton(master=self.BAGparam,width=460,text='Псевдомультиграф', 
            value=3, variable=self.BAGselected, command = lambda v=3: self.updateSliders(v))
        self.BAGlabelSeed = customtkinter.CTkLabel(master=self.BAGseed,anchor=customtkinter.W,text='Затравка:')
        self.BAGselectedSeed = IntVar(value=0)
        self.BAGradDeg1_1 = customtkinter.CTkRadioButton(master=self.BAGseed,width=460,text='Степени 1-1', 
            value=0, variable=self.BAGselectedSeed, command = lambda v=0: self.updateSliders(v))
        self.BAGradDeg2_2_2 = customtkinter.CTkRadioButton(master=self.BAGseed,width=460,text='Степени 2-2-2', 
            value=1, variable=self.BAGselectedSeed, command = lambda v=1: self.updateSliders(v))
        self.BAGradDeg1_2_2_3 = customtkinter.CTkRadioButton(master=self.BAGseed,width=460,text='Степени 1-2-2-3', 
            value=2, variable=self.BAGselectedSeed, command = lambda v=2: self.updateSliders(v))
        #plotting elements
        self.BAGlabedParam.grid(row=0, column=0, sticky="nswe", padx=10, pady=10) 
        self.BAGradGraph.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGradPseudograph.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGradMultiGraph.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGradPseudoMultiGraph.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        #plotting elements
        self.BAGlabelSeed.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGradDeg1_1.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGradDeg2_2_2.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGradDeg1_2_2_3.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
                
        ##################
        #    buttons     #
        ##################
        bag = BAG()
        self.edgesCount = 1
        self.BAGlabelEdges = customtkinter.CTkLabel(master=self.BAGbuttons,height=20,anchor=customtkinter.W,text=f"Количество добавляемых ребер: {self.edgesCount}")
        self.BAGsliderEdges = customtkinter.CTkSlider(master=self.BAGbuttons,height=25,width=480,from_=1, to=26, number_of_steps=25)
        self.BAGbtnCreate = customtkinter.CTkButton(master=self.BAGbuttons,text="Построить граф заново",height=35,width=480,command=bag.newGraph)
        self.BAGbtnAdd = customtkinter.CTkButton(master=self.BAGbuttons,text="Добавить вершину",height=35,width=480,command=bag.addVertex)
        self.BAGlabelEdges.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGsliderEdges.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGbtnCreate.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGbtnAdd.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGsliderEdges.configure(command = lambda v=self.edgesCount: self.updateCountSliderLabelBAG(v))
        self.BAGsliderEdges.set(self.edgesCount)
        
        
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create BRG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        
        self.FrameBRG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FrameBRG.rowconfigure(0, weight=1)
        self.FrameBRG.columnconfigure(0, weight=1)
        # Frame window - left one
        graph = customtkinter.CTkImage(light_image=Image.open(os.path.join("Assets/Images/BRG.png")), dark_image=Image.open(os.path.join("Assets/Images/BRG.png")), size=(self.S_GRAPH_WIDTH,self.S_GRAPH_HEIGHT))
        self.BRGgraphFrame = customtkinter.CTkFrame(master=self.FrameBRG, width=self.S_GRAPH_WIDTH+20, height=self.S_GRAPH_HEIGHT+20, corner_radius=self.CORNER_RADIUS)
        self.BRGgraphVisualizeFrame = customtkinter.CTkFrame(master=self.BRGgraphFrame, width=self.S_GRAPH_WIDTH+20, height=self.S_GRAPH_HEIGHT+20, corner_radius=self.CORNER_RADIUS)
        self.BRGgraphInfoFrame = customtkinter.CTkFrame(master=self.BRGgraphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.BRGgraphImage = customtkinter.CTkLabel(master=self.BRGgraphVisualizeFrame,width=self.S_GRAPH_WIDTH,height=self.S_GRAPH_HEIGHT,text="",image=graph)
        self.BRGlabelConnectivity = customtkinter.CTkLabel(master=self.BRGgraphInfoFrame,width=(self.S_GRAPH_WIDTH/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Связность")
        self.BRGlabelPlanarity = customtkinter.CTkLabel(master=self.BRGgraphInfoFrame,width=(self.S_GRAPH_WIDTH/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Планарность")
        self.BRGlabelTrianglesPresence= customtkinter.CTkLabel(master=self.BRGgraphInfoFrame,width=(self.S_GRAPH_WIDTH/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Наличие треугольников")
        self.BRGgraphFrame.grid(row=0, column=0, sticky="nswe", padx=(10,0), pady=(10,10))
        self.BRGgraphVisualizeFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGgraphInfoFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        # Parameters window - right one
        self.BRGparametersFrame = customtkinter.CTkFrame(master=self.FrameBRG, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BRGoptionsFrame = customtkinter.CTkFrame(master=self.BRGparametersFrame, width=500, corner_radius=self.CORNER_RADIUS)
        self.BRGinputFrame = customtkinter.CTkFrame(master=self.BRGparametersFrame, width=500, corner_radius=self.CORNER_RADIUS)
        self.BRGbuttonsFrame = customtkinter.CTkFrame(master=self.BRGparametersFrame, width=500, corner_radius=self.CORNER_RADIUS)
        self.BRGparametersFrame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.BRGoptionsFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGinputFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGbuttonsFrame.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGgraphImage.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.BRGlabelConnectivity.grid(row=0, column=0, sticky="nswe", padx=5, pady=0)
        self.BRGlabelPlanarity.grid(row=0, column=1, sticky="nswe", padx=5, pady=0)
        self.BRGlabelTrianglesPresence.grid(row=0, column=2, sticky="nswe", padx=5, pady=0)
        
        ##########################################
        #    creating elements for graphFrame    #
        ##########################################
    
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  setting up default parameters
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        
        # select default theme
        self.switcherTheme.select()
        customtkinter.set_appearance_mode("Dark")
        # select default frame
        self.select_frame_by_name("BAG")
        # update sliders
        self.updateSliders(0)
    
    #################################################################################################################################################################################
    #################################################################################################################################################################################
    #################################################################################################################################################################################
    #  defining functions
    #################################################################################################################################################################################
    #################################################################################################################################################################################
    #################################################################################################################################################################################
    
    def updateConstSliderLabel(self,v):
        self.ERGlabelCConst.configure(text=f"Константа C: {float('{:.2f}'.format(v))}")

    def updatePropSliderLabel(self,v):
        self.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(v))}")

    def updateCountSliderLabel(self,v):
        self.ERGlabelVertex.configure(text=f"Количество вершин в графе: {int(v)}")
        if v > 20:
            self.ERGsliderPropability.set(0.4)
            self.ERGlabelPropability.configure(text=f"Вероятность появления ребер в графе: {0.4}")
            self.ERGsliderPropability.configure(to=0.8, number_of_steps=80, button_color=App.Colors.sliderWarning,progress_color=App.Colors.sliderWarning)
        else:
            self.ERGsliderPropability.configure(to=1, number_of_steps=100, button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
                        

    def updateCountSliderLabelBAG(self,v):
        self.BAGlabelEdges.configure(text=f"Количество добавляемых ребер: {int(v)}")

    def updateSliders(self, v):
        if v in [0, 7]:
            self.ERGsliderVertex.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
            self.ERGsliderPropability.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
            self.ERGsliderCConstant.configure(state="disabled",button_color=App.Colors.sliderDisabled,progress_color=App.Colors.sliderDisabled)
        elif v in [1, 2, 3, 4, 5, 6]:
            self.ERGsliderVertex.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
            self.ERGsliderPropability.configure(state="disabled",button_color=App.Colors.sliderDisabled,progress_color=App.Colors.sliderDisabled)
            self.ERGsliderCConstant.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.MenuButtonERG.configure(fg_color=("gray75", "gray25") if name == "ERG" else "transparent")
        self.MenuButtonBAG.configure(fg_color=("gray75", "gray25") if name == "BAG" else "transparent")
        self.MenuButtonBRG.configure(fg_color=("gray75", "gray25") if name == "BRG" else "transparent")
        # show selected frame
        if name == "ERG":
            self.FrameERG.grid(row=0, column=1, sticky="nsew")
        else:
            self.FrameERG.grid_forget()
        if name == "BAG":
            self.FrameBAG.grid(row=0, column=1, sticky="nsew")
        else:
            self.FrameBAG.grid_forget()
        if name == "BRG":
            self.FrameBRG.grid(row=0, column=1, sticky="nsew")
        else:
            self.FrameBRG.grid_forget()

    def MenuButtonERG_event(self):
        self.select_frame_by_name("ERG")

    def MenuButtonBAG_event(self):
        self.select_frame_by_name("BAG")

    def MenuButtonBRG_event(self):
        self.select_frame_by_name("BRG")

    def changeThemeMode(self):
        if self.switcherTheme.get() == 1:
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")
            
    def on_closing(self, event=0):
        self.quit()




if __name__ == "__main__":
    app = App()
    app.mainloop()