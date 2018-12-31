import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    eSum = np.sum(np.exp(L))
    result = [np.exp(x)/eSum for x in L]
    return result

print(softmax([1, 2, 3]))