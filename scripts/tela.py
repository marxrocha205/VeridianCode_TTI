import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import shutil
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Imagem")

        # Frame principal com padding
        self.main_frame = ttk.Frame(self, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Campo de texto
        self.label_text = ttk.Label(self.main_frame, text="Solicitação:")
        self.label_text.pack(anchor="w", pady=5)

        self.text_field = ttk.Entry(self.main_frame, width=50)
        self.text_field.pack(pady=5)

        # Botão para enviar
        self.send_button = ttk.Button(self.main_frame, text="Enviar", command=self.send_data)
        self.send_button.pack(pady=20)

        # Label para exibir a imagem carregada
        self.image_label = ttk.Label(self.main_frame)
        self.image_label.pack(pady=5)

   
    def send_data(self):
        text_data = self.text_field.get()

        if text_data:
            # Mostrar a imagem carregada
            img = Image.open(r"C:\\Users\\CauaS\\programacao\\work\\tensorFlow\\imgs\\class1\\Borboleta.png")
            img = img.resize((200, 200), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
            
        else:
            messagebox.showwarning("Por favor, preencha o campo de solicitação")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
