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
def showQuery4(content):
    # clear the old content
    clearContent(content)

    # add the title
    tk.Label(content, text="Consulta 1", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=4)

    # add explanation
    tk.Label(content, text='Para cada vendedor, listar a quantidade de vendas executadas nos últimos 30 dias e o preço total das festas vendidas.\nOrdenar decrescentemente por preço.', font='Helvetica 12').grid(row=1, column=0, sticky="nsew", columnspan=4)

    # add 
    tk.Label(content, text="Nome", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=0, sticky="nsew")
    tk.Label(content, text="CPF", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=1, sticky="nsew")
    tk.Label(content, text="Num Festas", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=2, sticky="nsew")
    tk.Label(content, text="Total Festas", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=3, sticky="nsew")

    # add the table content
    server.cur.execute('SELECT F.NOME, F.CPF, COUNT(C.FESTA) AS NUM_FESTAS, SUM(C.PRECO) AS TOTAL_VENDIDO\
        FROM VENDEDOR V JOIN FUNCIONARIO F\
        ON V.CPF=F.CPF\
        LEFT JOIN CONTRATO C\
        ON C.VENDEDOR=F.CPF\
        WHERE C.DATA >= SYSDATE - 30\
        GROUP BY F.CPF, F.NOME\
        ORDER BY SUM(C.PRECO) DESC')

    i = 3
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            tk.Label(content, text=result[j], padx=15, pady=5, borderwidth=2, relief="ridge").grid(row=i, column=j, sticky="nsew")
        i = i + 1
