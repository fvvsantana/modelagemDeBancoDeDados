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

# show employee list table
def showEmployee(content):
    # clear the old content
    clearContent(content)

    # add the table headers
    tk.Label(content, text="CPF", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=0, sticky="nsew")
    tk.Label(content, text="Nome", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=1, sticky="nsew")
    tk.Label(content, text="Email", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=2, sticky="nsew")
    tk.Label(content, text="Telefone", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=3, sticky="nsew")
    tk.Label(content, text="Salário", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=4, sticky="nsew")
    tk.Label(content, text="Banco", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=5, sticky="nsew")
    tk.Label(content, text="Agência", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=6, sticky="nsew")
    tk.Label(content, text="Número da conta", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=7, sticky="nsew")
    tk.Label(content, text="Endereço completo", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=8, sticky="nsew")
    tk.Label(content, text="Cargo", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=9, sticky="nsew")

    # add the options header
    tk.Label(content, text="Opções", padx=20, pady=5, borderwidth=2, relief="ridge", bg='palegreen', font="Helvetica 11 bold").grid(row=1, column=10, sticky="nsew", columnspan=2)

    # add the title
    tk.Label(content, text="Lista de Funcionários", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=content.grid_size()[0])

    # add the "new" button
    tk.Button(content, text="Adicionar", command=lambda:addEmployee(content), relief=tk.RIDGE, pady=3, padx=15, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2')\
        .grid(row=0, column=0, columnspan=content.grid_size()[0], stick='e', pady=5, padx=5)

    # add the table content
    server.cur.execute('select * from FUNCIONARIO order by CPF')
    i = 2
    for result in server.cur:
        for j in range(len(result)):
            tk.Grid.columnconfigure(content, j, weight=1)
            tk.Label(content, text=result[j], padx=15, pady=5, borderwidth=2, relief="ridge").grid(row=i, column=j, sticky="nsew")
        tk.Button(content, text="Editar", padx=20, pady=5, borderwidth=2, relief="ridge", bg='lemonchiffon', cursor='hand2', command=lambda employee=result:editEmployee(content, employee)).grid(row=i, column=j+1, sticky="nsew")
        tk.Button(content, text="Excluir", padx=20, pady=5, borderwidth=2, relief="ridge", bg='mistyrose', cursor='hand2', command=lambda employee=result:removeEmployee(content, employee)).grid(row=i, column=j+2, sticky="nsew")
        i = i + 1

# show the new employee screen
def addEmployee(content):
    # clear the old content
    clearContent(content)

    # set the second column to fill the free space
    tk.Grid.columnconfigure(content, 1, weight=1)

    # add the title
    tk.Label(content, text="Cadastrar Funcionario", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=2, pady=5)

    # add the content
    tk.Label(content, text="CPF:", font='Helvetica 11').grid(row=1, column=0, pady=3, sticky='w')
    cpf = tk.Entry(content)
    cpf.grid(row=1, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Nome:", font='Helvetica 11').grid(row=2, column=0, pady=3, sticky='w')
    nome = tk.Entry(content)
    nome.grid(row=2, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Email:", font='Helvetica 11').grid(row=3, column=0, pady=3, sticky='w')
    email = tk.Entry(content)
    email.grid(row=3, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Telefone:", font='Helvetica 11').grid(row=4, column=0, pady=3, sticky='w')
    telefone = tk.Entry(content)
    telefone.grid(row=4, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Salário", font='Helvetica 11').grid(row=5, column=0, pady=3, sticky='w')
    salario = tk.Entry(content)
    salario.grid(row=5, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Banco:", font='Helvetica 11').grid(row=6, column=0, pady=3, sticky='w')
    banco = tk.Entry(content)
    banco.grid(row=6, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Agência:", font='Helvetica 11').grid(row=7, column=0, pady=3, sticky='w')
    agencia = tk.Entry(content)
    agencia.grid(row=7, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Número da conta:", font='Helvetica 11').grid(row=8, column=0, pady=3, sticky='w')
    numero = tk.Entry(content)
    numero.grid(row=8, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Endereço completo:", font='Helvetica 11').grid(row=9, column=0, pady=3, sticky='w')
    endereco = tk.Entry(content)
    endereco.grid(row=9, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Cargo:", font='Helvetica 11').grid(row=10, column=0, pady=3, sticky='w')
    cargo = tk.Entry(content)
    cargo.grid(row=10, column=1, pady=3, padx=3, stick='nsew')

    def save():
        # prepare the SQL Insert command
        server.cur.prepare('insert into FUNCIONARIO(CPF, NOME, EMAIL, TELEFONE, SALARIO, BANCO, AGENCIA, NUMERO, ENDERECO, CARGO) VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)')

        # get data about the employee from the user
        cpf1 = cpf.get()
        nom = nome.get()
        em = email.get()
        tel = telefone.get()
        sal = salario.get()
        ban = banco.get()
        ag = agencia.get()
        num = numero.get()
        end = endereco.get()
        car = cargo.get()

        # execute the command and commit the result
        server.cur.execute(None, {'1':cpf1, '2':nom, '3':em, '4':tel, '5':sal, '6':ban, '7':ag, '8':num, '9':end, '10':car})
        server.con.commit()

        # update employee list table
        showEmployee(content)

    # add the confirm button
    tk.Button(content, text="Concluir", command=save, relief=tk.RIDGE, pady=3, padx=50, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2').grid(row=11, column=0, columnspan=2, pady=5)

def removeEmployee(content, employee):
    # prepare the SQL Delete command
    server.cur.prepare("delete from FUNCIONARIO where CPF = :1")

    # get employee's CPF from the tuple
    cpf = employee[0]

    # execute the command and commit the result
    server.cur.execute(None, {'1':cpf})
    server.con.commit()

    # update employee list table
    showEmployee(content)

def editEmployee(content, employee):
    # clear the old content
    clearContent(content)

    # set the second column to fill the free space
    tk.Grid.columnconfigure(content, 1, weight=1)

    # add the title
    tk.Label(content, text="Editar Funcionario", font='Helvetica 14').grid(row=0, stick='nsew', columnspan=2, pady=5)

    # add the content
    tk.Label(content, text="CPF:", font='Helvetica 11').grid(row=1, column=0, pady=3, sticky='w')
    cpf = tk.Entry(content)
    cpf.insert(0, employee[0])
    cpf.grid(row=1, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Nome:", font='Helvetica 11').grid(row=2, column=0, pady=3, sticky='w')
    nome = tk.Entry(content)
    nome.insert(0, employee[1])
    nome.grid(row=2, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Email:", font='Helvetica 11').grid(row=3, column=0, pady=3, sticky='w')
    email = tk.Entry(content)
    email.insert(0, employee[2])
    email.grid(row=3, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Telefone:", font='Helvetica 11').grid(row=4, column=0, pady=3, sticky='w')
    telefone = tk.Entry(content)
    telefone.insert(0, employee[3])
    telefone.grid(row=4, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Salário", font='Helvetica 11').grid(row=5, column=0, pady=3, sticky='w')
    salario = tk.Entry(content)
    salario.insert(0, employee[4])
    salario.grid(row=5, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Banco:", font='Helvetica 11').grid(row=6, column=0, pady=3, sticky='w')
    banco = tk.Entry(content)
    banco.grid(row=6, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Agência:", font='Helvetica 11').grid(row=7, column=0, pady=3, sticky='w')
    agencia = tk.Entry(content)
    agencia.insert(0, employee[5])
    agencia.grid(row=7, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Número da conta:", font='Helvetica 11').grid(row=8, column=0, pady=3, sticky='w')
    numero = tk.Entry(content)
    numero.insert(0, employee[6])
    numero.grid(row=8, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Endereço completo:", font='Helvetica 11').grid(row=9, column=0, pady=3, sticky='w')
    endereco = tk.Entry(content)
    endereco.insert(0, employee[7])
    endereco.grid(row=9, column=1, pady=3, padx=3, stick='nsew')

    tk.Label(content, text="Cargo:", font='Helvetica 11').grid(row=10, column=0, pady=3, sticky='w')
    cargo = tk.Entry(content)
    cargo.insert(0, employee[8])
    cargo.grid(row=10, column=1, pady=3, padx=3, stick='nsew')

    def save():
        # prepare the SQL Update command
        server.cur.prepare("update FUNCIONARIO set NOME = :2, EMAIL = :3, TELEFONE = :4, SALARIO = :5, BANCO = :6, AGENCIA = :7, NUMERO  = :8, ENDERECO = :9, CARGO = :10 where CPF = :1")

        # get data about the employee from the user
        cpf = employee[0]
        nom = nome.get()
        em = email.get()
        tel = telefone.get()
        sal = salario.get()
        ban = banco.get()
        ag = agencia.get()
        num = numero.get()
        end = endereco.get()
        car = cargo.get()

        # execute the command and commit the result
        server.cur.execute(None, {'1':cpf, '2':nom, '3':em, '4':tel, '5':sal, '6':ban, '7':ag, '8':num, '9':end, '10':car})
        server.con.commit()

        # update employee list table
        showEmployee(content)

    # add the confirm button
    tk.Button(content, text="Concluir", command=save, relief=tk.RIDGE, pady=3, padx=50, bg='green', fg='white', font='Helvetica 11 bold', cursor='hand2').grid(row=11, column=0, columnspan=2, pady=5)
