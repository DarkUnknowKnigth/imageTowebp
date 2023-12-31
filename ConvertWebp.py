from PIL import Image
import os
import subprocess
import platform
class ConvertWebp:
  inputhPath = ''
  outputhBase = './converted/webp'
  outputPath = ''
  """
    Clase para convertir imágenes a formato WebP.

    :param inputPath: Ruta de la imagen de entrada.
  """
  def __init__(self, inputPath: str):
    self.inputhPath = inputPath
  def convert(self):
    """
      Convierte la imagen de entrada a formato WebP con el mismo nombre de archivo.
    """
    if not os.path.exists(self.outputhBase):
      os.makedirs(self.outputhBase)
    try:
      with Image.open(self.inputhPath) as img:
        filename, ext = os.path.splitext(os.path.basename(self.inputhPath))
        self.outputPath = self.outputhBase+'/'+filename+".webp"
        img.save(self.outputPath, 'webp')
        if platform.system() == "Windows":
          subprocess.Popen(['explorer', os.path.abspath(self.outputPath)], shell=True)
        else:
          subprocess.Popen(['xdg-open', os.path.abspath(self.outputPath)])
    except Exception as e:
      print(f"Error al convertir la imagen: {str(e)}")