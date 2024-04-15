#GUI work with tkinker.

# ? * unlimited arguments

# def add(*args):
# #   args gives as a tupple
#   count = 0
#   for n in args:
#      count = count+n
#   return count

# result = add(1,23,4)
# print(result)

# ? ** kwargs

# we can pass a keyword argument and it returns  a dictionary.add()

# def add(**kwargs):
#     for key, value in kwargs.items():
#         print(key,value) 
# add(add=3,sub=4)


from tkinter import *

window = Tk()


window.title("First GUI Program");
window.minsize(width=500,height=300)


#label
my_lable = Label(text='I am a robot',font=('Arial',24,"bold"))
# my_lable.pack() # pack is important to show
# instead of pack we can use place
# my_lable.place(x=0,y=10) x and y axis view.
# Grid layout manger. example

my_lable.grid(column=0, row=0)


# entry
input = Entry(width=15)
input.grid(column=3, row=2)
 
def button_clicked():
    resut_input = input.get()
    my_lable['text']=resut_input

# button

button = Button(text='Click Me',command=button_clicked)
button.grid(column=1,row=1);

button = Button(text='Click Me',command=button_clicked)
button.grid(column=2,row=0);



#  text spinbox scale checkbox radion button listbox.



window.mainloop()



# summary
# tkinter is a GUI app where wwe can use to build GUI and event interaction.

# core components in GUI is (lable, entry, text, spinbox, scale, button, checkbox, radio, list)

#layout or of 3 types pack, place , grid 