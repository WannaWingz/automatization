from tkinter import *
from tkinter.tix import StdButtonBox

root = Tk()
def lyalya():
    info['text'] = 'laylay'

root['bg'] = '#fafafa'
root.title('<3')
root.geometry('600x600')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)

frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)


# btn = Button(frame_top, text='Посмотреть погоду', command=lyalya)
# btn.pack()

info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()
# btn = StdButtonBox(frame_top, text='Посмотреть погоду', command=lyalya)
# btn.pack()



if __name__ == '__main__':
    root.mainloop()
