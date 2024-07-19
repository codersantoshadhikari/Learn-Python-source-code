import tkinter as tk
from tkinter import messagebox
def calculate():
    num = int(entry1.get())
    sq = num * num
    messagebox.showinfo("Square", f"The Square of {num} is {sq}")

root = tk.Tk()
root.geometry("300x300")
root.title("Square Calculator")

# FOr number 

label1= tk.Label(root, text="Enter the number")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()



button1 = tk.Button(root, text="Calculate", command=calculate)
button1.pack()

root.mainloop()

