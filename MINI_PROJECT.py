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

        self.original_image = Image.open("asset/background.png")
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

            logo_image = Image.open("asset/Logo_Unila.png").resize((200, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.canvas.create_image(10, 10, image=self.logo_photo, anchor="nw")

            rama_image = Image.open("asset/rama.png").resize((100,150), Image.LANCZOS)
            self.rama_photo = ImageTk.PhotoImage(rama_image) 
            self.canvas.create_image(350, 230, image=self.rama_photo, anchor="nw")
            self.canvas.create_text(400, 400, text="Rama Praditha R.\n2417051039", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            reggy_image = Image.open("asset/reggy.png").resize((100,150), Image.LANCZOS)
            self.reggy_photo = ImageTk.PhotoImage(reggy_image) 
            self.canvas.create_image(540, 230, image=self.reggy_photo, anchor="nw")
            self.canvas.create_text(600, 400, text="Reggy Desvita Kamal\n2417051016", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            karina_image = Image.open("asset/karina.png").resize((100,150), Image.LANCZOS)
            self.karina_photo = ImageTk.PhotoImage(karina_image) 
            self.canvas.create_image(720, 230, image=self.karina_photo, anchor="nw")
            self.canvas.create_text(770, 400, text="Karina Fitriamalia\n2417051014", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            ikbal_image = Image.open("asset/ikbal.png").resize((100,150), Image.LANCZOS)
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
        ThirdPage(self.root)
    
    def before_page(self):
        self.canvas.pack_forget()
        self.button_frame.pack_forget()
        self.root.unbind("<Configure>")
        WelcomePage(self.root)

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

            logo_image = Image.open("asset/Logo_Unila.png").resize((200, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.canvas.create_image(10, 10, image=self.logo_photo, anchor="nw")

            rama_image = Image.open("asset/rama.png").resize((100,150), Image.LANCZOS)
            self.rama_photo = ImageTk.PhotoImage(rama_image) 
            self.canvas.create_image(350, 230, image=self.rama_photo, anchor="nw")
            self.canvas.create_text(400, 400, text="Rama Praditha R.\n2417051039", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            reggy_image = Image.open("asset/reggy.png").resize((100,150), Image.LANCZOS)
            self.reggy_photo = ImageTk.PhotoImage(reggy_image) 
            self.canvas.create_image(540, 230, image=self.reggy_photo, anchor="nw")
            self.canvas.create_text(600, 400, text="Reggy Desvita Kamal\n2417051016", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            karina_image = Image.open("asset/karina.png").resize((100,150), Image.LANCZOS)
            self.karina_photo = ImageTk.PhotoImage(karina_image) 
            self.canvas.create_image(720, 230, image=self.karina_photo, anchor="nw")
            self.canvas.create_text(770, 400, text="Karina Fitriamalia\n2417051014", font=("Segoe UI", 10, "bold"), fill="white", anchor="n")

            ikbal_image = Image.open("asset/ikbal.png").resize((100,150), Image.LANCZOS)
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
        ThirdPage(self.root)
    
    def before_page(self):
        self.canvas.pack_forget()
        self.button_frame.pack_forget()
        self.root.unbind("<Configure>")
        WelcomePage(self.root)

    def exit_app(self):
        self.root.destroy()()
        
class ThirdPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Third Page")
        self.root.state("zoomed")
        self.destroyed = False
        self.resize_job = None

        self.header_height = 120
        self.header_frame = tk.Frame(self.root, bg="black", height=self.header_height)
        self.header_frame.pack(side="top", fill="x")

        division_frame = tk.Frame(self.header_frame, bg="black")
        division_frame.place(relx=0.5, y=10, anchor="n")
        division_label = tk.Label(division_frame, text="Division", fg="white", bg="black", font=("Segoe UI", 14, "bold"))
        division_label.pack(side="left", padx=(0, 10))
        self.division_var = tk.StringVar()
        self.division_dropdown = ttk.Combobox(division_frame, textvariable=self.division_var, values=["Putra", "Putri"], state="readonly", width=20, font=("Segoe UI", 11))
        self.division_dropdown.set("Putra")
        self.division_dropdown.pack(side="left")

        ao_label = tk.Label(self.header_frame, text="Ao", fg="red", bg="black", font=("Segoe UI", 16, "bold"))
        ao_label.place(relx=0.02, rely=0.3)
        self.ao_entry = tk.Entry(self.header_frame, width=20, font=("Segoe UI", 12))
        self.ao_entry.place(relx=0.08, rely=0.35)

        aka_label = tk.Label(self.header_frame, text="Aka", fg="blue", bg="black", font=("Segoe UI", 16, "bold"))
        aka_label.place(relx=0.5, rely=0.3)
        self.aka_entry = tk.Entry(self.header_frame, width=20, font=("Segoe UI", 12))
        self.aka_entry.place(relx=0.56, rely=0.35)

        self.judges_frame = tk.Frame(self.header_frame, bg="black")
        self.judges_frame.place(relx=0.5, rely=0.6, anchor="n")
        self.judges_buttons = []
        self.judges_count = 0
        self.reset_judges_selection()

        self.names = []
        self.ao_dropdown_var = tk.StringVar()
        self.aka_dropdown_var = tk.StringVar()
        self.ao_dropdown = ttk.Combobox(textvariable=self.ao_dropdown_var, font=("Segoe UI", 14, "bold"), state="readonly")
        self.aka_dropdown = ttk.Combobox(textvariable=self.aka_dropdown_var, font=("Segoe UI", 14, "bold"), state="readonly")
        self.ao_dropdown.place(relx=0.8, rely=0.12, anchor="center")
        self.aka_dropdown.place(relx=0.12, rely=0.12, anchor="center")

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        try:
            self.original_image = Image.open("asset/Bendera.png")
        except FileNotFoundError:
            self.original_image = Image.new("RGB", (800, 600), "gray")
        self.bg_photo = None

        self.score_kanan = 0
        self.score_kiri = 0
        self.seconds_elapsed_kiri = 0
        self.is_running_kiri = False
        self.seconds_elapsed_kanan = 0
        self.is_running_kanan = False
        self.timer_visible = True
        self.status_kiri = ""
        self.status_kanan = ""
        self.hasil_pertandingan = []

        self.frame_kanan = tk.Frame(self.root, bg="#06075C")
        self.frame_kiri = tk.Frame(self.root, bg="#FF0000")
        self.setup_score_section_kiri(self.frame_kiri)
        self.setup_score_section_kanan(self.frame_kanan)
        self.frame_kiri.place(relx=0.12, rely=0.5, anchor="center")
        self.frame_kanan.place(relx=0.65, rely=0.5, anchor="center")

   self.button_frame = tk.Frame(self.root, bg="#06075C", bd=0)
        self.back_button = tk.Button(self.button_frame, text="BACK", font=("Segoe UI", 12, "bold"), bg="#767b21", fg="white", width=10, command=self.before_page)
        self.exit_button = tk.Button(self.button_frame, text="EXIT", font=("Segoe UI", 12, "bold"), bg="#dc3545", fg="white", width=10, command=self.exit_app)
        self.back_button.pack(side="left", padx=5)
        self.exit_button.pack(side="left", padx=5)

        self.button_window = None
        self.update_background()
        self.root.bind("<Configure>", self.on_resize)

    def set_judges(self, count):
        self.judges_count = count
        for btn in self.judges_buttons:
            btn.destroy()
        self.judges_buttons.clear()
        selected_btn = tk.Button(self.judges_frame, text=f"{count} Judge{'s' if count > 1 else ''}", font=("Segoe UI", 12, "bold"), bg="blue", fg="white", command=self.reset_judges_selection)
        selected_btn.pack(side="left", padx=5)
        self.judges_buttons.append(selected_btn)

    def reset_judges_selection(self):
        for btn in self.judges_buttons:
            btn.destroy()
        self.judges_buttons.clear()
        for i in range(1, 6):
            btn = tk.Button(self.judges_frame, text=str(i), width=3, font=("Segoe UI", 12, "bold"), bg="gray", fg="white", command=lambda x=i: self.set_judges(x))
            btn.pack(side="left", padx=2)
            self.judges_buttons.append(btn)

    def setup_score_section_kiri(self, frame):
        self.label_score_kiri = tk.Label(frame, text="0", font=("Montserrat", 50, "bold"), fg="white", bg="#FF0000")
        self.label_score_kiri.pack(pady=30)
        button_frame = tk.Frame(frame, bg="#FF0000")
        button_frame.pack(pady=2)
        tk.Button(button_frame, text="+1", font=("Montserrat", 18, "bold"), bg="green", fg="white", width=4, height=2, command=self.increase_score_kiri).pack(side="left", padx=5)
        tk.Button(button_frame, text="-1", font=("Montserrat", 18, "bold"), bg="blue", fg="white", width=4, height=2, command=self.decrease_score_kiri).pack(side="left", padx=5)

    def setup_score_section_kanan(self, frame):
        self.label_score_kanan = tk.Label(frame, text="0", font=("Montserrat", 50, "bold"), fg="white", bg="#06075C")
        self.label_score_kanan.pack(pady=30)
        button_frame = tk.Frame(frame, bg="#06075C")
        button_frame.pack(pady=2)
        tk.Button(button_frame, text="+1", font=("Montserrat", 18, "bold"), bg="green", fg="white", width=4, height=2, command=self.increase_score_kanan).pack(side="left", padx=5)
        tk.Button(button_frame, text="-1", font=("Montserrat", 18, "bold"), bg="blue", fg="white", width=4, height=2, command=self.decrease_score_kanan).pack(side="left", padx=5)

    def setup_function_buttons(self):
        self.func_button_frame = tk.Frame(self.root, bg="#867E7E")  
        self.func_button_frame.pack(side="bottom", fill="x")
        buttons = [
        ("Show/Hide\nStopwatch", "gray", self.toggle_timer_visibility),
        ("Shikkaku", "red", self.shikkaku_kiri),
        ("Kikken", "red", self.kikken_kiri),
        ("Shikkaku", "blue", self.shikkaku_kanan),
        ("Kikken", "blue", self.kikken_kanan),
        ("Done", "orange", self.done),
        ("Reset", "red", self.reset_scores),
        ]
        for text, color, command in buttons:
            btn = tk.Button(self.func_button_frame, text=text, font=("Segoe UI", 10, "bold"), bg=color, fg="white", command=command)
            btn.pack(side="left", fill="x", expand=True, padx=1, pady=3)


    def setup_timer_frames(self):
        self.timer_frame_kiri = tk.Frame(self.root, bg="#FF0000")
        start_btn = tk.Button(self.timer_frame_kiri, text="Start", font=("Segoe UI", 20, "bold"), bg="green", fg="white", command=self.start_both_timers)
        start_btn.pack(side="left", padx=10)
        self.timer_label_kiri = tk.Label(self.timer_frame_kiri, text="00:00", font=("Montserrat", 40, "bold"), fg="white", bg="#FF0000")
        self.timer_label_kiri.pack(side="left", padx=10)
        self.timer_frame_kiri.place(relx=0.3, rely=0.8, anchor="center")

        self.timer_frame_kanan = tk.Frame(self.root, bg="#06075C")
        self.timer_label_kanan = tk.Label(self.timer_frame_kanan, text="00:00", font=("Montserrat", 40, "bold"), fg="white", bg="#06075C")
        self.timer_label_kanan.pack(side="left", padx=10)
        self.timer_frame_kanan.place(relx=0.8, rely=0.8, anchor="center")
        
def done(self):
        self.is_running_kiri = False
        self.is_running_kanan = False
        ao_name = self.ao_entry.get().strip()
        aka_name = self.aka_entry.get().strip()
        division = self.division_var.get()
        timer_kiri = f"{self.seconds_elapsed_kiri // 60:02d}:{self.seconds_elapsed_kiri % 60:02d}"
        timer_kanan = f"{self.seconds_elapsed_kanan // 60:02d}:{self.seconds_elapsed_kanan % 60:02d}"

        if ao_name and ao_name not in self.names:
            self.names.append(ao_name)
        if aka_name and aka_name not in self.names:
            self.names.append(aka_name)
        self.ao_dropdown['values'] = self.names
        self.aka_dropdown['values'] = self.names
        self.ao_dropdown_var.set(ao_name)
        self.aka_dropdown_var.set(aka_name)

        status_kiri = "Normal"
        status_kanan = "Normal"
        if self.status_kiri == "Shikkaku":
            status_kiri = "Diskualifikasi"
            status_kanan = "Menang"
        elif self.status_kiri == "Kikken":
            status_kiri = "Menyerah"
            status_kanan = "Menang"
        elif self.status_kanan == "Shikkaku":
            status_kanan = "Diskualifikasi"
            status_kiri = "Menang"
        elif self.status_kanan == "Kikken":
            status_kanan = "Menyerah"
            status_kiri = "Menang"
        elif self.score_kiri > self.score_kanan:
            status_kiri = "Menang"
            status_kanan = "Kalah"
        elif self.score_kiri < self.score_kanan:
            status_kiri = "Kalah"
            status_kanan = "Menang"
        else:
            status_kiri = status_kanan = "Seri"

        hasil = (
            f"Division: {division} | "
            f"{ao_name} ({status_kiri}, {timer_kiri}) vs "
            f"{aka_name} ({status_kanan}, {timer_kanan})"
        )
        self.hasil_pertandingan.append(hasil)
        with open("hasil_pertandingan.txt", "a", encoding="utf-8") as file:
            file.write(hasil + "\n")

    def update_background(self):
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        if w > 1 and h > 1:
            resized = self.original_image.resize((w, h), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(resized)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
            if self.button_frame:
                self.button_window = self.canvas.create_window(w - 20, 20, window=self.button_frame, anchor="ne")

    def on_resize(self, event):
        if self.resize_job:
            self.root.after_cancel(self.resize_job)
        self.resize_job = self.root.after(100, self.update_background)

    def before_page(self):
        self.is_running_kiri = False
        self.is_running_kanan = False
        self.destroyed = True
        self.root.unbind("<Configure>")
        try:
            self.header_frame.destroy()
            self.canvas.destroy()
            self.button_frame.destroy()
            self.frame_kanan.destroy()
            self.frame_kiri.destroy()
            self.timer_frame_kiri.destroy()
            self.timer_frame_kanan.destroy()
            self.func_button_frame.destroy()
        except Exception:
            pass
        SecondPage(self.root)

    def exit_app(self):
        self.is_running_kiri = False
        self.is_running_kanan = False
        self.destroyed = True
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomePage(root)
    root.mainloop()
