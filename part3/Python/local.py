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

# show local list table
def showLocal(content):
    # clear the old content
    clearContent(content)

    # add the table headers
    tk.Label(content, text="CEP", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=0, sticky="nsew")
    tk.Label(content, text="Número", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=1, sticky="nsew")
    tk.Label(content, text="Nome", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=2, sticky="nsew")
    tk.Label(content, text="Capacidade", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=3, sticky="nsew")
    tk.Label(content, text="e-mail", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=4, sticky="nsew")
    tk.Label(content, text="Telefone", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=5, sticky="nsew")

    # add the options header
    tk.Label(content, text="Opções", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=6, sticky="nsew", columnspan=2)

    # add the title
    tk.Label(content, text="Lista de Locais", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=content.grid_size()[0])

    # add the "new" button
    tk.Button(content, text="Adicionar", command=lambda:addLocal(content), relief=tk.RIDGE, pady=3, padx=15, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2')\
        .grid(row=0, column=0, columnspan=content.grid_size()[0], stick='e', pady=5, padx=5)

    # add the table content
    server.cur.execute('select * from LOCAL order by CEP, NUMERO')
    i = 2
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            tk.Label(content, text=result[j], padx=15, pady=5, borderwidth=2, relief="ridge").grid(row=i, column=j, sticky="nsew")
        tk.Button(content, text="Editar", padx=20, pady=5, borderwidth=2, relief="ridge", bg='lemonchiffon', cursor='hand2', command=lambda local=result:editLocal(content, local)).grid(row=i, column=j+1, sticky="nsew")
        tk.Button(content, text="Excluir", padx=20, pady=5, borderwidth=2, relief="ridge", bg='mistyrose', cursor='hand2', command=lambda local=result:removeLocal(content, local)).grid(row=i, column=j+2, sticky="nsew")
        i = i + 1

# show the new Local screen
def addLocal(content):
    # clear the old content
    clearContent(content)

    # set the second column to fill the free space
    tk.Grid.columnconfigure(content, 1, weight=1)

    # add the title
    tk.Label(content, text="Cadastrar Local", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=2, pady=5)

    # add the content
    tk.Label(content, text="CEP:", font='Helvetica 11').grid(row=1, column=0, pady=3, sticky='w')
    cep = tk.Entry(content)
    cep.grid(row=1, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Número:", font='Helvetica 11').grid(row=2, column=0, pady=3, sticky='w')
    numero = tk.Entry(content)
    numero.grid(row=2, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Nome:", font='Helvetica 11').grid(row=3, column=0, pady=3, sticky='w')
    nome = tk.Entry(content)
    nome.grid(row=3, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Capacidade:", font='Helvetica 11').grid(row=4, column=0, pady=3, sticky='w')
    capacidade = tk.Entry(content)
    capacidade.grid(row=4, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="e-mail:", font='Helvetica 11').grid(row=5, column=0, pady=3, sticky='w')
    email = tk.Entry(content)
    email.grid(row=5, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Telefone:", font='Helvetica 11').grid(row=6, column=0, pady=3, sticky='w')
    telefone = tk.Entry(content)
    telefone.grid(row=6, column=1, pady=3, padx=3, stick='nsew')

    def save():
        # prepare the SQL Insert command
        server.cur.prepare('insert into LOCAL(CEP, NUMERO, CAPACIDADE, EMAIL, TELEFONE, NOME) VALUES(:1, :2, :3, :4, :5, :6)')

        # get data about the Local from the user
        cep1 = cep.get()
        num = numero.get()
        nom = nome.get()
        cap = capacidade.get()
        em = email.get()
        tel = telefone.get()

        # execute the command and commit the result
        server.cur.execute(None, {'1':cep1, '2':num, '3':cap, '4':em, '5':tel, '6':nom})
        server.con.commit()

        # update Local list table
        showLocal(content)

    # add the confirm button
    tk.Button(content, text="Concluir", command=save, relief=tk.RIDGE, pady=3, padx=50, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2').grid(row=7, column=0, columnspan=2, pady=5)

def removeLocal(content, local):
    # prepare the SQL Delete command
    server.cur.prepare("delete from LOCAL where CEP = :1 and NUMERO = :2")

    # get Local's CEP and Number from the tuple
    cep = local[0]
    num = local[1]

    # execute the command and commit the result
    server.cur.execute(None, {'1':cep, '2':num})
    server.con.commit()

    # update Local list table
    showLocal(content)

def editLocal(content, local):
    # clear the old content
    clearContent(content)

    # set the second column to fill the free space
    tk.Grid.columnconfigure(content, 1, weight=1)

    # add the title
    tk.Label(content, text="Editar Local", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=2, pady=5)

    # add the content
    tk.Label(content, text="CEP:", font='Helvetica 11').grid(row=1, column=0, pady=3, sticky='w')
    cep = tk.Entry(content, state='disabled')
    cep.insert(0, local[0])
    cep.grid(row=1, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Número:", font='Helvetica 11').grid(row=2, column=0, pady=3, sticky='w')
    numero = tk.Entry(content, state='disabled')
    numero.insert(0, local[1])
    numero.grid(row=2, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Nome:", font='Helvetica 11').grid(row=3, column=0, pady=3, sticky='w')
    nome = tk.Entry(content)
    nome.insert(0, local[2])
    nome.grid(row=3, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Capacidade:", font='Helvetica 11').grid(row=4, column=0, pady=3, sticky='w')
    capacidade = tk.Entry(content)
    capacidade.insert(0, local[3])
    capacidade.grid(row=4, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="e-mail:", font='Helvetica 11').grid(row=5, column=0, pady=3, sticky='w')
    email = tk.Entry(content)
    email.insert(0, local[4])
    email.grid(row=5, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Telefone:", font='Helvetica 11').grid(row=6, column=0, pady=3, sticky='w')
    telefone = tk.Entry(content)
    telefone.insert(0, local[5])
    telefone.grid(row=6, column=1, pady=3, padx=3, stick='nsew')

    def save():
        # prepare the SQL Update command
        server.cur.prepare("update LOCAL set NOME = :3, CAPACIDADE = :4, EMAIL = :5, TELEFONE = :6 where CEP = :1 and NUMERO = :2")

        # get data about the Local from the user
        cep1 = local[0]
        num = local[1]
        nom = nome.get()
        cap = capacidade.get()
        em = email.get()
        tel = telefone.get()

        # execute the command and commit the result
        server.cur.execute(None, {'1':cep1, '2':num, '3':nom, '4':cap, '5':em, '6':tel})
        server.con.commit()

        # update Local list table
        showLocal(content)

    # add the confirm button
    tk.Button(content, text="Concluir", command=save, relief=tk.RIDGE, pady=3, padx=50, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2').grid(row=7, column=0, columnspan=2, pady=5)
