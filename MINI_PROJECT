import tkinter as tk
from PIL import Image, ImageTk, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

class WelcomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome Page")
        self.root.state("zoomed")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.original_image = Image.open("background.png")
        self.bg_photo = None
        self.logo_photo = None

        self.button_frame = tk.Frame(self.root, bg="#37004A", bd=0)
        self.next_button = tk.Button(
            self.button_frame, text="NEXT", font=("Segoe UI", 12, "bold"),
            bg="#28a745", fg="white", width=10, command=self.next_page
        )
        self.exit_button = tk.Button(
            self.button_frame, text="EXIT", font=("Segoe UI", 12, "bold"),
            bg="#dc3545", fg="white", width=10, command=self.exit_app
        )
        self.next_button.pack(side="left", padx=5)
        self.exit_button.pack(side="left", padx=5)

        self.button_window = None
        self.update_background()
        self.root.bind("<Configure>", self.on_resize)
