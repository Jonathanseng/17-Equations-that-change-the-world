def pythagorean_theorem(a, b):
  """
  Calculates the length of the hypotenuse of a right triangle given the lengths of the other two sides.

  Args:
    a: The length of one leg of the triangle.
    b: The length of the other leg of the triangle.

  Returns:
    The length of the hypotenuse of the triangle.
  """

  # Calculate the square of the hypotenuse.
  c_squared = a ** 2 + b ** 2

  # Take the square root of the square of the hypotenuse to get the length of the hypotenuse.
  c = c_squared ** 0.5

  return c

>>> pythagorean_theorem(3, 4)
5.0


# This code can be used to calculate the length of the hypotenuse of any right triangle, as long as the lengths of the other two sides are known. For example, if the lengths of the legs of a right triangle are 3 and 4, then the length of the hypotenuse can be found using the following code:
# As you can see, the output of the code is 5.0, which is the length of the hypotenuse of a right triangle with legs of length 3 and 4.
