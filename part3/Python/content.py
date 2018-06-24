import tkinter as tk
import server

# remove all the widgets from a frame
def clearContent(content):
    for widget in content.winfo_children():
        widget.destroy()

def showClient(content):
    # clear the old content
    clearContent(content)

    # add the title
    titulo = tk.Label(content, text="Lista de Clientes", font='Helvetica 14');
    titulo.grid(row=0, stick='nsew', columnspan=100)

    # add the table content
    server.cur.execute('select * from CLIENTE')
    i = 1
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            b = tk.Label(content, text=result[j], padx="50", pady="5", borderwidth=2, relief="ridge")
            b.grid(row=i, column=j, sticky="nsew")
        i = i + 1