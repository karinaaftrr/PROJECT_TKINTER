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

            text = "WELCOME TO OUR PROJECT" 
            font_style = ("Georgia", 44, "bold")
            self.canvas.create_text(w * 0.5, h * 0.45, text=text, font=font_style, fill="white", anchor="center")

            self.button_window = self.canvas.create_window(w - 20, 20, window=self.button_frame, anchor="ne")

    def on_resize(self, event):
        self.update_background()

    def next_page(self):
        from second_page import SecondPage
        self.canvas.destroy()
        self.button_frame.destroy()
        self.root.unbind("<Configure>")
        SecondPage(self.root)

    def exit_app(self):
        self.root.destroy()
