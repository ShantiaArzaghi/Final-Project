import math
import matplotlib.pyplot as pl

def convolution_1d(signal, kernel):
 
    signal_length = len(signal)
    kernel_length = len(kernel)
    
    output_length = signal_length - kernel_length + 1
    
   
    output = [0] * output_length
    
    
    for i in range(output_length):
        for j in range(kernel_length):
            if 0<=i-j<signal_length:
              output[i] += signal[i+j] * kernel[j]
             
         
    return output
signal=[]
for i in range(1, 1001):
    signal.append(math.sin(2*math.pi*0.1*i/100)+math.sin(2*math.pi*0.01*i/100))


kernel_low_freq = [1,0,1]
kernel_high_freq = [1,-1,1]

low_frq=convolution_1d(signal, kernel_high_freq)    
high_frq=convolution_1d(signal, kernel_low_freq)


print("Recovered Low Frequency Signal=", low_frq)
print("Recovered High Frequency Signal=", high_frq)
pl.plot(low_frq)
pl.plot(high_frq)
pl.show()