import tkinter

import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Модели случайных графов")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.geometry("1470x820")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        pathImages = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets/Images")
        pathIcons = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Assets/Icons")   
        self.imageLogo = customtkinter.CTkImage(Image.open(os.path.join(pathIcons, "Leti_logo.png")), size=(32, 32))
        self.imageERG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(500, 300))
        self.imageBAG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(500, 300))
        self.imageBRG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(500, 300))
        self.menuImageERG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(24, 24))
        self.menuImageBAG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(24, 24))
        self.menuImageBRG = customtkinter.CTkImage(Image.open(os.path.join(pathImages, "BG_Barabasi_Albert.png")), size=(24, 24))

        #################################
        #    create navigation frame    #
        #################################
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Модели случайных графов", image=self.imageLogo, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.MenuButtonERG = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.imageERG, anchor="w", command=self.MenuButtonERG_event)
        self.MenuButtonERG.grid(row=1, column=0, sticky="ew")
        self.MenuButtonBAG = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.imageERG, anchor="w", command=self.MenuButtonBAG_event)
        self.MenuButtonBAG.grid(row=2, column=0, sticky="ew")
        self.MenuButtonBRG = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.imageERG, anchor="w", command=self.MenuButtonBRG_event)
        self.MenuButtonBRG.grid(row=3, column=0, sticky="ew")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        ##########################
        #    create ERG frame    #
        ##########################
        self.FrameERG = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FrameERG.grid_columnconfigure(0, weight=1)

        self.FrameERG_large_image_label = customtkinter.CTkLabel(self.FrameERG, text="", image=self.imageERG)
        self.FrameERG_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.FrameERG_button_1 = customtkinter.CTkButton(self.FrameERG, text="", image=self.imageERG)
        self.FrameERG_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.FrameERG_button_2 = customtkinter.CTkButton(self.FrameERG, text="CTkButton", image=self.imageERG, compound="right")
        self.FrameERG_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.FrameERG_button_3 = customtkinter.CTkButton(self.FrameERG, text="CTkButton", image=self.imageERG, compound="top")
        self.FrameERG_button_3.grid(row=3, column=0, padx=20, pady=10)
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
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.MenuButtonERG.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.MenuButtonBAG.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.MenuButtonBRG.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.FrameERG.grid(row=0, column=1, sticky="nsew")
        else:
            self.FrameERG.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def MenuButtonERG_event(self):
        self.select_frame_by_name("home")

    def MenuButtonBAG_event(self):
        self.select_frame_by_name("frame_2")

    def MenuButtonBRG_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()




if __name__ == "__main__":
    app = App()
    app.mainloop()