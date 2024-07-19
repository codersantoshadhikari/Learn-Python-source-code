import tkinter as tk
from tkinter import ttk

def calculate_roi():
    try:
        investment = float(entry_investment.get())
        income = float(entry_income.get())
        
        profit = income - investment
        roi_percentage = (profit / investment) * 100
        
        result_label.config(text=f"Profit: ${profit:.2f}\nROI: {roi_percentage:.2f}%")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


root = tk.Tk()
root.title("ROI Calculator")
root.geometry("300x200")
root.resizable(False, False)  


style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")  # Light gray background
style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white")  # Green button
style.configure("TLabel", padding=5, background="#f0f0f0")  # Light gray background

# Create main frame
mainframe = ttk.Frame(root, style="TFrame")
mainframe.pack(padx=10, pady=10, fill="both", expand=True)

# Investment entry and label
ttk.Label(mainframe, text="Enter investment:", style="TLabel").grid(column=0, row=0, padx=5, pady=5)
entry_investment = ttk.Entry(mainframe, width=10)
entry_investment.grid(column=1, row=0, padx=5, pady=5)

# Income entry and label
ttk.Label(mainframe, text="Enter income:", style="TLabel").grid(column=0, row=1, padx=5, pady=5)
entry_income = ttk.Entry(mainframe, width=10)
entry_income.grid(column=1, row=1, padx=5, pady=5)

# Calculate button
calculate_button = ttk.Button(mainframe, text="Calculate ROI", command=calculate_roi, style="TButton")
calculate_button.grid(column=0, row=2, columnspan=2, padx=5, pady=10)

# Result label
result_label = ttk.Label(mainframe, text="", style="TLabel")
result_label.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

# Set focus to investment entry widget
entry_investment.focus()

# Start the main loop
root.mainloop()
