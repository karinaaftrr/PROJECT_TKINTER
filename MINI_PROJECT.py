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

    def update_background(self):
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        if w > 1 and h > 1:
            resized = self.original_image.resize((w, h), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

            logo_image = Image.open("Logo_Unila.png").resize((200, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.canvas.create_image(10, 10, image=self.logo_photo, anchor="nw")

            text = " ".join("WELCOME TO OUR PROJECT")
            font_style = ("Georgia", 44, "bold")
            self.canvas.create_text(w * 0.5, h * 0.45, text=text, font=font_style, fill="white", anchor="center")

            self.button_window = self.canvas.create_window(w - 20, 20, window=self.button_frame, anchor="ne")

    def on_resize(self, event):
        self.update_background()

    def next_page(self):
        self.canvas.pack_forget()
        self.button_frame.pack_forget()
        self.root.unbind("<Configure>")
        SecondPage(self.root)

    def exit_app(self):
        self.root.destroy()

class SecondPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Second Page")

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.original_image = Image.open("background.png")
        self.bg_photo = None
        self.logo_photo = None

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

            logo_image = Image.open("Logo_Unila.png").resize((200, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.canvas.create_image(10, 10, image=self.logo_photo, anchor="nw")

            rama_image = Image.open("rama praditha.jpg").resize((100,150), Image.LANCZOS)
            self.rama_photo = ImageTk.PhotoImage(rama_image) 
            self.canvas.create_image(350, 230, image=self.rama_photo, anchor="nw")
            self.canvas.create_text(400, 400, text="Rama Praditha R.\n2417051039", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            reggy_image = Image.open("reggy2.jpg").resize((100,150), Image.LANCZOS)
            self.reggy_photo = ImageTk.PhotoImage(reggy_image) 
            self.canvas.create_image(540, 230, image=self.reggy_photo, anchor="nw")
            self.canvas.create_text(600, 400, text="Reggy Desvita Kamal\n2417051016", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            karina_image = Image.open("karina3.jpg").resize((100,150), Image.LANCZOS)
            self.karina_photo = ImageTk.PhotoImage(karina_image) 
            self.canvas.create_image(720, 230, image=self.karina_photo, anchor="nw")
            self.canvas.create_text(770, 400, text="Karina Fitriamalia\n2417051014", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            ikbal_image = Image.open("ikbal.jpg").resize((100,150), Image.LANCZOS)
            self.ikbal_photo = ImageTk.PhotoImage(ikbal_image) 
            self.canvas.create_image(900, 230, image=self.ikbal_photo, anchor="nw")
            self.canvas.create_text(950, 400, text="Ikbal Feri Amanda\n2417051031", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            text = " ".join("Our Team!")
            font_style = ("Impact", 44, "bold")
            self.canvas.create_text(w * 0.5, h * 0.15, text=text, font=font_style, fill="white", anchor="center")

            text = "KELOMPOK 6"
            font_style = ("Comic Sans MS", 22, "bold")
            self.canvas.create_text(w * 0.5, h * 0.25, text=text, font=font_style, fill="white", anchor="center")

            self.button_window = self.canvas.create_window(w - 20, 20, window=self.button_frame, anchor="ne")
    def on_resize(self, event):
        self.update_background()

    def next_page(self):
        self.canvas.pack_forget()
        self.button_frame.pack_forget()
        self.root.unbind("<Configure>")
        print("Next page belum dibuat.")
    
    def before_page(self):
        self.canvas.pack_forget()
        self.button_frame.pack_forget()
        self.root.unbind("<Configure>")
        WelcomePage(self.root)

    def exit_app(self):
        self.root.destroy()
        
class ThirdPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Third Page")
        self.root.state("zoomed")

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.original_image = Image.open("Bendera.png")
        self.bg_photo = None
        self.logo_photo = None

        self.frame_kanan = tk.Frame(self.root, bg="#111")
        self.frame_kanan.place(relx=0.6, rely=0.35, anchor="w")

        self.score_kanan = 0
        self.setup_score_section_kanan(self.frame_kanan)

        self.frame_kiri = tk.Frame(self.root, bg="#111")
        self.frame_kiri.place(relx=0.15, rely=0.35, anchor="e")

        self.score_kiri = 0
        self.setup_score_section_kiri(self.frame_kiri)

        self.button_frame = tk.Frame(self.root, bg="#06075C", bd=0)

        self.back_button = tk.Button(
            self.button_frame, text="BACK", font=("Segoe UI", 12, "bold"),
            bg="#767b21", fg="white", width=10, command=self.before_page
        )
        self.exit_button = tk.Button(
            self.button_frame, text="EXIT", font=("Segoe UI", 12, "bold"),
            bg="#dc3545", fg="white", width=10, command=self.exit_app
        )
        self.back_button.pack(side="left", padx=5)
        self.exit_button.pack(side="left", padx=5)

        self.button_window = None
        self.update_background()
        self.root.bind("<Configure>", self.on_resize)

    def setup_score_section_kanan(self, frame):
        self.label_score_kanan = tk.Label(frame, text="0", font=("Helvetica", 20), fg="white", bg="#06075C")
        self.label_score_kanan.pack(pady=10)

        button_frame = tk.Frame(frame, bg="#06075C")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="+1", font=("Helvetica", 18, "bold"),
                  bg="green", fg="white", width=4, height=2,
                  command=self.increase_score_kanan).pack(side="left", padx=5)
        tk.Button(button_frame, text="-1", font=("Helvetica", 18, "bold"),
                  bg="blue", fg="white", width=4, height=2,
                  command=self.decrease_score_kanan).pack(side="left", padx=5)
    
    def setup_score_section_kiri(self, frame):
        self.label_score_kiri = tk.Label(frame, text="0", font=("Helvetica", 20), fg="white", bg="#FF0000")
        self.label_score_kiri.pack(pady=10)

        button_frame = tk.Frame(frame, bg="#FF0000")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="+1", font=("Helvetica", 18, "bold"),
                  bg="green", fg="white", width=4, height=2,
                  command=self.increase_score_kiri).pack(side="left", padx=5)
        tk.Button(button_frame, text="-1", font=("Helvetica", 18, "bold"),
                  bg="blue", fg="white", width=4, height=2,
                  command=self.decrease_score_kiri).pack(side="left", padx=5)
    def increase_score_kanan(self):
        self.score_kanan += 1
        self.label_score_kanan.config(text=str(self.score_kanan))

    def decrease_score_kanan(self):
        self.score_kanan = max(0, self.score_kanan - 1)
        self.label_score_kanan.config(text=str(self.score_kanan))

    def increase_score_kiri(self):
        self.score_kiri += 1
        self.label_score_kiri.config(text=str(self.score_kiri))

    def decrease_score_kiri(self):
        self.score_kiri = max(0, self.score_kiri - 1)
        self.label_score_kiri.config(text=str(self.score_kiri))
    def update_background(self):
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        if w > 1 and h > 1:
            resized = self.original_image.resize((w, h), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
            self.button_window = self.canvas.create_window(w - 20, 20, window=self.button_frame, anchor="ne")

    def on_resize(self, event):
        self.update_background()

    def before_page(self):
        self.canvas.pack_forget()
        self.button_frame.pack_forget()
        self.frame_kanan.destroy()
        self.frame_kiri.destroy()
        self.root.unbind("<Configure>")
        SecondPage(self.root) 

    def exit_app(self):
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomePage(root)
    root.mainloop()
