import tkinter as tk
import server

def showClient(content):
    # add the title
    titulo = tk.Label(content, text="Clientes");
    titulo.grid(row=0)
    # add the table content
    server.cur.execute('select * from CLIENTE')
    i = 1
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            b = tk.Label(content, text=result[j], padx="50", pady="5", borderwidth=2, relief="ridge")
            b.grid(row = i, column=j, sticky="nsew")
        i = i + 1