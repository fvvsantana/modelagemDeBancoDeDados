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
        font='Helvetica 14 bold').grid(row=0, sticky='nsew')
    tk.Label(menu,
        pady='5',
        anchor='w',
        text="Dados",
        bg='lightskyblue',
        font='Helvetica 12 bold').grid(row=1, sticky='nsew')
    tk.Button(menu,
        text="Locais",
        anchor='w',
        command=buttonFunction,
        font='Helvetica 12').grid(row=3, sticky='nsew')
    tk.Button(menu,
        text="Formaturas",
        anchor='w',
        command=buttonFunction,
        font='Helvetica 12').grid(row=4, sticky='nsew')
    tk.Button(menu,
        text="Funcionários",
        anchor='w',
        command=buttonFunction,
        font='Helvetica 12').grid(row=5, sticky='nsew')
    tk.Button(menu,
        text="Clientes",
        anchor='w',
        command=lambda: content.showClient(contentContainer),
        font='Helvetica 12').grid(row=6, sticky='nsew')
    tk.Button(menu,
        text="Contratos",
        anchor='w',
        command=buttonFunction,
        font='Helvetica 12').grid(row=7, sticky='nsew')
    tk.Label(menu,
        pady='5',
        anchor='w',
        text="Consultas",
        bg='lightskyblue',
        font='Helvetica 12 bold').grid(row=8, sticky='nsew')
    tk.Button(menu,
        text="Exemplo",
        anchor='w',
        command=buttonFunction,
        font='Helvetica 12').grid(row=9, sticky='nsew')