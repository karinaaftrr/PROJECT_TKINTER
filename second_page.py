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
