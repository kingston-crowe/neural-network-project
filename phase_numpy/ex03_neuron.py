import numpy as np
from ex02_sigmoid import sigmoid 

def main():
    w = np.array([0.5,-1 ,2])
    x = np.array([1,2,3])
    b = 0.1
    print(neuron(w,x,b))


def neuron(w,x,b):
    z = np.dot(w,x) + b
    return sigmoid(z)

if __name__ == "__main__":
    main()