import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

FORTNITE_EXE_NAME = "FortniteClient-Win64-Shipping.exe"

def select_fortnite_path():
    folder = filedialog.askdirectory(title="בחר תיקיית Fortnite")
    if not folder:
        return
    exe_path = os.path.join(folder, "FortniteGame", "Binaries", "Win64", FORTNITE_EXE_NAME)
    if not os.path.exists(exe_path):
        messagebox.showerror("שגיאה", "לא נמצא Fortnite בתיקייה")
        return
    path_var.set(exe_path)

def launch_game():
    exe_path = path_var.get()
    if not exe_path:
        messagebox.showerror("שגיאה", "לא נבחר נתיב")
        return
    try:
        subprocess.Popen([exe_path, "-log"])
        messagebox.showinfo("Launcher", "המשחק הופעל")
    except Exception as e:
        messagebox.showerror("שגיאה", str(e))

root = tk.Tk()
root.title("Reload Launcher")
root.geometry("450x200")
path_var = tk.StringVar()

tk.Label(root, text="נתיב Fortnite:").pack(pady=5)
tk.Entry(root, textvariable=path_var, width=50).pack(pady=5)
tk.Button(root, text="בחר תיקייה", command=select_fortnite_path).pack(pady=5)
tk.Button(root, text="Launch", command=launch_game).pack(pady=15)
root.mainloop()
