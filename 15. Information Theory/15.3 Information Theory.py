import math

def entropy(p):
  """
  Calculates the entropy of a probability distribution.

  Args:
    p: A list of probabilities.

  Returns:
    The entropy of the probability distribution.
  """

  entropy = 0
  for pi in p:
    if pi > 0:
      entropy -= pi * math.log2(pi)
  return entropy

def main():
  """
  Calculates the entropy of a few probability distributions.
  """

  p1 = [0.2, 0.8]
  p2 = [0.5, 0.5]
  p3 = [0.1, 0.9]

  print("Entropy of p1:", entropy(p1))
  print("Entropy of p2:", entropy(p2))
  print("Entropy of p3:", entropy(p3))

if __name__ == "__main__":
  main()

# This code first defines a function called entropy(), which takes a list of probabilities as input and returns the entropy of the probability distribution. The entropy of a probability distribution is a measure of the uncertainty involved in the value of a random variable. The higher the entropy, the more uncertain the value of the random variable, and therefore the more information is contained in the message.

#The entropy() function works by looping through the list of probabilities and adding the negative logarithm of each probability to the entropy. The logarithm is used to convert the probabilities to a common scale, so that the entropy can be calculated regardless of the size of the probabilities.

#The main() function then calls the entropy() function on a few different probability distributions. The results of the entropy() function are then printed to the console.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as entropy.py, you can run it by typing the following command into the command line:
