import math

def time_dilation(v, c):
  """Calculates the time dilation factor for a moving object.

  Args:
    v: The speed of the object in meters per second.
    c: The speed of light in meters per second.

  Returns:
    The time dilation factor.
  """

  return 1 / math.sqrt(1 - (v / c)**2)

def length_contraction(v, c):
  """Calculates the length contraction factor for a moving object.

  Args:
    v: The speed of the object in meters per second.
    c: The speed of light in meters per second.

  Returns:
    The length contraction factor.
  """

  return 1 / math.sqrt(1 - (v / c)**2)

def mass_energy_equivalence(m):
  """Calculates the mass-energy equivalence of an object.

  Args:
    m: The mass of the object in kilograms.

  Returns:
    The mass-energy of the object in joules.
  """

  return m * math.pow(c, 2)

def main():
  # Calculate the time dilation factor for an object moving at 0.9c.
  v = 0.9 * c
  time_dilation_factor = time_dilation(v, c)
  print("The time dilation factor for v = 0.9c is:", time_dilation_factor)

  # Calculate the length contraction factor for an object moving at 0.9c.
  length_contraction_factor = length_contraction(v, c)
  print("The length contraction factor for v = 0.9c is:", length_contraction_factor)

  # Calculate the mass-energy equivalence of an object with mass 1 kg.
  mass = 1
  mass_energy = mass_energy_equivalence(mass)
  print("The mass-energy of an object with mass 1 kg is:", mass_energy)

if __name__ == "__main__":
  main()

# This code calculates the time dilation factor, length contraction factor, and mass-energy equivalence for an object moving at a given speed. The code can be easily modified to calculate these quantities for different speeds.

#To run the code, you can save it as a Python file and then run it from the command line. For example, if you save the code as relativity.py, you can run it by typing the following command into the command line:
