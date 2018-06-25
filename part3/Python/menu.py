import tkinter as tk
import content
import query1

# example fuction for button press
def buttonFunction():
    print('botao')

# add the menu options
def fillMenu(menu, contentContainer):
    tk.Label(menu,
        pady='5',
        text="Menu",
        fg='white',
        bg='deepskyblue',
        font='Helvetica 14 bold').pack(fill=tk.X)
    tk.Label(menu,
        pady='5',
        anchor='w',
        text="Dados",
        bg='lightskyblue',
        font='Helvetica 12 bold').pack(fill=tk.X)
    tk.Button(menu,
        text="Locais",
        anchor='w',
        command=buttonFunction,
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Formaturas",
        anchor='w',
        command=buttonFunction,
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Funcionários",
        anchor='w',
        command=buttonFunction,
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Clientes",
        anchor='w',
        command=lambda: content.showClient(contentContainer),
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Contratos",
        anchor='w',
        command=buttonFunction,
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Locações",
        anchor='w',
        command=buttonFunction,
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Supervisões",
        anchor='w',
        command=buttonFunction,
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Label(menu,
        pady='5',
        anchor='w',
        text="Consultas",
        bg='lightskyblue',
        font='Helvetica 12 bold').pack(fill=tk.X)
    tk.Button(menu,
        text="Consulta 1",
        anchor='w',
        command=lambda: query1.showQuery1(contentContainer),
        cursor='hand2',
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)

