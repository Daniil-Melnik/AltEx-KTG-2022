import os
import sys
import math
import random
import customtkinter
import networkx as nx
import matplotlib.pyplot as plt
import PIL

from tkinter import *
from types import CellType
from tkinter.ttk import Checkbutton
from PIL import Image, ImageTk




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
    vertexCount=int(app.ERGsliderVertexCount.get())
    selectedRadioButton=app.selected.get()
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
    ##################################
    #    Планарность (теорема 26)    #
    ##################################
    elif (selectedRadioButton==2):
        constantC=float(app.ERGsliderCConstant.get())
        propability=constantC/vertexCount
        app.ERGsliderPropability.set(propability)
    ################################################
    #    Присутствие треугольников (теорема 12)    #
    ################################################
    elif (selectedRadioButton==3):
        w=vertexCount/math.log(vertexCount)
        propability=w/vertexCount
        app.ERGsliderPropability.set(propability)
     ###############################################
     #    Отсутствие треугольников (теорема 10)    #
     ###############################################
    elif (selectedRadioButton==4):
        a=1/vertexCount
        propability=a/vertexCount
        app.ERGsliderPropability.set(propability)
    ##############################################
    #    Феодальная раздробленность (стр. 48)    #
    ##############################################
    elif (selectedRadioButton==5):
        propability=1/(vertexCount**3)
        app.ERGsliderPropability.set(propability)
    ###########################
    #    Империя (стр. 48)    #
    ###########################
    elif (selectedRadioButton==6):
        propability=vertexCount*math.log(vertexCount)/vertexCount
        app.ERGsliderPropability.set(propability)
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
        k=random.randint(0,1000)/1000
        if (k<=propability):
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
    # plt.axis('on')
    plt.savefig("graph.png", dpi=150) # 960x720
    # plt.clf()
    # plt.subplot(212)
    topImg = customtkinter.CTkImage(light_image=Image.open(os.path.join("graph.png")), dark_image=Image.open(os.path.join("graph.png")),size=(app.GRAPH_WIDTH,app.GRAPH_HEIGHT))
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
    CORNER_RADIUS = 10
    # color class
    class Colors:
        graphInfoTrue = "#84a98c"
        graphInfoFalse = "#9b2226"
        graphBackground = "#9b2226"
        sliderEnabled = "#2a9d8f"
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
        self.ERGgraphFrame = customtkinter.CTkFrame(master=self.FrameERG, width=self.GRAPH_HEIGHT+20, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.ERGgraphVisualizeFrame = customtkinter.CTkFrame(master=self.ERGgraphFrame, width=self.GRAPH_HEIGHT, height=self.GRAPH_HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.ERGgraphInfoFrame = customtkinter.CTkFrame(master=self.ERGgraphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.ERGgraphFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
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
        self.selected = IntVar(value=0)
        #radiobuttons
        self.ERGradProbability = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Вероятностный граф', 
            value=0, variable=self.selected, command = lambda v=0: self.updateSliders(v))
        self.ERGradConnectivity = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Связность (теорема 13)', 
            value=1, variable=self.selected, command = lambda v=1: self.updateSliders(v))
        self.ERGradPlanarity = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Планарность (теорема 26)', 
            value=2, variable=self.selected, command = lambda v=2: self.updateSliders(v))
        self.ERGradNonTriangle = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Присутствие треугольников (теорема 12)', 
            value=3, variable=self.selected, command = lambda v=3: self.updateSliders(v))
        self.ERGradTriangle = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Отсутствие треугольников (теорема 10)', 
            value=4, variable=self.selected, command = lambda v=4: self.updateSliders(v))
        self.ERGradFeudalFrag = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Феодальная раздробленность (стр. 48)', 
            value=5, variable=self.selected, command = lambda v=5: self.updateSliders(v))
        self.ERGradEmpire = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Империя (стр. 48)', 
            value=6, variable=self.selected, command = lambda v=6: self.updateSliders(v))
        self.ERGradGiantConnComp = customtkinter.CTkRadioButton(master=self.ERGoptionsFrame,text='Гигантская компонента связности', 
            value=7, variable=self.selected, command = lambda v=7: self.updateSliders(v))
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
        self.ERGlabelTxtn = customtkinter.CTkLabel(master=self.ERGinputFrame,height=20,anchor=customtkinter.W,text=f"Количество вершин в графе: {self.vertexCount}")
        self.ERGlabelTxtp = customtkinter.CTkLabel(master=self.ERGinputFrame,height=20,anchor=customtkinter.W,text=f"Вероятность появления ребер в графе: {self.propability}")
        self.ERGlabelTxtc = customtkinter.CTkLabel(master=self.ERGinputFrame,height=20,anchor=customtkinter.W,text=f"Константа C: {self.constantC}")
        self.ERGsliderVertexCount = customtkinter.CTkSlider(master=self.ERGinputFrame,height=25,width=480,from_=1, to=26, number_of_steps=25)
        self.ERGsliderPropability = customtkinter.CTkSlider(master=self.ERGinputFrame,height=25,width=480,from_=0, to=1, number_of_steps=100)
        self.ERGsliderCConstant = customtkinter.CTkSlider(master=self.ERGinputFrame,height=25,width=480,from_=0, to=10, number_of_steps=1000)
        self.ERGsliderVertexCount.set(self.vertexCount)
        self.ERGsliderPropability.set(self.propability)
        self.ERGsliderCConstant.set(self.constantC)
        self.ERGsliderVertexCount.configure(command = lambda v=self.vertexCount: self.updateCountSliderLabel(v))
        self.ERGsliderPropability.configure(command = lambda v=self.propability: self.updatePropSliderLabel(v))
        self.ERGsliderCConstant.configure(command = lambda v=self.constantC: self.updateConstSliderLabel(v))
        #plotting elements
        self.ERGlabelTxtn.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGlabelTxtp.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.ERGlabelTxtc.grid(row=4, column=0, sticky="nswe",padx=10, pady=10)
        self.ERGsliderVertexCount.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
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
        self.FrameBRG.rowconfigure(14, weight=10)
        self.FrameBRG.columnconfigure(0, weight=1)
        # Frame window - left one
        self.BAGgraphFrame = customtkinter.CTkFrame(master=self.FrameBAG, width=self.GRAPH_HEIGHT+20, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphVisualizeFrame = customtkinter.CTkFrame(master=self.BAGgraphFrame, width=self.GRAPH_HEIGHT, height=self.GRAPH_HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphInfoFrame = customtkinter.CTkFrame(master=self.BAGgraphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.BAGgraphFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGgraphVisualizeFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGgraphInfoFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        # Parameters window - right one
        self.BAGparametersFrame = customtkinter.CTkFrame(master=self.FrameBAG, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BAGoptionsFrame = customtkinter.CTkFrame(master=self.BAGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.BAGinputFrame = customtkinter.CTkFrame(master=self.BAGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.BAGbuttonsFrame = customtkinter.CTkFrame(master=self.BAGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.BAGparametersFrame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.BAGoptionsFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGinputFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.BAGbuttonsFrame.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create BRG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        
        self.FrameBRG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FrameBRG.rowconfigure(14, weight=10)
        self.FrameBRG.columnconfigure(0, weight=1)
        # Frame window - left one
        self.BRGgraphFrame = customtkinter.CTkFrame(master=self.FrameBRG, width=self.GRAPH_HEIGHT+20, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BRGgraphVisualizeFrame = customtkinter.CTkFrame(master=self.BRGgraphFrame, width=self.GRAPH_HEIGHT, height=self.GRAPH_HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BRGgraphInfoFrame = customtkinter.CTkFrame(master=self.BRGgraphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.BRGgraphFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGgraphVisualizeFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGgraphInfoFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        # Parameters window - right one
        self.BRGparametersFrame = customtkinter.CTkFrame(master=self.FrameBRG, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.BRGoptionsFrame = customtkinter.CTkFrame(master=self.BRGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.BRGinputFrame = customtkinter.CTkFrame(master=self.BRGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.BRGbuttonsFrame = customtkinter.CTkFrame(master=self.BRGparametersFrame, height=self.GRAPH_HEIGHT/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.BRGparametersFrame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        self.BRGoptionsFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGinputFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.BRGbuttonsFrame.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)

    
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
        self.select_frame_by_name("ERG")
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
        self.ERGlabelTxtc.configure(text=f"Константа C: {float('{:.2f}'.format(v))}")

    def updatePropSliderLabel(self,v):
        self.ERGlabelTxtp.configure(text=f"Вероятность появления ребер в графе: {float('{:.2f}'.format(v))}")

    def updateCountSliderLabel(self,v):
        self.ERGlabelTxtn.configure(text=f"Количество вершин в графе: {int(v)}")

    def updateSliders(self, v):
        if v in [0, 7]:
            self.ERGsliderVertexCount.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
            self.ERGsliderPropability.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
            self.ERGsliderCConstant.configure(state="disabled",button_color=App.Colors.sliderDisabled,progress_color=App.Colors.sliderDisabled)
        elif v in [1, 2, 3, 4, 5, 6]:
            self.ERGsliderVertexCount.configure(state="normal",button_color=App.Colors.sliderEnabled,progress_color=App.Colors.sliderEnabled)
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