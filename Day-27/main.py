from tkinter import *


def convert_miles_to_km():
    miles = float(miles_input.get())
    km = 1.60934 * miles
    label2.config(text=f"   {km}   ")


window = Tk()
window.title("Miles to Kilo")
window.config(padx=20,pady=20)

miles_input = Entry(width=10)
# miles_input.config(padx=200,pady=200)
miles_input.grid(row=0, column=1)

miles_label = Label(text="miles")
miles_label.grid(row=0, column=2)
km_value = 0.0
label1 = Label(text=f"is equal to")
label1.grid(row=1, column=0)

label2 = Label(text=f"{km_value}")
label2.grid(row=1, column=1)

label3 = Label(text=f"Km")
label3.grid(row=1, column=2)


calc_button = Button(text="Calculate",command=convert_miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()
