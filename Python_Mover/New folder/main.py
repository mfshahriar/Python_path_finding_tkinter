import tkinter
from Snake import Snake
_root_window = tkinter.Tk()
_root_window.title('Snake')
_root_window.resizable(False, False)

borad = Snake()
borad.pack()

_root_window.mainloop()