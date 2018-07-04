import tkinter as tk
from pathlib import Path

path = Path(__file__).parent/"img"

root = tk.Tk()
root.iconbitmap(path/"icono.ico")

about = tk.Toplevel(root)
about.title("Prueba")
about.iconbitmap(path/"icono.png")

root.mainloop()
