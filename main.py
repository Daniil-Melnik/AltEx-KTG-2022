import tkinter

import customtkinter
import os
from PIL import Image


#################################################################################################################################################################################
#################################################################################################################################################################################
#  Setting initial main window parameters
#################################################################################################################################################################################
#################################################################################################################################################################################
class App(customtkinter.CTk):
    ######################################################################
    #    Setting the parameters and the class for working with colors    #
    ######################################################################
    WIDTH = 1860
    HEIGHT = 1000
    GRAPH_RESOLUTION = HEIGHT-100
    CORNER_RADIUS = 10

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
        self.MenuButtonERG.grid(row=1, column=0, sticky="ew")
        self.MenuButtonBAG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Барабаши-Альберт", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonBAG_event)
        self.MenuButtonBAG.grid(row=2, column=0, sticky="ew")
        self.MenuButtonBRG = customtkinter.CTkButton(self.Menu, corner_radius=0, height=40, border_spacing=10, text="Модель Баллобаша-Риордана", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.MenuButtonBRG_event)
        self.MenuButtonBRG.grid(row=3, column=0, sticky="ew")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.Menu, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        ##########################
        #    create ERG frame    #
        ##########################
        self.FrameERG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FrameERG.grid_columnconfigure(0, weight=1)

        



        self.FrameERG_large_image_label = customtkinter.CTkLabel(self.FrameERG, text="", image=self.imageERG)
        self.FrameERG_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        self.FrameERG_button_4 = customtkinter.CTkButton(self.FrameERG, text="CTkButton", image=self.imageERG, compound="bottom", anchor="w")
        self.FrameERG_button_4.grid(row=4, column=0, padx=20, pady=10)

        ##########################
        #    create BAG frame    #
        ##########################
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        ##########################
        #    create BRG frame    #
        ##########################
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