from tkinter import *


def button_clicked():
    new_text = float(input.get())*1.609344
    display_label.config(text=new_text,font=("Arial", 24, "bold"))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Button
calculate_button = Button(text="Calculate",font=("Arial", 24, "bold"), command=button_clicked)
calculate_button.grid(column=1, row=2)


# Entry
input = Entry(width=10,font=("Arial", 24, "bold"))
entry = input.get()
input.grid(column=1, row=0)

# Labels
is_equal_to_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

Km_label = Label(text="Km", font=("Arial", 24, "bold"))
Km_label.grid(column=3, row=1)

display_label = Label(text="0", font=("Arial", 24, "bold"))
display_label.grid(column=1, row=1)

window.mainloop()