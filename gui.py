import tkinter as tk
from tkinter import filedialog, messagebox
from encoder import encode_image
from decoder import decode_image

class SteganographyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Steganography Tool")
        self.root.geometry("400x300")

        self.image_path = ""

        tk.Label(self.root, text="Steganography Tool", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Upload Image", command=self.upload_image).pack(pady=5)

        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(pady=5)
        self.message_entry.insert(0, "Enter message")

        tk.Button(self.root, text="Encode", command=self.encode).pack(pady=5)
        tk.Button(self.root, text="Decode", command=self.decode).pack(pady=5)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.bmp")])
        messagebox.showinfo("Selected", self.image_path)

    def encode(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected")
            return

        message = self.message_entry.get()
        output_path = filedialog.asksaveasfilename(defaultextension=".png")

        encode_image(self.image_path, message, output_path)
        messagebox.showinfo("Success", "Message encoded successfully!")

    def decode(self):
        if not self.image_path:
            messagebox.showerror("Error", "No image selected")
            return

        message = decode_image(self.image_path)
        messagebox.showinfo("Hidden Message", message)

    def run(self):
        self.root.mainloop()
