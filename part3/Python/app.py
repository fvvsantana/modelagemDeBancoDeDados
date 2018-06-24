import tkinter as tk
import menu
import server

server.openConnection()

# create and configure the root
root = tk.Tk()
root.geometry("1000x600")
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 1, weight=1,)

# create and configure the lateral menu contatiner
menuContainer = tk.Frame(root)
menuContainer.grid(row=0, column=0, sticky='nsew')
tk.Grid.columnconfigure(menuContainer, 0, weight=1)

# create and configure the content container
content = tk.Frame(root)
content.grid(row=0, column=1, sticky='nsew')

# fill the menu options
menu.fillMenu(menuContainer, content)

tk.mainloop()
server.closeConnection()