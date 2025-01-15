import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store canned responses
DATA_FILE = "responses.json"

# Load responses from file
def load_responses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save responses to file
def save_responses(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add a new response
def add_response():
    key = simpledialog.askstring("Add Response", "Enter a unique key for the response:")
    if not key:
        return
    if key in responses:
        messagebox.showerror("Error", "Key already exists!")
        return
    response = simpledialog.askstring("Add Response", "Enter the canned response text:")
    if response:
        responses[key] = response
        save_responses(responses)
        update_listbox()

# Edit an existing response
def edit_response():
    key = listbox.get(tk.ACTIVE)
    if not key:
        messagebox.showerror("Error", "No response selected!")
        return
    new_response = simpledialog.askstring("Edit Response", "Edit the response text:", initialvalue=responses[key])
    if new_response:
        responses[key] = new_response
        save_responses(responses)
        update_listbox()

# Delete a response
def delete_response():
    key = listbox.get(tk.ACTIVE)
    if not key:
        messagebox.showerror("Error", "No response selected!")
        return
    if messagebox.askyesno("Delete Response", f"Are you sure you want to delete '{key}'?"):
        del responses[key]
        save_responses(responses)
        update_listbox()

# Copy response to clipboard
def copy_response():
    key = listbox.get(tk.ACTIVE)
    if not key:
        messagebox.showerror("Error", "No response selected!")
        return
    response = responses[key]
    root.clipboard_clear()
    root.clipboard_append(response)
    root.update()
    messagebox.showinfo("Copied", "Response copied to clipboard!")

# Update the listbox with current responses
def update_listbox():
    listbox.delete(0, tk.END)
    for key in responses:
        listbox.insert(tk.END, key)

# Minimize the window
def minimize_window():
    root.iconify()

# Maximize the window
def maximize_window():
    root.state('zoomed')

# Main application window
root = tk.Tk()
root.title("Canned Response Manager")

# Menu bar for window control
menu_bar = tk.Menu(root)
window_menu = tk.Menu(menu_bar, tearoff=0)
window_menu.add_command(label="Minimize", command=minimize_window)
window_menu.add_command(label="Maximize", command=maximize_window)
window_menu.add_command(label="Close", command=root.quit)
menu_bar.add_cascade(label="Window", menu=window_menu)
root.config(menu=menu_bar)

# Load existing responses
responses = load_responses()

# UI Elements
frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT, padx=5)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", command=add_response).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit", command=edit_response).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", command=delete_response).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Copy", command=copy_response).grid(row=0, column=3, padx=5)

# Populate listbox
update_listbox()

# Run the application
root.mainloop()
