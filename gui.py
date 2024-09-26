import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Dropdown and Date Input")

# Define a list of options for the drop-downs
options1 = ["Option 1-1", "Option 1-2", "Option 1-3"]
options2 = ["Option 2-1", "Option 2-2", "Option 2-3"]
options3 = ["Option 3-1", "Option 3-2", "Option 3-3"]
options4 = ["Option 4-1", "Option 4-2", "Option 4-3"]

# Create combo boxes (dropdowns)
combo1 = ttk.Combobox(root, values=options1)
combo2 = ttk.Combobox(root, values=options2)
combo3 = ttk.Combobox(root, values=options3)
combo4 = ttk.Combobox(root, values=options4)

# Set default values for combo boxes
combo1.set("Select option 1")
combo2.set("Select option 2")
combo3.set("Select option 3")
combo4.set("Select option 4")

# Pack the combo boxes into the window
combo1.pack(pady=5)
combo2.pack(pady=5)
combo3.pack(pady=5)
combo4.pack(pady=5)

# Create labels and entries for the date inputs
label_start_date = tk.Label(root, text="Enter start date (YYYY-MM-DD):")
label_start_date.pack(pady=5)
start_date_entry = tk.Entry(root)
start_date_entry.pack(pady=5)

label_end_date = tk.Label(root, text="Enter end date (YYYY-MM-DD):")
label_end_date.pack(pady=5)
end_date_entry = tk.Entry(root)
end_date_entry.pack(pady=5)

# Function to validate and print the inputs
def submit_inputs():
    # Get the selections and dates
    selected1 = combo1.get()
    selected2 = combo2.get()
    selected3 = combo3.get()
    selected4 = combo4.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    # Basic validation of inputs
    if "Select" in [selected1, selected2, selected3, selected4]:
        messagebox.showerror("Input Error", "Please make selections for all dropdowns.")
        return
    
    # Validate date format (YYYY-MM-DD)
    try:
        import datetime
        datetime.datetime.strptime(start_date, "%Y-%m-%d")
        datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid dates in YYYY-MM-DD format.")
        return
    
    # Use the inputs (Here, it's printed, but you can pass these to your script)
    print(f"Selections: {selected1}, {selected2}, {selected3}, {selected4}")
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    
    # Here you can call your script and pass the values
    # Example: your_script(selected1, selected2, selected3, selected4, start_date, end_date)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_inputs)
submit_button.pack(pady=10)

# Start the tkinter event loop
root.mainloop()