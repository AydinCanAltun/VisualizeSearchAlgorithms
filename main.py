from graph import AlgorithmHelper
import networkx as nx
import matplotlib.pyplot as plt
import time
import customtkinter

customtkinter.set_appearance_mode("dark");
customtkinter.set_default_color_theme("green");

root=customtkinter.CTk()
root.geometry("500x700")

g = AlgorithmHelper('matris.txt')
def bfs():print(f"bfs result: {g.bfs(3, 5)}")
def dfs():print(f"dfs result: {g.dfs(0, 1)}")
def ucs():print(f"ucs result : {g.ucs(3, 5)}")
def dls():print(f"dls result: {g.dls(deep_limit=4, start=3,target=5)}")
def iddfs():print(f"iddfs")
def bidirectional():print(f"bidirectional")
def showGraf():print(f"showGraf")

frame = customtkinter.CTkFrame(master=root,corner_radius=10)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame, text="Algoritma Seçiniz", font=("Roboto",32))
label.pack(pady=32,padx=10)

button1 = customtkinter.CTkButton(master=frame, text="bfs", command=bfs)
button1.pack(pady=12,padx=10)

button2 = customtkinter.CTkButton(master=frame, text="dfs", command=dfs)
button2.pack(pady=12,padx=10)

button3 = customtkinter.CTkButton(master=frame, text="ucs", command=ucs)
button3.pack(pady=12,padx=10)

button4 = customtkinter.CTkButton(master=frame, text="dls", command=dls)
button4.pack(pady=12,padx=10)

button5 = customtkinter.CTkButton(master=frame, text="iddfs", command=iddfs)
button5.pack(pady=12,padx=10)

button6 = customtkinter.CTkButton(master=frame, text="bidirectional search", command=bidirectional)
button6.pack(pady=12,padx=10)

button7 = customtkinter.CTkButton(master=frame, text="Grafı Göster", command=showGraf)
button7.pack(pady=12,padx=10)

labelWriter1 = customtkinter.CTkLabel(master=frame, text="Aydıncan ALTUN - 180202117", font=("Roboto",14), wraplength=300)
labelWriter1.pack(pady=0,padx=10)

labelWriter2 = customtkinter.CTkLabel(master=frame, text="Ege ÖZEREN - 180202047", font=("Roboto",14), wraplength=300)
labelWriter2.pack(pady=0,padx=10)

labelWriter3 = customtkinter.CTkLabel(master=frame, text="Emre YELBEY - 180202043", font=("Roboto",14), wraplength=300)
labelWriter3.pack(pady=0,padx=10)

labelWriter4 = customtkinter.CTkLabel(master=frame, text="Osman ŞİMŞEK - 180202048", font=("Roboto",14), wraplength=300)
labelWriter4.pack(pady=0,padx=10)

labelWriter5 = customtkinter.CTkLabel(master=frame, text="Yener Emin ELİBOL - 180202054", font=("Roboto",14), wraplength=300)
labelWriter5.pack(pady=0,padx=10)

root.mainloop()


# g = AlgorithmHelper('matris.txt')
# print(f"bfs result: {g.bfs(3, 5)}")
#print(f"dfs result: {g.dfs(0, 1)}")
#print(f"ucs result : {g.ucs(3, 5)}")
# print(f"dls result: {g.dls(deep_limit=4, start=3,target=5)}")
