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


# text label
my_lable = Label(text='I am a robot',font=('Arial',34,"bold"))
my_lable.pack() # pack is important to show




# entry
input = Entry(width=15)
input.pack()
 
def button_clicked():
    resut_input = input.get()
    my_lable['text']=resut_input

# button
button = Button(text='Click Me',command=button_clicked)
button.pack()


window.mainloop()