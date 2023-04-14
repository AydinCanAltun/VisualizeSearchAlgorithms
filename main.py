from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt
import time
from CTkMessagebox import CTkMessagebox
import customtkinter as tk
import os

os.environ["PATH"] += os.pathsep + "C:\Program Files\Graphviz\\bin\\"

tk.set_appearance_mode("dark");
tk.set_default_color_theme("green");

root=tk.CTk()
root.geometry("500x700")
root.title("Visualize Search Algorithms")

g = AlgorithmHelper('matrix.txt')

def show_path(title, path):
    if path != None:
        g.visualizer.show_path(title=title, draw_curved_edges=False, path=path)
    else:
        CTkMessagebox(title="Sonuç Bulunamadı", message="Yol bulunamadı!",
                  icon="warning")
    g.visualizer.close_plot()

def bfs():
    path = g.bfs(3, 5)
    title = "BFS (3, 5)"
    show_path(title, path)
def dfs():
    path = g.dfs(3, 5)
    title = "DFS (3, 5)"
    show_path(title, path)
def ucs():
    path = g.ucs(3, 5)
    title = "UCS (3, 5)"
    show_path(title, path)
def dls():
    path = g.dls(deep_limit=4, start=3, target=5)
    title = "DLS (3, 5) Deep Limit = 4"
    show_path(title, path)
def iddfs():
    path = g.iddfs(0, 10, 1)
    title = "IDDFS (0, 10), Maximum Depth Limit = 1"
    show_path(title, path)
def bidirectional():
    path = g.bidirectional_search(0, 10)
    title = "Bi Directional Search (0, 10)"
    show_path(title, path)
def showGraf():
    g.visualizer.visualize_graph(title="Graph", draw_curved_edges=False)

frame = tk.CTkFrame(master=root,corner_radius=10)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = tk.CTkLabel(master=frame, text="Algoritma Seçiniz", font=("Roboto",32))
label.pack(pady=32,padx=10)

bfsButton = tk.CTkButton(master=frame, text="bfs", command=bfs)
bfsButton.pack(pady=12,padx=10)

dfsButton = tk.CTkButton(master=frame, text="dfs", command=dfs)
dfsButton.pack(pady=12,padx=10)

ucsButton = tk.CTkButton(master=frame, text="ucs", command=ucs)
ucsButton.pack(pady=12,padx=10)

dlsButton = tk.CTkButton(master=frame, text="dls", command=dls)
dlsButton.pack(pady=12,padx=10)

iddfsButton = tk.CTkButton(master=frame, text="iddfs", command=iddfs)
iddfsButton.pack(pady=12,padx=10)

biDirectionalButton = tk.CTkButton(master=frame, text="bidirectional search", command=bidirectional)
biDirectionalButton.pack(pady=12,padx=10)

showGraphButton = tk.CTkButton(master=frame, text="Grafı Göster", command=showGraf)
showGraphButton.pack(pady=12,padx=10)

labelWriter1 = tk.CTkLabel(master=frame, text="Aydın Can ALTUN - 180202117", font=("Roboto",14), wraplength=300)
labelWriter1.pack(pady=0,padx=10)

labelWriter2 = tk.CTkLabel(master=frame, text="Ege ÖZEREN - 180202047", font=("Roboto",14), wraplength=300)
labelWriter2.pack(pady=0,padx=10)

labelWriter3 = tk.CTkLabel(master=frame, text="Emre YELBEY - 180202043", font=("Roboto",14), wraplength=300)
labelWriter3.pack(pady=0,padx=10)

labelWriter4 = tk.CTkLabel(master=frame, text="Osman ŞİMŞEK - 180202048", font=("Roboto",14), wraplength=300)
labelWriter4.pack(pady=0,padx=10)

labelWriter5 = tk.CTkLabel(master=frame, text="Yener Emin ELİBOL - 180202054", font=("Roboto",14), wraplength=300)
labelWriter5.pack(pady=0,padx=10)

root.mainloop()
