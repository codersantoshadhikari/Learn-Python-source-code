# # import tkinter as tk
# # from tkinter import ttk

# # def calculate_square():
# #     try:
# #         number = float(entry_number.get())
# #         square = number ** 2
# #         result_label.config(text=f"Square: {square}")
# #     except ValueError:
# #         result_label.config(text="Please enter a valid number")

# # root = tk.Tk()
# # root.title("Square Calculator")
# # root.geometry("300x200")
# # root.resizable(0, 0)  # Disable resizing

# # mainframe = ttk.Frame(root, padding="20")
# # mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# # # Labels and Entry
# # ttk.Label(mainframe, text="Enter a number:").grid(column=0, row=0, padx=5, pady=5)
# # entry_number = ttk.Entry(mainframe, width=10)
# # entry_number.grid(column=1, row=0, padx=5, pady=5)

# # # Calculate Button
# # calculate_button = ttk.Button(mainframe, text="Calculate", command=calculate_square)
# # calculate_button.grid(column=2, row=0, padx=5, pady=5)

# # # Result Label
# # result_label = ttk.Label(mainframe, text="Square: ")
# # result_label.grid(column=0, row=1, columnspan=3, padx=5, pady=5)

# # # Configure grid weights
# # mainframe.columnconfigure(1, weight=1)  # Column with entry box to expand with window resize

# # # Set focus on entry field
# # entry_number.focus()

# # root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# def calculate_square():
#     try:
#         number = float(entry_number.get())
#         square = number ** 2
#         result_label.config(text=f"Square: {square}")
#     except ValueError:
#         result_label.config(text="Please enter a valid number")

# # Create main window
# root = tk.Tk()
# root.title("Square Calculator")
# root.geometry("300x150")
# root.resizable(False, False)  # Disable resizing

# # Create style for widgets
# style = ttk.Style()
# style.configure("TFrame", background="#f0f0f0")  # Light gray background
# style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white")  # Green button
# style.configure("TLabel", padding=5, background="#f0f0f0")  # Light gray background

# # Create main frame
# mainframe = ttk.Frame(root, style="TFrame")
# mainframe.pack(padx=10, pady=10, fill="both", expand=True)

# # Number entry and label
# ttk.Label(mainframe, text="Enter a number:", style="TLabel").grid(column=0, row=0, padx=5, pady=5)
# entry_number = ttk.Entry(mainframe, width=10)
# entry_number.grid(column=1, row=0, padx=5, pady=5)

# # Calculate button
# calculate_button = ttk.Button(mainframe, text="Calculate", command=calculate_square, style="TButton")
# calculate_button.grid(column=2, row=0, padx=5, pady=5)

# # Result label
# result_label = ttk.Label(mainframe, text="Square: ", style="TLabel")
# result_label.grid(column=0, row=1, columnspan=3, padx=5, pady=5)

# # Set focus to entry widget
# entry_number.focus()

# # Start the main loop
# root.mainloop()


### create a program that calculate  ROI calculator
### Return on investment
### for  Example: 10,000 
### investment = 10000
### income = 100000
### profit ?


investment = 10000
income = 100000
profit = income - investment
roi = (profit / investment) * 100
print(f"The ROI is {roi}%")

