import unittest
import math

def convolution_1d(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    output_length = signal_length - kernel_length + 1
    output = [0] * output_length
    for i in range(output_length):
        for j in range(kernel_length):
            if 0 <= i - j < signal_length:
                output[i] += signal[i + j] * kernel[j]
    return output

class TestSignalProcessing(unittest.TestCase):
    def test_convolution_1d_with_known_kernel(self):
       
        signal = [1, 2, 3, 4, 5]
        kernel = [1, 0, 1]
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [2, 4, 6, 8])

        signal = [1, 2, 3, 4, 5]
        kernel = [1, -1, 1]
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [1, 1, 2, 3])

    def test_convolution_1d_with_custom_kernel(self):
        signal = [1, 2, 3, 4, 5]
        kernel = [2, -2, 2]
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [2, 2, 2, 2])

        signal = [1, 2, 3, 4, 5]
        kernel = [0.5, 0.5]
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [1.5, 2.5, 3.5, 4.5])

    def test_convolution_1d_with_empty_signal(self):
    
        signal = []
        kernel = [1, 0, 1]
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [])

    def test_convolution_1d_with_empty_kernel(self):

        signal = [1, 2, 3, 4, 5]
        kernel = []
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [])

    def test_convolution_1d_with_signal_shorter_than_kernel(self):
    
        signal = [1, 2, 3]
        kernel = [1, 0, 1, 0, 1]
        result = convolution_1d(signal, kernel)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
