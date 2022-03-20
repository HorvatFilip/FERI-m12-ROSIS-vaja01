from multiprocessing.context import SpawnContext
from tkinter import Tk, Button, filedialog, Frame
from scipy.io import wavfile
from scipy.fftpack import fft
from scipy import signal
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, 
    NavigationToolbar2Tk
)


class Window():
    def __init__(self):
        self.main_window = Tk()  
        self.main_window.title('Plotting in Tkinter')
        self.main_window.geometry("1100x1000")

        self.fig1 = Figure(figsize = (5,4), dpi=100)
        self.fig2 = Figure(figsize = (5,4), dpi=100)
        self.fig3 = Figure(figsize = (5,4), dpi=100)


        self.canvas1 = FigureCanvasTkAgg(self.fig1,master=self.main_window) 
        self.toolbar_frame1 = Frame(master=self.main_window)
        self.toolbar1 = ''

        self.canvas2 = FigureCanvasTkAgg(self.fig2,master=self.main_window) 
        self.toolbar_frame2 = Frame(master=self.main_window)
        self.toolbar2 = ''

        self.canvas3 = FigureCanvasTkAgg(self.fig3,master=self.main_window) 
        self.toolbar_frame3 = Frame(master=self.main_window)
        self.toolbar3 = ''
       
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
            title = filename[0].split('/')
            
            #
            # SIGNAL
            #
            fs, samples = wavfile.read(filename[0])
            duration = len(samples)/fs
            t = np.arange(0, duration, 1/fs)
           
            self.fig1.clf()
            self.fig_axis1 = self.fig1.add_subplot(111)
            self.fig_axis1.set_title(title[-1])
            self.fig_axis1.set_xlabel("Cas [s]")
            self.fig_axis1.set_ylabel("Amplituda")
            self.fig_axis1.plot(t,samples)
            self.fig1.tight_layout()
           
            self.canvas1.draw()
            self.canvas1.get_tk_widget().grid(row=1, column=0)
            self.toolbar_frame1.grid(row=2, column=0)
            if not self.toolbar1:
                self.toolbar1 = NavigationToolbar2Tk(self.canvas1,self.toolbar_frame1)
            self.toolbar1.update()
            self.canvas1.get_tk_widget().grid(row=1, column=0)


            #
            # DFT
            #
            data_channel = samples.T[0]
            data_fft = fft(data_channel)
            data_fft_len = len(data_fft)//2

            self.fig2.clf()
            self.fig_axis2 = self.fig2.add_subplot(111)
            self.fig_axis2.set_title(title[-1])
            self.fig_axis2.set_xlabel("Frekvenca [Hz]")
            self.fig_axis2.set_ylabel("Amplituda")
            self.fig_axis2.plot(abs(data_fft[:(data_fft_len-1)]))
            self.fig2.tight_layout()
           
            self.canvas2.draw()
            self.canvas2.get_tk_widget().grid(row=1, column=1)
            self.toolbar_frame2.grid(row=2, column=1)
            if not self.toolbar2:
                self.toolbar2 = NavigationToolbar2Tk(self.canvas2,self.toolbar_frame2)
            self.toolbar2.update()
            self.canvas2.get_tk_widget().grid(row=1, column=1)


            #
            # KRATKO ČASOVNA FOURIEROVA TRANS
            #
            freq, t, spectogram = signal.spectrogram(samples.T[0], fs)

            self.fig3.clf()
            self.fig_axis3 = self.fig3.add_subplot(111)
            self.fig_axis3.set_title(title[-1])
            self.fig_axis3.set_xlabel("Cas [s]")
            self.fig_axis3.set_ylabel("Frekvenca [Hz]")
            self.fig_axis3.specgram(samples.T[0], NFFT=1024, Fs=fs)
            self.fig3.tight_layout()
           
            self.canvas3.draw()
            self.canvas3.get_tk_widget().grid(row=3, column=0)
            self.toolbar_frame3.grid(row=4, column=0)
            if not self.toolbar3:
                self.toolbar3 = NavigationToolbar2Tk(self.canvas3,self.toolbar_frame3)
            self.toolbar3.update()
            self.canvas3.get_tk_widget().grid(row=3, column=0)
            

    def Close(self):
        self.main_window.destroy()
  

app = Window()