# To compile into an executable type 'pyinstaller --onefile --windowed -i your_icon.ico SortingScript.py' in the terminal
# tkinter is the module that I'm using for the GUI.
import tkinter as tk
from tkinter import filedialog, messagebox
# The re module is just being used to search through the txt file to find the RFID IDD
import re
# The os module is to interact with the operating system so you can interact with the file directory
import os
import time

# Predefined directory path: This will change depending on user/computer
directory_path = "/Users/..."


def latest_opened_file():
    """This function resets the most recent file, scans the current directory path, looks for the most recently
    modified txt file, and returns that most recently modified file."""
    most_recent_file = None
    most_recent_time = 0

    for entry in os.scandir(directory_path):
        if entry.is_file() and entry.name.endswith('.txt'):
            mod_time = entry.stat().st_mtime_ns
            if mod_time > most_recent_time:
                most_recent_file = entry.path
                most_recent_time = mod_time

    return most_recent_file


def count():
    """This function increments a button by 7 every time it is pressed to help with total part count since parts are
    packaged in quantities of 7."""
    global current_count
    bag_quantity = 7
    current_count += bag_quantity
    count_button.config(text=f"{current_count}")  # Update the button text
    if current_count == 504:
        count_button.config(bg="#32CD32", fg="white")
    elif current_count > 504:
        count_button.config(bg="red", fg="white")


def extract_ids_to_new_file(input_filename, output_filename):
    """This function reads the txt file that was output by the ... software and finds the unique IDDs.
       Following that, the program will write those IDDs into a new file with the Box ID. Lastly, it shows
       a message box stating how many unique IDs are in the file. There is also some error handling if no file
       is found or you have issues reading/writing the file."""
    unique_ids = set()

    try:
        # Ensure file exists before processing
        if not os.path.exists(input_filename):
            messagebox.showerror("Error", f"The file {input_filename} was not found.")
            return

        # Read and extract unique IDs
        with open(input_filename, 'r') as infile:
            for line in infile:
                match = re.search(r"IDD='([A-Z0-9]{16})'", line)
                if match:
                    unique_id = match.group(1)
                    unique_ids.add(unique_id)

        # Write the unique IDs to a new file (one folder up)
        output_path = os.path.join(os.path.dirname(directory_path), output_filename)
        with open(output_path, 'w') as outfile:
            for unique_id in unique_ids:
                outfile.write(f"{unique_id}\n")

        # Notify the user about the results
        if len(unique_ids) == 504:
            messagebox.showinfo("Result", "There are 504 unique IDs in the file.")
        else:
            messagebox.showinfo("Result", f"There are {len(unique_ids)} unique IDs in the file.")

        # Wait a short time before deleting to avoid file locks
        time.sleep(1)

        # Delete the original file after successfully extracting data. This is important because if the other file is
        # not deleted than the ... program will not generate a new .txt file and the IDDs will compound instead of
        # being reset.
        os.remove(input_filename)
        print(f"Deleted original file: {input_filename}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file {input_filename} was not found.")
    except PermissionError:
        messagebox.showerror("Error", f"Permission denied: Unable to delete {input_filename}. Ensure it's not in use.")
    except IOError:
        messagebox.showerror("Error", f"An error occurred while reading or writing the file.")


def validate_input(char):
    """This function checks to make sure the user enters and integer value"""
    return char.isdigit()


def scan_box():
    """This function asks the user to input a Box ID and then asks the user if they want to use the most recently
    modified file. If they do it will continue, if they do not it will open up file explorer for them to select
    a different file. It then creates the name of the output file. There is some error handling for if no box
     ID is entered or if there is no valid file in the directory."""
    recent_file = latest_opened_file()

    box_num = box_entry.get()
    global current_count
    current_count = 0
    count_button.config(text=f"{current_count}", bg="white", fg="black")

    if not box_num:
        messagebox.showerror("Error", "Please enter a Box ID.")
        return

    if recent_file:
        file_choice = messagebox.askyesno("Confirm", f"Would you like to open the most recent file?\n{recent_file}")
        if not file_choice:
            recent_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if not recent_file:
                return

        output_filename = f"Box{box_num}.txt"
        extract_ids_to_new_file(recent_file, output_filename)
        box_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "No valid files found in the directory.")


current_count = 0
# This section creates the GUI
app = tk.Tk()
app.title("Box Scanner")
app.geometry("650x500")
app.configure(bg="#f0f8ff")
# "#f0f8ff"
header_label = tk.Label(app, text="Box Scanner", font=("Helvetica", 28, "bold"), bg="#4682B4", fg="white", pady=20)
header_label.pack(fill="x")

frame = tk.Frame(app, bg="#f0f8ff")
frame.pack(expand=True)

validate_command = app.register(validate_input)

tk.Label(frame, text="Box ID:", bg="#f0f8ff", font=("Helvetica", 18)).pack(pady=10)
box_entry = tk.Entry(frame, width=25, font=("Helvetica", 18), validate="key", validatecommand=(validate_command, '%S'))
box_entry.pack(pady=10)

scan_button = tk.Button(frame, text="Scan Box", command=scan_box, bg="#32CD32", fg="white", font=("Helvetica", 18),
                        padx=20, pady=10)
scan_button.pack(pady=20)

count_button = tk.Button(frame, text=f"{current_count}", command=count, bg="white", fg="black", font=("Helvetica", 18),
                         padx=20, pady=10)
count_button.pack(pady=20)

app.mainloop()
