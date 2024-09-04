# promodo technique building with tkinter


from tkinter import *



window = Tk();

window.title("Pomodoro")
window.config(bg="white")
canvas = Canvas(window,width=512 ,height=512,bg="white",highlightthickness=0)
img = PhotoImage(file='unnamed.png')
canvas.create_image(240,200,image=img)
canvas.create_text(240,240,text='00:00',fill="white" ,font=('Courier',35,"bold"))

canvas.pack()

window.mainloop()