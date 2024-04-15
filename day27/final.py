from tkinter import *



window = Tk()
window.title('Mile to km convertor')
window.minsize(width=500,height=500)
my_label  = Label(text='Mile to KiloMeter')
my_label.grid(column=2, row=0)

input = Entry()
input.grid(column=2,row =1);



def km():
    mile = input.get()
    km = float(mile) * 1.609
    result_label['text'] = f'Miles is equal to {km} km'

result_label = Label(text='Miles is equal to 0 km')
result_label.grid(column=1,row=3)

button= Button(text='Calculate' , command=km)
button.grid(column=2,row=4)
    





window.mainloop()