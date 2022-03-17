from tkinter import Tk, Button, Label, filedialog
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from tkinter.messagebox import showinfo, askokcancel
  
class Window():
    def __init__(self):
        self.main_window = Tk()  
        self.main_window.title('Plotting in Tkinter')
        self.main_window.geometry("500x500")

        self.fig, self.fig_axis = plt.subplots(figsize = (5,4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig,master=self.main_window)  

        self.toolbar = NavigationToolbar2Tk(self.canvas,self.main_window)

        self.open_button = Button(master = self.main_window, 
                             command = self.OpenFile,
                             height = 2, 
                             width = 10,
                             text = "Open")

        self.open_button.pack()


        self.main_window.protocol("WM_DELETE_WINDOW", self.CloseApp)
        self.main_window.mainloop()

        def OpenFile(self):
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

            self.fig_axis.set_title(filename[0])
            self.fig_axis.set_ylabel('Amplitude')
            self.fig_axis.set_xlabel('Time [s]')
            plt.clf()
            plt.plot(t,data)

            
            self.canvas.draw()
        
            self.canvas.get_tk_widget().pack()
        
            self.toolbar.update()

            self.canvas.get_tk_widget().pack()

        def CloseApp(self):
            if askokcancel("Quit", "Do you want to quit?"):
                self.main_window.destroy()

win = Window()