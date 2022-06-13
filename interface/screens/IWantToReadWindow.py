
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class IWantToReadWindow:

    def __init__(self):        
        self.IWTR_window = Toplevel()
        x = self.IWTR_window.winfo_x()
        y = self.IWTR_window.winfo_y()
        self.IWTR_window.title("I Want to Read")
        self.IWTR_window.geometry(f"{x+870}x{y+200}")
        self.IWTR_window.configure(bg = "#2C0A59")
        self.IWTR_window.maxsize(width=988, height=700)#configura as dmensoes maximas da tela
        self.IWTR_window.minsize(width=400, height=170)

    def generate_IWTR_window(self):
        canvas = Canvas(
            self.IWTR_window,
            bg = "#2C0A59",
            height = 270,
            width = 870,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        image_image_WTR= PhotoImage(
            file=relative_to_assets("WTR.png"))
        canvas.create_image(
            179.0,
            47.0,
            image=image_image_WTR
        )

        canvas.place(x=0,y=0)

        self.IWTR_window.btn_2022inactive = PhotoImage(file=relative_to_assets("button_2022.png"))
        self.IWTR_window.btn_2022active = PhotoImage(file=relative_to_assets("button_2022Active.png"))

        button_image_2022 = PhotoImage(
            file=relative_to_assets("button_2022.png"))

        button_2022 = Button(
            self.IWTR_window,
            image=button_image_2022,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=lambda: print("button_2022 clicked"),
        )
        button_2022.place(
            x=22.76129150390624,
            y=111.438201904296,
        )

        button_2022.bind("<Enter>", lambda e: button_2022.config(image=self.IWTR_window.btn_2022active))
        button_2022.bind("<Leave>", lambda e: button_2022.config(image=self.IWTR_window.btn_2022inactive))


        self.IWTR_window.btn_2023inactive = PhotoImage(file=relative_to_assets("button_2023.png"))
        self.IWTR_window.btn_2023active = PhotoImage(file=relative_to_assets("button_2023Active.png"))

        button_image_2023 = PhotoImage(
            file=relative_to_assets("button_2023.png"))

        button_2023 = Button(
            self.IWTR_window,
            image=button_image_2023,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=lambda: print("button_2023 clicked"),
            
        )

        button_2023.place(
            x=173.8081817626953,
            y=112.17134094238281,

        )
        button_2023.bind("<Enter>", lambda e: button_2023.config(image=self.IWTR_window.btn_2023active))
        button_2023.bind("<Leave>", lambda e: button_2023.config(image=self.IWTR_window.btn_2023inactive))


        self.IWTR_window.btn_2024inactive = PhotoImage(file=relative_to_assets("button_2024.png"))
        self.IWTR_window.btn_2024active = PhotoImage(file=relative_to_assets("button_2024Active.png"))

        button_image_2024 = PhotoImage(
            file=relative_to_assets("button_2024.png"))

        button_2024 = Button(
            self.IWTR_window,
            image=button_image_2024,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=lambda: print("button_2024 clicked"),
            
        )
        button_2024.place(
            x=323.07843017578125,
            y=112.90451049804688,

        )

        button_2024.bind("<Enter>", lambda e: button_2024.config(image=self.IWTR_window.btn_2024active))
        button_2024.bind("<Leave>", lambda e: button_2024.config(image=self.IWTR_window.btn_2024inactive))


        self.IWTR_window.btn_2025inactive = PhotoImage(file=relative_to_assets("button_2025.png"))
        self.IWTR_window.btn_2025active = PhotoImage(file=relative_to_assets("button_2025Active.png"))

        button_image_2025 = PhotoImage(
            file=relative_to_assets("button_2025.png"))

        button_2025 = Button(
            self.IWTR_window,
            image=button_image_2025,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            relief="sunken",
            cursor="hand2",
            activebackground="#2C0A59",
            command=lambda: print("button_2025 clicked"),
            
        )
        button_2025.place(
            x=480.5277099609375,
            y=112.90451049804688,
        )

        button_2025.bind("<Enter>", lambda e: button_2025.config(image=self.IWTR_window.btn_2025active))
        button_2025.bind("<Leave>", lambda e: button_2025.config(image=self.IWTR_window.btn_2025inactive))

        self.IWTR_window.btn_IDKinactive = PhotoImage(file=relative_to_assets("button_IDK.png"))
        self.IWTR_window.btn_IDKactive = PhotoImage(file=relative_to_assets("button_IDKActive.png"))

        button_image_IDK = PhotoImage(
            file=relative_to_assets("button_IDK.png"))

        button_IDK = Button(
            self.IWTR_window,
            image=button_image_IDK,
            borderwidth=0,
            highlightthickness=0,
            bg="#2C0A59",
            bd=0,
            activebackground="#2C0A59",
            command=lambda: print("button_IDK clicked"),
            relief="sunken",
            cursor="hand2",
        )
        button_IDK.place(
            x=651.0565795898438,
            y=111.85713958740234,

        )

        button_IDK.bind("<Enter>", lambda e: button_IDK.config(image=self.IWTR_window.btn_IDKactive))
        button_IDK.bind("<Leave>", lambda e: button_IDK.config(image=self.IWTR_window.btn_IDKinactive))



        self.IWTR_window.resizable(False, False)
        self.IWTR_window.mainloop()