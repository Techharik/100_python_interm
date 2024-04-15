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

def add(**kwargs):
    for key, value in kwargs.items():
        print(key)
          


add(add=3,sub=4)


import tkinter as tk

window = tk.Tk()


window.title("First GUI Program");
window.minsize(width=500,height=300)



my_lable = tk.Label(text='I am a robot',font=('Arial',34,"bold"))
my_lable.pack() # pack is important to show







window.mainloop()