import json
import tkinter as tk

root = tk.Tk()
root.configure(bg = "green")
root.title("POSITION MANAGER")

overview = tk.Label(root, text="", width="20", bg="green", fg="black", font=("Times", 15, "bold"))
overview.grid(row="2", column="3")

def update_list():
   with open("locations.json", "r") as f:
      pos_dict = json.load(f)
      key_list = list(pos_dict.keys())
      overview["text"] = "Existing Locations: \n" + "\n".join(key_list)

update_list()

def savepos():
   entry = savebox.get().split(',')
   name = entry[0]
   coords = entry[1]
   with open("locations.json") as f:
      pos_dict = json.load(f)
      new_pos = {name: coords}
      pos_dict.update(new_pos)
      print(json.dumps(pos_dict))
   with open("locations.json", "w") as json_file:
      json.dump(pos_dict, json_file)
   sl["text"] = "Added %s to your saves!" % (name + ':' + coords)
   update_list()

def getpos():
   name = getbox.get()
   with open("locations.json") as f:
      pos_dict = json.load(f)
      print(pos_dict[name])
      gl["text"] = "Location %s : %s" % (name, pos_dict[name])

def showentries():
   with open("locations.json") as f:
      pos_dict = json.load(f)
      for i in pos_dict:
         print(i, ":", pos_dict[i])

def removeentry(name):
   with open("locations.json", "r") as f:
      pos_dict = json.load(f)
      del pos_dict[name]
   with open("locations.json", "w") as json_file:
      json.dump(pos_dict, json_file)


header = tk.Label(root, text="POSITION MANAGER", width="20", height = "2", bg="white", fg="black", font=("Times", 16, "bold italic"))
header.grid(row="0", column="3")

saveLabel = tk.Label(root, height="2", bg="green", text="Save New Position (name,coords)", font=("Times", 15, "bold"))
saveLabel.grid(row="1", column="0")

getLabel = tk.Label(root, height="2", bg="green", text="Get New Position (name)", font=("Times", 15, "bold"))
getLabel.grid(row="1", column="5")

savebox = tk.Entry(root, width = "75")
savebox.grid(row="2", column="0")

getbox = tk.Entry(root, width = "75")
getbox.grid(row="2", column="5")

savebutton = tk.Button(root, text = "Save", width = "60", height = "4", command = savepos, bg = "black", fg = "white", font=("Times", 10, "bold"))
savebutton.grid(row="3", column="0")

getbutton = tk.Button(root, text = "Get", width = "60", height = "4", command = getpos, bg = "black", fg = "white", font=("Times", 10, "bold"))
getbutton.grid(row="3", column="5")

sl = tk.Label(root, text="", width = "60", height = "4", bg = "green", fg = "black", font=("Times", 15, "bold"))
sl.grid(row="4", column="0")

gl = tk.Label(root, text="", width = "60", height = "4", bg = "green", fg = "black", font=("Times", 15, "bold"))
gl.grid(row="4", column="5")



root.mainloop()
