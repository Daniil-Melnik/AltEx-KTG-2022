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
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
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
        graph = PIL.Image.open("Assets/images/start.png")
        self.graphImage = customtkinter.CTkCanvas(master=self.graphVisualizeFrame, width=self.GRAPH_RESOLUTION-10, height=self.GRAPH_RESOLUTION-10,background="Black")
        self.graphImage.image = ImageTk.PhotoImage(graph) 
        self.graphImage.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.labelConnectivity = customtkinter.CTkLabel(master=self.graphInfoFrame,width=(self.GRAPH_RESOLUTION/3)-20,height=50,text="Связность")
        self.labelPlanarity = customtkinter.CTkLabel(master=self.graphInfoFrame,width=(self.GRAPH_RESOLUTION/3)-20,height=50,text="Планарность")
        self.labelTrianglesPresence= customtkinter.CTkLabel(master=self.graphInfoFrame,width=(self.GRAPH_RESOLUTION/3)-20,height=50,text="Наличие треугольников")
        self.labelConnectivity.grid(row=0, column=0, sticky="nswe", padx=0, pady=0)
        self.labelPlanarity.grid(row=0, column=1, sticky="nswe", padx=0, pady=0)
        self.labelTrianglesPresence.grid(row=0, column=2, sticky="nswe", padx=0, pady=0)
        #################################################
        #    creating elements for R_parametersFrame    #
        #################################################
        
        
        
        
        
    #########################################################
    #    cleaning the window and exiting the application    #
    #########################################################
    def on_closing(self, event=0):
        self.destroy()
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