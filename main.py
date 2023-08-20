import tkinter as tk
from tkinter import messagebox as msg
import def_functions as func # Import the def_functions script as func. Program will not work without it.

func.connect() # Run the connect function from func.

index = None
entry_provider = None

def clear(): # Clear the contents of the following text entries.
    search_entry.delete(0, tk.END)
    app_entry.delete(0, tk.END)
    url_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    psswd_entry.delete(0, tk.END)

def generate(): # Run the gen_pass function from func which returns a random password and insert it into psswd_entry.
    password = func.gen_pass()
    psswd_entry.delete(0, tk.END)
    psswd_entry.insert(0, password)

def add(): # Run the insert function from func with the contents of the text entries as args.
    app = app_entry.get()
    url = url_entry.get()
    user = user_entry.get()
    psswd = psswd_entry.get()
    clear()
    func.insert(app, url, user, psswd)

def delete(): # Run the delete function from func with the content of app_name as arg.
    app_name = app_entry.get()
    func.delete(app_name)
    clear()

def display_result(button="next"): # Display the results returned by the entry_provider class in the text entries. button="next" means if a positional argument isn't provided it will set it as "next".
    if len(app_entry.get()) == 0 and button == "next": # Make sure the Next Result button wasn't pressed without a search being performed.
        pass
    else:
        search_results = entry_provider.get_next_entry()
        app, url, user, psswd = search_results
        clear()
        app_entry.insert(0, app)
        url_entry.insert(0, url)
        user_entry.insert(0, user)
        psswd_entry.insert(0, psswd)

class EntryProvider: # Return one entry from the list of possible multiple entries. Return the next entry on each call and start over once the end is reached.
    def __init__(self, entries):
        self.entries = entries
        self.current_index = 0
    
    def get_next_entry(self):
        if not self.entries:
            return None
        entry = self.entries[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.entries)
        return entry

def search(): # Run the search function from func with the contents of search_entry as an arg. Then run the display_result function.
    term = search_entry.get()
    global index, entry_provider
    index = func.search(term)
    if not index:
        msg.showerror("Error", "Results not found.")
    else:
        entry_provider = EntryProvider(index)
        display_result("search")

# Innitialize the GUI window.
root = tk.Tk()
root.title("Pass It")
root.iconbitmap('logo.ico') # If you are having problems with this line when running in Linux it can be commented out. It only sets the app icon.

# Define each label.
app_label = tk.Label(root, text="App:")
url_label = tk.Label(root, text="Url:")
user_label = tk.Label(root, text="Username:")
psswd_label = tk.Label(root, text="Password:")

# Define each text entry.
search_entry = tk.Entry(root)
app_entry = tk.Entry(root)
url_entry = tk.Entry(root)
user_entry = tk.Entry(root)
psswd_entry = tk.Entry(root)

# Define each button.
search_button = tk.Button(root, text="Search", command=search)
next_button = tk.Button(root, text="Next Result", command=display_result)
clear_button = tk.Button(root, text="Clear", command=clear)
add_button = tk.Button(root, text="Add", command=add)
delete_button = tk.Button(root, text="Delete", command=delete)
psswd_button = tk.Button(root, text="Generate", command=generate)

# Define blank frame.
blank_frame = tk.Frame(root, height=15)

# Configure the resizing behavior of the rows and columns.
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

# Configure each entry, label, and button in a gridview by rows and columns.
search_entry.grid(row=0, column=1, padx=10, pady=6, sticky="nsew")
search_button.grid(row=0, column=2, padx=10, pady=3, sticky="nsew")
next_button.grid(row=0, column=3, padx=10, pady=3, sticky="nsew")
blank_frame.grid(row=1, column=0)
app_label.grid(row=2, column=0)
url_label.grid(row=2, column=1)
user_label.grid(row=2, column=2)
psswd_label.grid(row=2, column=3)
app_entry.grid(row=3, column=0, padx=10, pady=3, sticky="nsew")
url_entry.grid(row=3, column=1, padx=10, pady=3, sticky="nsew")
user_entry.grid(row=3, column=2, padx=10, pady=3, sticky="nsew")
psswd_entry.grid(row=3, column=3, padx=10, pady=3, sticky="nsew")
clear_button.grid(row=4, column=0, padx=10, pady=3, sticky="nsew")
add_button.grid(row=4, column=1, padx=10, pady=3, sticky="nsew")
delete_button.grid(row=4, column=2, padx=10, pady=3, sticky="nsew")
psswd_button.grid(row=4, column=3, padx=10, pady=3, sticky="nsew")

# Start the GUI window.
root.mainloop()