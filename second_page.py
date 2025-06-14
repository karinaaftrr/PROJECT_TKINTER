import tkinter as tk
from PIL import Image, ImageTk

class SecondPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Second Page")
        self.root.state("zoomed")

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.original_image = Image.open("asset/background.png")
        self.logo_image = Image.open("asset/Logo_Unila.png").resize((200, 150), Image.LANCZOS)
        self.rama_image = Image.open("asset/rama.png").resize((100,150), Image.LANCZOS)
        self.reggy_image = Image.open("asset/reggy.png").resize((100,150), Image.LANCZOS)
        self.karina_image = Image.open("asset/karina.png").resize((100,150), Image.LANCZOS)
        self.ikbal_image = Image.open("asset/ikbal.png").resize((100,150), Image.LANCZOS)

        self.bg_photo = None
        self.logo_photo = None
        self.rama_photo = None
        self.reggy_photo = None
        self.karina_photo = None
        self.ikbal_photo = None

        self.button_frame = tk.Frame(self.root, bg="#37004A", bd=0)
        self.back_button = tk.Button(
            self.button_frame, text="BACK", font=("Segoe UI", 12, "bold"),
            bg="#767b21", fg="white", width=10, command=self.before_page
        )
        self.next_button = tk.Button(
            self.button_frame, text="NEXT", font=("Segoe UI", 12, "bold"),
            bg="#28a745", fg="white", width=10, command=self.next_page
        )
        self.exit_button = tk.Button(
            self.button_frame, text="EXIT", font=("Segoe UI", 12, "bold"),
            bg="#dc3545", fg="white", width=10, command=self.exit_app
        ) 
        self.back_button.pack(side="left", padx=5)
        self.next_button.pack(side="left", padx=5)
        self.exit_button.pack(side="left", padx=5)

        self.button_window = None
        self.update_background()
        self.root.bind("<Configure>", self.on_resize)
    def update_background(self):
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        if w > 1 and h > 1:
            resized = self.original_image.resize((w, h), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

            self.logo_photo = ImageTk.PhotoImage(self.logo_image)
            self.canvas.create_image(10, 10, image=self.logo_photo, anchor="nw")

            self.rama_photo = ImageTk.PhotoImage(self.rama_image)
            self.canvas.create_image(350, 230, image=self.rama_photo, anchor="nw")
            self.canvas.create_text(400, 400, text="Rama Praditha R.\n2417051039", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            self.reggy_photo = ImageTk.PhotoImage(self.reggy_image)
            self.canvas.create_image(540, 230, image=self.reggy_photo, anchor="nw")
            self.canvas.create_text(600, 400, text="Reggy Desvita Kamal\n2417051016", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            self.karina_photo = ImageTk.PhotoImage(self.karina_image)
            self.canvas.create_image(720, 230, image=self.karina_photo, anchor="nw")
            self.canvas.create_text(770, 400, text="Karina Fitriamalia\n2417051014", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            self.ikbal_photo = ImageTk.PhotoImage(self.ikbal_image)
            self.canvas.create_image(900, 230, image=self.ikbal_photo, anchor="nw")
            self.canvas.create_text(950, 400, text="Ikbal Feri Amanda\n2417051031", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            text = "Our Team!"
            font_style = ("Impact", 44, "bold")
            self.canvas.create_text(w * 0.5, h * 0.15, text=text, font=font_style, fill="white", anchor="center")

            text = "KELOMPOK 6"
            font_style = ("Comic Sans MS", 22, "bold")
            self.canvas.create_text(w * 0.5, h * 0.25, text=text, font=font_style, fill="white", anchor="center")

            self.button_window = self.canvas.create_window(w - 20, 20, window=self.button_frame, anchor="ne")

    def on_resize(self, event):
        self.update_background()

    def next_page(self):
        from third_page import ThirdPage
        self.canvas.destroy()
        self.button_frame.destroy()
        self.root.unbind("<Configure>")
        ThirdPage(self.root)
    
    def before_page(self):
        from welcome_page import WelcomePage
        self.canvas.destroy()
        self.button_frame.destroy()
        self.root.unbind("<Configure>")
        WelcomePage(self.root)

    def exit_app(self):
        self.root.destroy()
