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
    BV=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    E=[]
    val_map = {}
    n=int(app.txtn.get()) 
    us = app.selected.get()
    print(us)
    if (us==1):
        p=float(app.txtp.get())
        app.txtс.delete(0, END)
        app.txtс.insert(0,'c')
    elif (us==2):
        c=float(app.txtс.get())
        p=c*(math.log(n)/n)
        app.txtp.delete(first=0,last=END)
        app.txtp.insert(0, str(p))
    elif (us==3):
        c=float(app.txtс.get())
        p=c/n
        app.txtp.delete(first=0,last=END)
        app.txtp.insert(0, str(p))
    elif (us==4):
        w=n/math.log(n)
        p=w/n
        app.txtp.delete(first=0,last=END)
        app.txtp.insert(0, str(p))
    elif (us==5):
        a=1/n
        p=a/n
        app.txtp.delete(first=0,last=END)
        app.txtp.insert(0, str(p))
    elif (us==6):
        p=1/(n**3)
        app.txtp.delete(first=0,last=END)
        app.txtp.insert(0, str(p))
    elif (us==7):
        p=n*math.log(n)/n
        app.txtp.delete(first=0,last=END)
        app.txtp.insert(0, str(p))
    elif (us==8):
        p=float(txtp.get())
        app.txtс.delete(0, END)
        app.txtс.insert(0,'c')

    V=[]
    for i in range(n*(n-1)//2):
        E.append([])

    for i in range (n):
        V.append(BV[i])
        val_map[BV[i]]=1.0
    m=0

    for i in range(n):
        for j in range(i+1, len(V)):
            E[m].append(V[i])
            E[m].append(V[j])
            m+=1
    
    G = nx.Graph()
    G.add_nodes_from(V)
    for i in range (n*(n-1)//2):
        k=random.randint(0,1000)/1000
        if (k<=p):
            G.add_edge(E[i][0],E[i][1])    
    
    if (us==4):
        all_cliques= nx.enumerate_all_cliques(G)
        triad_cliques=[x for x in all_cliques if len(x)==3 ]
        if (len(triad_cliques)!=0):
            for v in triad_cliques[0]:
                val_map[v]=0.1
            
    
    all_cliques= nx.enumerate_all_cliques(G)
    if triad_cliques := [x for x in all_cliques if len(x) == 3]:
        app.labelTrianglesPresence.configure(fg_color=App.Colors.graphInfoTrue)
    else:
        app.labelTrianglesPresence.configure(fg_color=App.Colors.graphInfoFalse)

    if (us==8):
        for v in (max(nx.connected_components(G))):
            val_map[v]=0.1 

    values = [val_map.get(node, 0.25) for node in G.nodes()]

    plt.clf()
    if (nx.check_planarity(G, counterexample=False)[0]==True):
        nx.draw_planar(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        app.labelPlanarity.configure(fg_color=App.Colors.graphInfoTrue)
    else:
        nx.draw_circular(G, cmap=plt.get_cmap('viridis'), node_color=values, with_labels=True, font_color='white')
        app.labelPlanarity.configure(fg_color=App.Colors.graphInfoFalse)

    if (nx.is_connected(G)):
        app.labelConnectivity.configure(fg_color=App.Colors.graphInfoTrue)
    else:
        app.labelConnectivity.configure(fg_color=App.Colors.graphInfoFalse)
        
    print(max(nx.connected_components(G)))
    plt.axis('on')
    plt.savefig("st.png")
    plt.clf()
    plt.subplot(212)
        
    topImg = PhotoImage(file="st.png")
    app.graphImage.configure(image=topImg)
    app.graphImage.image = topImg

    # topImg = PhotoImage(file="st.png")
    # topImg = customtkinter.CTkImage(light_image=Image.open(os.path("st.png")), dark_image=Image.open(os.path.join(App.PIECE_DIR, 'bB.png')), size=(App.GRAPH_RESOLUTION,App.GRAPH_RESOLUTION))
    # app.graphImage.configure(image=topImg)
    # app.graphImage.image = topImg

#################################################################################################################################################################################
#################################################################################################################################################################################
#  Setting initial main window parameters
#################################################################################################################################################################################
#################################################################################################################################################################################
class App(customtkinter.CTk):
    ######################################################################
    #    Setting the parameters and the class for working with colors    #
    ######################################################################
    WIDTH = 1580
    HEIGHT = 900
    GRAPH_RESOLUTION = HEIGHT-100
    CORNER_RADIUS = 10
    # color class
    class Colors:
        graphInfoTrue = "#84a98c"
        graphInfoFalse = "#9b2226"
        graphBackground = "#9b2226"

    def __init__(self): 
        super().__init__()

        self.resizable(False, False)
        self.title("Модели случайных графов")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.geometry(f"{App.WIDTH+20}x{App.HEIGHT+20}")

        #############################
        #    set grid layout 1x2    #
        #############################х
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ####################################################
        #    load images with light and dark mode image    #
        ####################################################
        pathImages = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets/Images")
        pathIcons = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets/Icons")   
        self.imageLogo = customtkinter.CTkImage(Image.open(os.path.join(pathIcons, "leti.png")), size=(32, 32))
        self.imageERG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Erdos_Renyi.png")), size=(500, 300))
        self.imageBAG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(500, 300))
        self.imageBRG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Bollobas_Riordan.png")), size=(500, 300))

        #################################
        #    create navigation frame    #
        #################################
        self.Menu = customtkinter.CTkFrame(self, corner_radius=0)
        self.Menu.grid(row=0, column=0, sticky="nsew")
        self.Menu.grid_rowconfigure(4, weight=1)
        self.MenuLabel = customtkinter.CTkLabel(self.Menu, text="  Случайные графы", image=self.imageLogo, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.MenuLabel.grid(row=0, column=0, padx=20, pady=20)
        self.MenuButtonERG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Эрдёша-Реньи", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonERG_event)
        self.MenuButtonBAG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Барабаши-Альберт", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonBAG_event)
        self.MenuButtonBRG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Баллобаша-Риордана", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonBRG_event)
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.Menu, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.MenuButtonERG.grid(row=1, column=0, sticky="ew")
        self.MenuButtonBAG.grid(row=2, column=0, sticky="ew")
        self.MenuButtonBRG.grid(row=3, column=0, sticky="ew")
        self.appearance_mode_menu.grid(row=10, column=0, padx=10, pady=10, sticky="s")

        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create ERG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #frame
        self.FrameERG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # self.FrameERG.grid_columnconfigure(0, weight=1)
        self.FrameERG.rowconfigure(14, weight=10)
        self.FrameERG.columnconfigure(0, weight=1)
        # Frame window - left one
        self.L_graphFrame = customtkinter.CTkFrame(master=self.FrameERG, width=self.GRAPH_RESOLUTION+20, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.L_graphFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        # Зависсивые окна
        self.graphVisualizeFrame = customtkinter.CTkFrame(master=self.L_graphFrame, width=self.GRAPH_RESOLUTION, height=self.GRAPH_RESOLUTION, corner_radius=self.CORNER_RADIUS)
        self.graphInfoFrame = customtkinter.CTkFrame(master=self.L_graphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.graphVisualizeFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.graphInfoFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        # Parameters window - right one
        self.R_parametersFrame = customtkinter.CTkFrame(master=self.FrameERG, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.R_parametersFrame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        # Зависсивые окна
        self.optionsFrame = customtkinter.CTkFrame(master=self.R_parametersFrame, height=self.GRAPH_RESOLUTION/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.inputFrame = customtkinter.CTkFrame(master=self.R_parametersFrame, height=self.GRAPH_RESOLUTION/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.buttonsFrame = customtkinter.CTkFrame(master=self.R_parametersFrame, height=self.GRAPH_RESOLUTION/3, width=500, corner_radius=self.CORNER_RADIUS)
        self.optionsFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.inputFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.buttonsFrame.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        ############################################
        #    creating elements for L_graphFrame    #
        ############################################
        graph = customtkinter.CTkImage(light_image=Image.open(os.path.join("Assets/Images/BG_Erdos_Renyi.png")), dark_image=Image.open(os.path.join("Assets/Images/BG_Erdos_Renyi.png")), size=(self.GRAPH_RESOLUTION-20,self.GRAPH_RESOLUTION-20))
        # graph = PIL.Image.open("Assets/Images/BG_Erdos_Renyi.png")
        self.graphImage = customtkinter.CTkLabel(master=self.graphVisualizeFrame,width=self.GRAPH_RESOLUTION-10,height=self.GRAPH_RESOLUTION-10,text="",image=graph)
        self.graphImage.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.labelConnectivity = customtkinter.CTkLabel(master=self.graphInfoFrame,width=(self.GRAPH_RESOLUTION/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Связность")
        self.labelPlanarity = customtkinter.CTkLabel(master=self.graphInfoFrame,width=(self.GRAPH_RESOLUTION/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Планарность")
        self.labelTrianglesPresence= customtkinter.CTkLabel(master=self.graphInfoFrame,width=(self.GRAPH_RESOLUTION/3)-10,height=50,bg_color=App.Colors.graphInfoFalse,text="Наличие треугольников")
        self.labelConnectivity.grid(row=0, column=0, sticky="nswe", padx=5, pady=0)
        self.labelPlanarity.grid(row=0, column=1, sticky="nswe", padx=5, pady=0)
        self.labelTrianglesPresence.grid(row=0, column=2, sticky="nswe", padx=5, pady=0)
        ############################################
        #    creating elements for optionsFrame    #
        ############################################
        self.selected = IntVar(value=0)
        self.labedRad = customtkinter.CTkLabel(master=self.optionsFrame,anchor=customtkinter.W,text='Способы задания графа:')
        self.radProbability = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Вероятностный граф', 
            value=0, variable=self.selected)
        self.radConnectivity = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Связность (теорема 13)', 
            value=1, variable=self.selected)
        self.radPlanarity = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Планарность (теорема 26)', 
            value=2, variable=self.selected)
        self.radNonTriangle = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Присутствие треугольников (теорема 12)', 
            value=3, variable=self.selected)
        self.radTriangle = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Отсутствие треугольников (теорема 10)', 
            value=4, variable=self.selected)
        self.radFeudalFrag = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Феодальная раздробленность (стр. 48)', 
            value=5, variable=self.selected)
        self.radEmpire = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Империя (стр. 48)', 
            value=6, variable=self.selected)
        self.radGiantConnComp = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Гигантская компонента связности', 
            value=8, variable=self.selected)
        #plotting elements
        self.labedRad.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.radProbability.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.radConnectivity.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.radPlanarity.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.radNonTriangle.grid(row=4, column=0, sticky="nswe", padx=10, pady=10)
        self.radTriangle.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        self.radFeudalFrag.grid(row=6, column=0, sticky="nswe", padx=10, pady=10)
        self.radEmpire.grid(row=7, column=0, sticky="nswe", padx=10, pady=10)
        self.radGiantConnComp.grid(row=8, column=0, sticky="nswe", padx=10, pady=10)
        ##########################################
        #    creating elements for inputFrame    #
        ##########################################
        vertexCount = 8
        propability = 0.5
        constantC = 1
        self.labelTxtn = customtkinter.CTkLabel(master=self.inputFrame,anchor=customtkinter.W,text="Количество вершин в графе:")
        self.labelTxtp = customtkinter.CTkLabel(master=self.inputFrame,anchor=customtkinter.W,text="Вероятность появления ребер в графе:")
        self.labelTxtc = customtkinter.CTkLabel(master=self.inputFrame,anchor=customtkinter.W,text="Константа C:")
        self.txtn = customtkinter.CTkEntry(master=self.inputFrame,height=40,width=480,placeholder_text="Введите количество вершин")
        self.txtp = customtkinter.CTkEntry(master=self.inputFrame,height=40,width=480,placeholder_text="Введите вероятность")
        self.txtс = customtkinter.CTkEntry(master=self.inputFrame,height=40,width=480,placeholder_text="Задайте константу C")
        self.sliderVertexCount = customtkinter.CTkSlider(master=self.inputFrame,height=25,width=480,from_=1, to=26, number_of_steps=25)
        self.sliderPropability = customtkinter.CTkSlider(master=self.inputFrame,height=25,width=480,from_=0, to=1, number_of_steps=100)
        self.sliderCConstant = customtkinter.CTkSlider(master=self.inputFrame,height=25,width=480,from_=0, to=10, number_of_steps=100)
        self.sliderVertexCount.set(vertexCount)
        self.sliderPropability.set(propability)
        self.sliderCConstant.set(constantC)
        self.labelTxtn.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.labelTxtp.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.labelTxtc.grid(row=4, column=0, sticky="nswe",padx=10, pady=10)
        self.sliderVertexCount.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.sliderPropability.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.sliderCConstant.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        ############################################
        #    creating elements for buttonsFrame    #
        ############################################
        self.btnCreate = customtkinter.CTkButton(master=self.buttonsFrame,text="Построить граф",height=40,width=480)
        self.btnSave = customtkinter.CTkButton(master=self.buttonsFrame,text="Сохранить граф как картинку",height=40,width=480)
        self.btnCreate.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.btnSave.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)

        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create BAG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################

        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #  create BRG frame
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("ERG")

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
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "BRG":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def MenuButtonERG_event(self):
        self.select_frame_by_name("ERG")

    def MenuButtonBAG_event(self):
        self.select_frame_by_name("BAG")

    def MenuButtonBRG_event(self):
        self.select_frame_by_name("BRG")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()




if __name__ == "__main__":
    app = App()
    app.mainloop()