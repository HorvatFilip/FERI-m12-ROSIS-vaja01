from tkinter import Tk, Button, filedialog, Frame
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
        self.main_window.geometry("1100x600")

        fig1, self.fig_axis1 = plt.subplots(figsize = (5,4), dpi=100)    
        fig2, self.fig_axis2 = plt.subplots(figsize = (5,4), dpi=100)    

        self.canvas1 = FigureCanvasTkAgg(fig1,master=self.main_window) 
        self.toolbar_frame1 = Frame(master=self.main_window)
        self.toolbar1 = ''

        self.canvas2 = FigureCanvasTkAgg(fig2,master=self.main_window)  
        self.toolbar_frame2 = Frame(master=self.main_window)
        self.toolbar2 = ''

        self.open_button = Button(master = self.main_window, 
                             command = self.OpenFile,
                             height = 2, 
                             width = 10,
                             text = "Open")

        self.open_button.grid(column=0, row=0)
  
        self.main_window.mainloop()
  
    def OpenFile(self):
            filetypes = (
                ('audio files', '*.wav'),
                ('All files', '*.*')
            )
            filename = filedialog.askopenfilenames(
                title='Open wav file',
                initialdir='./audiofiles/',
                filetypes=filetypes
            )
            if not filename:
                return
            fs1, data1 = wavfile.read(filename[0])
            duration1 = len(data1)/fs1
            t1 = np.arange(0, duration1, 1/fs1)

           
            self.fig_axis1 = plt.clf()
            title = filename[0].split('/')
            self.fig_axis1 = plt.title(title[-1])
            self.fig_axis1 = plt.xlabel("Cas [s]")
            self.fig_axis1 = plt.ylabel("Amplituda")
            self.fig_axis1.plot(t1,data1)

           
            self.canvas1.draw()
            self.canvas1.get_tk_widget().grid(row=1, column=0)
            
            self.toolbar_frame1.grid(row=2, column=0)
            if not self.toolbar1:
                self.toolbar1 = NavigationToolbar2Tk(self.canvas1,self.toolbar_frame1)
            self.toolbar1.update()

            self.canvas1.get_tk_widget().grid(row=1, column=0)
            

            fs, data = wavfile.read(filename[0])
            duration = len(data)/fs
            t = np.arange(0, duration, 1/fs)

            self.fig_axis2 = plt.clf()
            title = filename[0].split('/')
            self.fig_axis2 = plt.title(title[-1])
            self.fig_axis2 = plt.xlabel("Cas [s]")
            self.fig_axis2 = plt.ylabel("Amplituda")
            self.fig_axis2 = plt.plot(t,data)

           
            self.canvas2.draw()
            self.canvas2.get_tk_widget().grid(row=1, column=1)
            self.toolbar_frame2.grid(row=2, column=1)
            if not self.toolbar2:
                self.toolbar2 = NavigationToolbar2Tk(self.canvas2,self.toolbar_frame2)
            self.toolbar2.update()

            self.canvas2.get_tk_widget().grid(row=1, column=1)
            
            self.fig_axis2 = plt.tight_layout()



    def Close(self):
        #plt.close(self.fig)
        self.main_window.destroy()
  
  
# Running test window
test = Window()