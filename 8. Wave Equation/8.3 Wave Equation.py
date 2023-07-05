import numpy as np
import matplotlib.pyplot as plt

def wave_equation(u, c, dx, dt):
    """
    Calculates the next step in the solution to the wave equation.

    Args:
        u: The current solution to the wave equation.
        c: The speed of the wave.
        dx: The spacing between grid points.
        dt: The time step.

    Returns:
        The next step in the solution to the wave equation.
    """

    u_new = u.copy()
    u_new[1:-1] = (u[1:-1] + u[:-2] - 2 * u[1:-1]) * dt / dx ** 2 + u[1:-1]
    return u_new

def main():
    """
    Run the main simulation.
    """

    c = 1.0
    dx = 0.01
    dt = 0.001
    tmax = 10.0

    u = np.sin(2 * np.pi * 0.5 * dx)

    for t in np.arange(0, tmax, dt):
        u = wave_equation(u, c, dx, dt)

    plt.plot(u)
    plt.show()

if __name__ == "__main__":
    main()

#This code first imports the numpy and matplotlib.pyplot libraries. Then, it defines a function called wave_equation() that takes the current solution to the wave equation, the speed of the wave, the spacing between grid points, and the time step as input, and returns the next step in the solution to the wave equation. The function uses the finite difference method to calculate the next step in the solution.

#The main function of the code then runs the main simulation. The simulation starts with a sine wave as the initial condition. The wave equation is then used to calculate the next step in the solution. This process is repeated until the end of the simulation.

#The final step in the code is to plot the solution to the wave equation. The matplotlib.pyplot.plot() function is used to plot the solution.

#To run the code, you can save it as a .py file and then run it in a Python interpreter. For example, if you save the code as wave_equation.py, you can run it by typing the following command in a Python interpreter:
