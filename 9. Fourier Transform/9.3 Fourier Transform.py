import numpy as np
import matplotlib.pyplot as plt

def fourier_transform(x):
    """
    Calculates the Fourier transform of the signal x.

    Args:
        x: The signal to be transformed.

    Returns:
        The Fourier transform of x.
    """

    N = len(x)
    y = np.fft.fft(x)
    f = np.fft.fftfreq(N)

    return y, f

if __name__ == "__main__":
    x = np.sin(2 * np.pi * 10 * np.linspace(0, 1, 100))
    y, f = fourier_transform(x)

    plt.plot(f, np.abs(y))
    plt.show()

# This code first imports the numpy and matplotlib libraries. Then, it defines a function called fourier_transform() that takes a signal as input and returns its Fourier transform. The function uses the numpy.fft.fft() function to calculate the Fourier transform. The numpy.fft.fftfreq() function is used to calculate the frequencies in the center of each bin in the output of numpy.fft.fft().

#The main function of the code then creates a sine wave signal and calculates its Fourier transform. The Fourier transform is plotted using the matplotlib.pyplot.plot() function.

#To run the code, you can save it as a .py file and then run it in a Python interpreter. For example, if you save the code as fourier_transform.py, you can run it by typing the following command in a Python interpreter:
