# plot_wave_file.py modified for exercise 12
# # filter_16.py
#% guitar_demo.m

from random import random
import pyaudio
import struct
from matplotlib import pyplot
from myfunctions import clip16

# Karplus-Strong paramters
K = 0.99;
Fs = 8000
f = 60
N = Fs/f
T = 2.0
b = 1;
RATE = 44000


p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = False,
                output      = True )


randomvalues = [random() - 1 for i in range(int(f*4))] #values to 60, like a variable 
chart=[]
fig = pyplot.figure(1)
#pyplot.ylim(-60, 60)
p#yplot.xlim(0, 100)

for i in range(Fs*8):
    k=i+1
    input_value = abs(randomvalues[i])
    chart.append(input_value)
    output_value = K * (b/T)*(input_value + randomvalues[k]) #Karplus-Strong method
    randomvalues.append(output_value)
    output_string = struct.pack('h', int(clip16(output_value*32000))) 
    stream.write(output_string) #playing sound

 #circular buffer
    k = k + 1
    if k >= len(randomvalues):
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0
  
pyplot.plot(chart)
pyplot.show() #chart
pyplot.draw()