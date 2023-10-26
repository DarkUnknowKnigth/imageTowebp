from ConvertWebp import *
import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
import threading
class ImageToWeb:
  root = ''
  paths = []
  progressLabel = ''
  def __init__(self, root):
    self.root = root
    self.root.geometry("500x250")
    self.root.title("Conversión de imágenes")
    self.paths = []
    imgPath = "./background.png"
    bgImg = PhotoImage(file=imgPath)
    canvas = tk.Canvas(root, width=500, height=200)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=bgImg)
    canvas.image = bgImg  # Mantener una referencia para evitar la eliminación


    # mostrar progreso
    self.progressLabel = tk.Label(root, text="Progreso: Esperando inicio de proceso")
    self.progressLabel.pack(pady=10)
    # seleccionar imagenes
    selectButton = tk.Button(root, text="Seleccionar imagenes", command=self.selectImages)
    selectButton.pack(pady=10)
    canvas.create_window(250, 50, window=selectButton)
    # convertir
    selectButton = tk.Button(root, text="Convertir a WebP", command=self.convert)
    selectButton.pack(pady=10)
    canvas.create_window(250, 100, window=selectButton)
  
  def selectImages(self):
    selectedPaths = filedialog.askopenfilenames(title="Selecciona imágenes", filetypes=(("Archivos de imagen","*.jpg *.png *.jpeg *.gif"), ("Todos los archivos", "*.*")))
    if selectedPaths:
      self.paths = selectedPaths
      messagebox.showinfo("Seleccionó ", f"{len(self.paths)} imágenes")
    else:
      messagebox.showwarning("Sin imágenes", "No ha seleccionado ninguna imagen el programa no puede continuar")
  
  def convert(self):
    if not self.paths:
      messagebox.showwarning("Sin imágenes", "No hay nada que convertir")
      return
    # hilo de conversion 
    def conversionThread():
      total = len(self.paths)
      for i, path in enumerate(self.paths, start=1):
        converter = ConvertWebp(path)
        converter.convert()
        self.progressLabel.config(text=f"Progreso {i} de {total} imágenes")
    conversionTrd = threading.Thread(target=conversionThread)
    conversionTrd.start()
    messagebox.showinfo("Conversion Iniciada", "Las imágenes serán convertidas a webp")
if __name__ == "__main__":
  root = tk.Tk()
  app = ImageToWeb(root)
  root.mainloop()