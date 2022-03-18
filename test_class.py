from tkinter import Tk, Button, filedialog
from scipy.io import wavfile
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, 
    NavigationToolbar2Tk
)
# Class for tkinter window
  
  
class Window():
    def __init__(self):
  
        # Creating the tkinter Window
        self.main_window = Tk()  
        self.main_window.title('Plotting in Tkinter')
        self.main_window.geometry("700x600")

        fig, self.fig_axis = plt.subplots(figsize = (5,4), dpi=100)    

        
        self.canvas = FigureCanvasTkAgg(fig,master=self.main_window)  
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.main_window)

        self.open_button = Button(master = self.main_window, 
                             command = self.OpenFile,
                             height = 2, 
                             width = 10,
                             text = "Open")

        self.open_button.pack()
  
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
            if not filename:
                return
            fs, data = wavfile.read(filename[0])
            duration = len(data)/fs
            t = np.arange(0, duration, 1/fs)

           
            plt.clf()
            title = filename[0].split('/')
            plt.title(title[-1])
            plt.xlabel("Cas [s]")
            plt.ylabel("Amplituda")
            plt.plot(t,data)

           
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()
        
            self.toolbar.update()

            self.canvas.get_tk_widget().pack()
            
            plt.tight_layout()
            
            

    def Close(self):
        #plt.close(self.fig)
        self.main_window.destroy()
  
  
# Running test window
test = Window()