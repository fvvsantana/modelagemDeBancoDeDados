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

# show the new client screen
def addClient(content):
    # clear the old content
    clearContent(content)

    # set the second column to fill the free space
    tk.Grid.columnconfigure(content, 1, weight=1)

    # add the title
    tk.Label(content, text="Cadastrar Cliente", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=2, pady=5)

    # add the content
    tk.Label(content, text="Código:", font='Helvetica 11').grid(row=1, column=0, pady=3, sticky='w')
    codigo = tk.Entry(content)
    codigo.grid(row=1, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Natureza:", font='Helvetica 11').grid(row=2, column=0, pady=3, sticky='w')
    natureza = ttk.Combobox(content, values=('FISICO', 'JURIDICO'), state="readonly")
    natureza.current(0)
    natureza.grid(row=2, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Email:", font='Helvetica 11').grid(row=3, column=0, pady=3, sticky='w')
    email = tk.Entry(content)
    email.grid(row=3, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Telefone:", font='Helvetica 11').grid(row=4, column=0, pady=3, sticky='w')
    telefone = tk.Entry(content)
    telefone.grid(row=4, column=1, pady=3, padx=3, stick='nsew')

    def save():
        # prepare the SQL Insert command
        server.cur.prepare("insert into CLIENTE(CODIGO, NATUREZA, EMAIL, TELEFONE) VALUES(:1, :2, :3, :4)")

        # get data about the Client from the user
        cod = codigo.get()
        nat = natureza.get()
        em = email.get()
        tel = telefone.get()

        # execute the command and commit the result
        server.cur.execute(None, {'1':cod, '2':nat, '3':em, '4':tel})
        server.con.commit()

        # update Client list table
        showClient(content)

    # add the confirm button
    tk.Button(content, text="Concluir", command=save, relief=tk.RIDGE, pady=3, padx=50, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2').grid(row=5, column=0, columnspan=2, pady=5)

def removeClient(content, client):
    # prepare the SQL Delete command
    server.cur.prepare("delete from CLIENTE where CODIGO = :1")

    # get Client's code from the tuple
    cod = client[0]

    # execute the command and commit the result
    server.cur.execute(None, {'1':cod})
    server.con.commit()

    # update Client list table
    showClient(content)

def editClient(content, client):
    # clear the old content
    clearContent(content)

    # set the second column to fill the free space
    tk.Grid.columnconfigure(content, 1, weight=1)

    # add the title
    tk.Label(content, text="Editar Cliente", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=2, pady=5)

    # add the content
    tk.Label(content, text="Código:", font='Helvetica 11').grid(row=1, column=0, pady=3, sticky='w')
    codigo = tk.Entry(content, state='disabled')
    codigo.insert(0, client[0])
    codigo.grid(row=1, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Natureza:", font='Helvetica 11').grid(row=2, column=0, pady=3, sticky='w')
    natureza = ttk.Combobox(content, values=('FISICO', 'JURIDICO'), state="readonly")
    natureza.set(client[1])
    natureza.grid(row=2, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Email:", font='Helvetica 11').grid(row=3, column=0, pady=3, sticky='w')
    email = tk.Entry(content)
    email.insert(0, client[2])
    email.grid(row=3, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Telefone:", font='Helvetica 11').grid(row=4, column=0, pady=3, sticky='w')
    telefone = tk.Entry(content)
    telefone.insert(0, client[3])
    telefone.grid(row=4, column=1, pady=3, padx=3, stick='nsew')

    def save():
        # prepare the SQL Update command
        server.cur.prepare("update CLIENTE set NATUREZA = :2, EMAIL = :3, TELEFONE = :4 where CODIGO = :1")

        # get data about the Client from the user
        cod = client[0]
        nat = natureza.get()
        em = email.get()
        tel = telefone.get()

        # execute the command and commit the result
        server.cur.execute(None, {'1':cod, '2':nat, '3':em, '4':tel})
        server.con.commit()

        # update Client list table
        showClient(content)

    # add the confirm button
    tk.Button(content, text="Concluir", command=save, relief=tk.RIDGE, pady=3, padx=50, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2').grid(row=5, column=0, columnspan=2, pady=5)
