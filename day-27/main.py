from tkinter import *

#
# def change_label():
#     label_name['text'] = input.get()


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=16, pady=16)


def convert():
    mile = input.get()
    result = int(mile) * 1.609
    label_result['text'] = str(round(result))


input = Entry()
input.grid(column=1, row=0)

label_miles = Label()
label_miles.config(text="Miles")
label_miles.grid(column=2, row=0)

label_is_equal_to = Label()
label_is_equal_to.config(text="Is equal to")
label_is_equal_to.grid(column=0, row=1)

label_result = Label()
label_result.config(text="0")
label_result.grid(column=1, row=1)

label_km = Label()
label_km.config(text="Km")
label_km.grid(column=2, row=1)

button = Button()
button.config(text="Calculate", command=convert)
button.grid(column=1, row=2)




window.mainloop()
