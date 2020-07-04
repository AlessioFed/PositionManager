import tkinter as tk
import json
import os

class App:

      def __init__(self, master):
         self.master = master
         master.title("POSITION MANAGER")

         self.overview = tk.Label(master, text="", bg="green", fg="black", font=("Times", 15, "bold"))
         self.overview.grid(row="2", column="3")

         self.header = tk.Label(master, text="POSITION MANAGER", bg="white", fg="black", font=("Times", 16, "bold italic"))
         self.header.grid(row="0", column="3")

         self.saveLabel = tk.Label(master, bg="green", text="Save New Location (name,coords)", font=("Times", 15, "bold"))
         self.saveLabel.grid(row="1", column="0")

         self.getLabel = tk.Label(master, bg="green", text="Get existing Location (name)", font=("Times", 15, "bold"))
         self.getLabel.grid(row="1", column="5")

         self.savebox = tk.Entry(master)
         self.savebox.grid(row="2", column="0")

         self.getbox = tk.Entry(master)
         self.getbox.grid(row="2", column="5")

         self.savebutton = tk.Button(master, text = "Save", command = self.savepos, bg = "black", fg = "white", font=("Times", 10, "bold"))
         self.savebutton.grid(row="3", column="0")

         self.getbutton = tk.Button(master, text = "Get", command = self.getpos, bg = "black", fg = "white", font=("Times", 10, "bold"))
         self.getbutton.grid(row="3", column="5")

         self.sl = tk.Label(master, text="", bg = "green", fg = "black", font=("Times", 15, "bold"))
         self.sl.grid(row="4", column="0")

         self.gl = tk.Label(master, text="", bg = "green", fg = "black", font=("Times", 15, "bold"))
         self.gl.grid(row="4", column="5")

         self.removeLabel = tk.Label(master, bg="green", text="Remove Location", font=("Times", 15, "bold"))
         self.removeLabel.grid(row="5", column="3")

         self.removebox = tk.Entry(master)
         self.removebox.grid(row="6", column="3")

         self.removebutton = tk.Button(master, text="Remove", command = self.removeentry, bg = "black", fg = "white", font=("Times", 10, "bold"))
         self.removebutton.grid(row="7", column="3")

         self.rl =tk.Label(master, text="", bg = "green", fg = "black", font=("Times", 15, "bold"))
         self.rl.grid(row="8", column="3")

      def update_list(self):
         with open("locations.json", "r") as f:
            pos_dict = json.load(f)
            key_list = list(pos_dict.keys())
         self.overview["text"] = "Existing Locations: \n" + "\n".join(key_list)

      def savepos(self):
         entry = self.savebox.get().split(',')
         name = entry[0]
         coords = entry[1]
         new_pos = {name: coords}
         with open("locations.json", "r") as f:
            pos_dict = json.load(f)
            pos_dict.update(new_pos)
            print(json.dumps(pos_dict, indent=4))
         with open("locations.json", "w") as f:
            json.dump(pos_dict, f, indent=4)
         self.sl["text"] = "Added %s to your saves!" % (name + ':' + coords)
         self.update_list()

      def getpos(self):
         name = self.getbox.get()
         with open("locations.json", "r") as f:
            pos_dict = json.load(f)
            self.gl["text"] = "Location %s : %s" % (name, pos_dict[name])
            os.system("echo %s | clip" % pos_dict[name])

      def removeentry(self):
         name = self.removebox.get()
         with open("locations.json", "r") as f:
            pos_dict = json.load(f)
            del pos_dict[name]
            print(json.dumps(pos_dict, indent=4))
         with open("locations.json", "w") as f:
            json.dump(pos_dict, f, indent=4)
         self.update_list()
         self.rl["text"] = "Removed Location %s" % name

