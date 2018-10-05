import tkinter as tk
  

consumos = [0]*12
mesa= 0 

#tk.Label(root, text="Bar Do Ze ").pack()
#tk.Button(root, text="Olha e sou um botao")
#tk.Entry(root, text ="qualquer coisa ")

def banana1():
   print("Mesa 1")
   global mesa
   mesa = 1

def banana2():
	print("Mesa 2")

def banana3():
	print("Mesa 3")

def banana4():
	print("Mesa 4")

def banana5():
		print("Mesa 5 ")
def banana6():
	print("Mesa 6 ")

def banana7():
	print("Mesa 7")

def banana8():
	print("Mesa 8")
def banana9():
	print("Mesa 9")
def banana10():
	print("Mesa 10")
def	banana11():
	print("Mesa 11")
def banana12():
	print("Mesa 12")		

root = tk.Tk()

tk.Button(root, text="M1", command=banana1).grid(row=0, column=1)
tk.Button(root, text="M2", command=banana2).grid(row=0, column=2)
tk.Button(root, text="M3", command=banana3).grid(row=0, column=3)
tk.Button(root, text="M4",command=banana4).grid(row=0, column=4)
tk.Button(root, text="M5", command=banana5).grid(row=1, column=1)
tk.Button(root, text="M6", command=banana6).grid(row=1, column=2)
tk.Button(root, text="M7", command=banana7).grid(row=1, column=3)
tk.Button(root, text="M8", command=banana8).grid(row=1, column=4)
tk.Button(root, text="M9", command=banana9).grid(row=2, column=1)
tk.Button(root, text="M10", command=banana10).grid(row=2, column=2)
tk.Button(root, text="M11", command=banana11).grid(row=2, column=3)
tk.Button(root, text="M12", command=banana12).grid(row=2, column=4)

root.mainloop()


