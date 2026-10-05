import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.iconbitmap("../assets/icon.ico")

button_start = tk.Button(root, text="start")
button_start.pack()
button_start2 = tk.Button(root, text="start")
button_start2.pack()
button_start3 = tk.Button(root, text="start")
button_start3.pack()

root.mainloop()

