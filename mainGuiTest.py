import gc
import os
import sys
import math
import shutil
import random
import pymysql
import platform
import itertools
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
#  Algorithm
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
    WIDTH = 1360
    HEIGHT = 900
    GRAPH_RESOLUTION = HEIGHT-100
    CORNER_RADIUS = 10
    # color class
    class Colors:
        graphInfoTrue = "#84a98c"
        graphInfoFalse = "#9b2226"
        graphBackground = "#9b2226"
    ################################################
    #    Class initialization - object creation    #
    ################################################
    def __init__(self):
        # Parent class definition
        super().__init__()
        # Setting initial window settings
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.resizable(False, False)
        self.title("Модель случайного графа Эрдёша-Реньи")
        self.geometry(f"{App.WIDTH+20}x{App.HEIGHT+20}")
        # Настройка макета сетки (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        #   Creating frames
        #################################################################################################################################################################################
        #################################################################################################################################################################################
        self.mainFrame = customtkinter.CTkFrame(master=self, width=self.WIDTH, height=self.HEIGHT, corner_radius=0)
        self.mainFrame.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.mainFrame.rowconfigure(14, weight=10)
        self.mainFrame.columnconfigure(0, weight=1)
        #################################
        #    Frame window - left one    #
        #################################
        self.L_graphFrame = customtkinter.CTkFrame(master=self.mainFrame, width=self.GRAPH_RESOLUTION+20, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
        self.L_graphFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        # Зависсивые окна
        self.graphVisualizeFrame = customtkinter.CTkFrame(master=self.L_graphFrame, width=self.GRAPH_RESOLUTION, height=self.GRAPH_RESOLUTION, corner_radius=self.CORNER_RADIUS)
        self.graphInfoFrame = customtkinter.CTkFrame(master=self.L_graphFrame, height=60, corner_radius=self.CORNER_RADIUS)
        self.graphVisualizeFrame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.graphInfoFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        #######################################
        #    Parameters window - right one    #
        #######################################
        self.R_parametersFrame = customtkinter.CTkFrame(master=self.mainFrame, height=self.HEIGHT, corner_radius=self.CORNER_RADIUS)
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
        # graph = customtkinter.CTkImage(light_image=Image.open(os.path.join("Assets/images/start.png")), dark_image=Image.open(os.path.join("Assets/images/start.png")), size=(54,54))
        graph = PIL.Image.open("Assets/Images/start.png")
        self.graphImage = customtkinter.CTkLabel(master=self.graphVisualizeFrame, width=self.GRAPH_RESOLUTION-10, height=self.GRAPH_RESOLUTION-10,text="")
        self.graphImage.image = ImageTk.PhotoImage(graph)
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
        self.selected = IntVar()
        self.labedRad = customtkinter.CTkLabel(master=self.optionsFrame,text='Способы задания графа:')
        self.radProbability = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Вероятностный граф', value=1, variable=self.selected)
        self.radConnectivity = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Связность (теорема 13)', value=2, variable=self.selected)
        self.radPlanarity = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Планарность (теорема 26)', value=3, variable=self.selected)
        self.radNonTriangle = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Присутствие треугольников (теорема 12)', value=4, variable=self.selected)
        self.radTriangle = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Отсутствие треугольников (теорема 10)', value=5, variable=self.selected)
        self.radFeudalFrag = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Феодальная раздробленность (стр. 48)', value=6, variable=self.selected)
        self.radEmpire = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Империя (стр. 48)', value=7, variable=self.selected)
        self.radGiantConnComp = customtkinter.CTkRadioButton(master=self.optionsFrame,text='Гигантская компонента связности', value=8, variable=self.selected)
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
        self.txtnLabel = customtkinter.CTkLabel(master=self.inputFrame,width=480,text="Количество вершин в графе:")
        self.txtpLabel = customtkinter.CTkLabel(master=self.inputFrame,width=480,text="Вероятность появления ребер в графе:")
        self.txtсLabel = customtkinter.CTkLabel(master=self.inputFrame,width=480,text="С:")
        self.txtn = customtkinter.CTkEntry(master=self.inputFrame,height=40,width=480,placeholder_text="Введите количество вершин")
        self.txtp = customtkinter.CTkEntry(master=self.inputFrame,height=40,width=480,placeholder_text="Введите вероятность")
        self.txtс = customtkinter.CTkEntry(master=self.inputFrame,height=40,width=480,placeholder_text="Задайте C")
        self.txtnLabel.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.txtpLabel.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
        self.txtсLabel.grid(row=4, column=0, sticky="nswe",padx=10, pady=10)
        self.txtn.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        self.txtp.grid(row=3, column=0, sticky="nswe", padx=10, pady=10)
        self.txtс.grid(row=5, column=0, sticky="nswe", padx=10, pady=10)
        ############################################
        #    creating elements for buttonsFrame    #
        ############################################
        self.btnCreate = customtkinter.CTkButton(master=self.buttonsFrame,text="Построить граф",height=40,width=480,command=ERG)
        self.btnSave = customtkinter.CTkButton(master=self.buttonsFrame,text="Сохранить изображение графа",height=40,width=480)
        self.btnCreate.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
        self.btnSave.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
        
        
        
        
    #########################################################
    #    cleaning the window and exiting the application    #
    #########################################################
    def start(self):
        self.mainloop()
 
        
        
#################################################################################################################################################################################
#################################################################################################################################################################################
#   Program initialization
#################################################################################################################################################################################
#################################################################################################################################################################################
if __name__ == "__main__":
    app = App()
    app.start()