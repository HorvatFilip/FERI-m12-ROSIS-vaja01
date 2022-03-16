from tkinter import * 
from tkinter import filedialog
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from tkinter.messagebox import showinfo

def OpenFile():
    filetypes = (
        ('audio files', '*.wav'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilenames(
        title='Open wav file',
        initialdir='./',
        filetypes=filetypes
    )
    fs, data = wavfile.read(filename[0])
    duration = len(data)/fs
    t = np.arange(0, duration, 1/fs)
    
    fig.add_subplot(111).plot(t,data)
    
    canvas.draw()
  
    canvas.get_tk_widget().pack()
  
    toolbar.update()

    canvas.get_tk_widget().pack()

main_window = Tk()  
main_window.title('Plotting in Tkinter')
main_window.geometry("500x500")


fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig,master=main_window)  

toolbar = NavigationToolbar2Tk(canvas,main_window)

open_button = Button(master = main_window, 
                     command = OpenFile,
                     height = 2, 
                     width = 10,
                     text = "Open")

open_button.pack()
  
main_window.mainloop()