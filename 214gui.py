import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x200")
root.title("authorization")

root.grid()


blue = tk.Canvas(height = 100, width = 200, background = "blue")
blue.grid(row = 0, column = 0)

green = tk.Canvas(height = 100, width = 100, background = "green")
green.grid(row = 0, column = 1)

red= tk.Canvas(height = 100, width = 200, background = "red")
red.grid(row = 1, column = 0)

yellow = tk.Canvas(height = 100, width = 100, background = "yellow")
yellow.grid(row = 1, column = 1)

root.mainloop()