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
def showQuery1(content):
    # clear the old content
    clearContent(content)

    # add the title
    tk.Label(content, text="Consulta 1", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=4)

    # add explanation
    tk.Label(content, text='Para cada cliente físico, mostrar o número de festas e o total gasto nos últimos cinco anos, ordenado decrescentemente pelo montante gasto.', font='Helvetica 12').grid(row=1, column=0, sticky="nsew", columnspan=4)

    # add 
    tk.Label(content, text="Nome", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=0, sticky="nsew")
    tk.Label(content, text="CPF", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=1, sticky="nsew")
    tk.Label(content, text="Num Festas", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=2, sticky="nsew")
    tk.Label(content, text="Total Festas", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=2, column=3, sticky="nsew")

    # add the table content
    server.cur.execute(' SELECT F.NOME, F.CPF, COUNT(C.FESTA) AS NUM_FESTAS, SUM(C.PRECO) AS TOTAL_FESTAS \
            FROM CLIENTE_FISICO F JOIN CONTRATO C \
            ON F.CODIGO=C.CLIENTE \
            WHERE EXTRACT(YEAR FROM C.DATA) >= EXTRACT(YEAR FROM SYSDATE) - 5 \
            GROUP BY F.CPF, F.NOME \
            ORDER BY SUM(C.PRECO) DESC')

    i = 3
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            tk.Label(content, text=result[j], padx=15, pady=5, borderwidth=2, relief="ridge").grid(row=i, column=j, sticky="nsew")


# show the client list table
def showClient(content):
    # clear the old content
    clearContent(content)

    # add the table headers
    tk.Label(content, text="Código", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=0, sticky="nsew")
    tk.Label(content, text="Natureza", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=1, sticky="nsew")
    tk.Label(content, text="Email", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=2, sticky="nsew")
    tk.Label(content, text="Telefone", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=3, sticky="nsew")

    # add the options header
    tk.Label(content, text="Opções", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=4, sticky="nsew", columnspan=2)

    # add the title
    tk.Label(content, text="Lista de Clientes", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=content.grid_size()[0])

    # add the "new" button
    tk.Button(content, text="Adicionar", command=lambda:addClient(content), relief=tk.RIDGE, pady=3, padx=15, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2')\
        .grid(row=0, column=0, columnspan=content.grid_size()[0], stick='e', pady=5, padx=5)

    # add the table content
    server.cur.execute('select * from CLIENTE order by CODIGO')
    i = 2
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            tk.Label(content, text=result[j], padx=15, pady=5, borderwidth=2, relief="ridge").grid(row=i, column=j, sticky="nsew")
        tk.Button(content, text="Editar", padx=20, pady=5, borderwidth=2, relief="ridge", bg='lemonchiffon', cursor='hand2', command=lambda client=result:editClient(content, client)).grid(row=i, column=j+1, sticky="nsew")
        tk.Button(content, text="Excluir", padx=20, pady=5, borderwidth=2, relief="ridge", bg='mistyrose', cursor='hand2', command=lambda client=result:removeClient(content, client)).grid(row=i, column=j+2, sticky="nsew")
        i = i + 1
