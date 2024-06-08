
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

sig_input=input()
signal=[float(i) for i in sig_input.split()]


kernel_low_freq = [1, 0, 1]
kernel_high_freq = [1, -1, 1]

low_frq=convolution_1d(signal, kernel_high_freq)    
high_frq=convolution_1d(signal, kernel_low_freq)

print("Recovered Low Frequency Signal=", low_frq)
print("Recovered High Frequency Signal=", high_frq)