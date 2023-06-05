import tkinter as tk
import webbrowser

class BotonCss(tk.Label):
    def __init__(self, parent, url, text="Haga clic aquí para abrir", **kwargs):
        super().__init__(parent, text=text, fg="#0ba6ab", cursor="hand2", **kwargs)
        self.url = url
        self.configure(bg="#c7e5f7", padx=10, pady=5, font=("Lilita One", 14))
        #self.configure(bg="#c7e5f7",relief="solid", borderwidth=1, padx=10, pady=5, font=("Lilita One", 14))
        self.bind("<Button-1>", self.open_url)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def open_url(self, event):
        webbrowser.open_new(self.url)

    def on_enter(self, event):
        self.configure(bg="#0ba6ab")
        self.configure(fg="white")
        self.configure(font=("Lilita One", 15))
        

    def on_leave(self, event):
        self.configure(bg="#c7e5f7")
        self.configure(fg="#0ba6ab")
        self.configure(font=("Lilita One", 14))
        
