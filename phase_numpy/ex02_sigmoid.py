import numpy as np
def main():
    x = np.array([-10, -1, 0, 1, 10])
    print(sigmoid(x))

def sigmoid(z):
    a = 1 / (1 + np.exp(-z))
    return a

main()