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
    tk.Label(content, text="Consulta 1", font='Helvetica 14').grid(row=0, stick='nsew')

    # add explanation
    tk.Label(content, text='Para cada cliente físico, mostrar o número de festas e o total gasto nos últimos cinco anos, ordenado decrescentemente pelo montante gasto.', font='Helvetica 12').grid(row=1, column=0, sticky="nsew")

