import tkinter as tk
import content

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
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Formaturas",
        anchor='w',
        command=buttonFunction,
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Funcionários",
        anchor='w',
        command=buttonFunction,
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Clientes",
        anchor='w',
        command=lambda: content.showClient(contentContainer),
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Button(menu,
        text="Contratos",
        anchor='w',
        command=buttonFunction,
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)
    tk.Label(menu,
        pady='5',
        anchor='w',
        text="Consultas",
        bg='lightskyblue',
        font='Helvetica 12 bold').pack(fill=tk.X)
    tk.Button(menu,
        text="Exemplo",
        anchor='w',
        command=buttonFunction,
        relief=tk.RIDGE,
        font='Helvetica 12').pack(fill=tk.X)