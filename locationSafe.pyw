import json
import tkinter as tk

root = tk.Tk()
root.configure(bg = "green")
root.title("POSITION MANAGER")

overview = tk.Label(root, text="", bg="green", fg="black", font=("Times", 15, "bold"))
overview.grid(row="2", column="3")

with open("locations.json", "r") as f:
   pos_dict = json.load(f)

   def update_list():
         key_list = list(pos_dict.keys())
         overview["text"] = "Existing Locations: \n" + "\n".join(key_list)

   update_list()

   def getpos():
      name = getbox.get()
      print(pos_dict[name])
      gl["text"] = "Location %s : %s" % (name, pos_dict[name])

   def showentries():
      for i in pos_dict:
            print(i, ":", pos_dict[i])

   def savepos():
      entry = savebox.get().split(',')
      name = entry[0]
      coords = entry[1]
      new_pos = {name: coords}
      pos_dict.update(new_pos)
      print(json.dumps(pos_dict, indent=4))
      with open("locations.json", "w") as f:
         json.dump(pos_dict, f, indent=4)
      sl["text"] = "Added %s to your saves!" % (name + ':' + coords)
      update_list()

   def removeentry():
      name = removebox.get()
      del pos_dict[name]
      with open("locations.json", "w") as f:
         json.dump(pos_dict, f, indent=4)
      update_list()
      rl["text"] = "Removed Location %s" % name
      

   header = tk.Label(root, text="POSITION MANAGER", bg="white", fg="black", font=("Times", 16, "bold italic"))
   header.grid(row="0", column="3")

   saveLabel = tk.Label(root, bg="green", text="Save New Location (name,coords)", font=("Times", 15, "bold"))
   saveLabel.grid(row="1", column="0")

   getLabel = tk.Label(root, bg="green", text="Get existing Location (name)", font=("Times", 15, "bold"))
   getLabel.grid(row="1", column="5")

   savebox = tk.Entry(root,)
   savebox.grid(row="2", column="0")

   getbox = tk.Entry(root,)
   getbox.grid(row="2", column="5")

   savebutton = tk.Button(root, text = "Save", command = savepos, bg = "black", fg = "white", font=("Times", 10, "bold"))
   savebutton.grid(row="3", column="0")

   getbutton = tk.Button(root, text = "Get", command = getpos, bg = "black", fg = "white", font=("Times", 10, "bold"))
   getbutton.grid(row="3", column="5")

   sl = tk.Label(root, text="", bg = "green", fg = "black", font=("Times", 15, "bold"))
   sl.grid(row="4", column="0")

   gl = tk.Label(root, text="", bg = "green", fg = "black", font=("Times", 15, "bold"))
   gl.grid(row="4", column="5")

   removeLabel = tk.Label(root, bg="green", text="Remove Location", font=("Times", 15, "bold"))
   removeLabel.grid(row="5", column="3")

   removebox = tk.Entry(root)
   removebox.grid(row="6", column="3")

   removebutton = tk.Button(root, text="Remove", command = removeentry, bg = "black", fg = "white", font=("Times", 10, "bold"))
   removebutton.grid(row="7", column="3")

   rl =tk.Label(root, text="", bg = "green", fg = "black", font=("Times", 15, "bold"))
   rl.grid(row="8", column="3")

   root.mainloop()
