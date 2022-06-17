import tkinter as tk
root = tk.Tk()
root.title ("counter")
label = tk.Label (root, fg= "dark green")
label.pack()
button = tk.Button (root, text="Stop",width=40)
button.pack()
root.mainloop()