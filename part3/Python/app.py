import tkinter as tk
import menu
import server

# open the server connection
server.openConnection()

# create and configure the root
root = tk.Tk()
root.geometry("1200x600")

# create and configure the lateral menu contatiner
menuContainer = tk.Frame(root, width=200)
menuContainer.pack(side='left', fill=tk.Y)
menuContainer.pack_propagate(0)

# create and configure the content container
content = tk.Frame(root)
content.pack(side='right', fill=tk.BOTH, expand=1)

# add an starting instruction
tk.Label(content,
    text='Selecione uma opção no menu lateral',
    font='Helvetica 12').pack(expand=1)

# fill the menu options
menu.fillMenu(menuContainer, content)

# start the tk loop to keep the interface open
tk.mainloop()

# close the connection after the interface is finished
server.closeConnection()