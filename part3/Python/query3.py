import tkinter as tk
from tkinter import ttk
import server

# remove all the widgets from a frame
def clearContent(content):
    for widget in content.winfo_children():
        widget.destroy()
    col_count = content.grid_size()[0]
    for i in range(col_count):
        tk.Grid.columnconfigure(content, i, weight=0)

# show the query 1
def showQuery3(content):
    # clear the old content
    clearContent(content)

    # add the title
    tk.Label(content, text="Consulta 3", font='Helvetica 14').grid(row=0, stick='nsew')

    # add explanation
    tk.Label(content, text='Para cada tipo de funcionário, calcular a média salarial e a quantidade de empregados. Ordenar decrescentemente pela média salarial.', font='Helvetica 12').grid(row=1, column=0, sticky="nsew")

    # add 
    tk.Label(content, text="Cargo", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=0, sticky="nsew")
    tk.Label(content, text="Salario_Medio", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=1, sticky="nsew")
    tk.Label(content, text="Num_Empregados", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=2, sticky="nsew")

    # add the table content
    server.cur.execute(' \
        SELECT CARGO, AVG(SALARIO) AS SALARIO_MEDIO, COUNT(CPF) AS NUM_EMPREGADOS \
            FROM FUNCIONARIO \
            GROUP BY CARGO \
            ORDER BY AVG(SALARIO) DESC \
        ')

    i = 3
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            tk.Label(content, text=result[j], padx=15, pady=5, borderwidth=2, relief="ridge").grid(row=i, column=j, sticky="nsew")

