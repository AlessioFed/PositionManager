import json
import tkinter as tk
import managerGUI as gui

root = tk.Tk()
root.configure(bg = "green")
window = gui.App(root)

with open("locations.json", "r") as f:
   pos_dict = json.load(f)

   window.update_list()

   def showentries():
      for i in pos_dict:
            print(i, ":", pos_dict[i])

root.mainloop()
