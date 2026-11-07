import numpy as np
from ex03_neuron import neuron
from ex02_sigmoid import sigmoid  

def main():
    W = np.array([[1,0,0,0],
                [0,1,0,0],
                [1,1,1,1]])
    x = np.array([1,2,3,4])
    b = np.array([0,0,-5])

    print(neuron_layer_fast(W,x,b))

def neuron_layer_fast(W,x,b):
    a = (neuron(W,x,b))
    return a


if __name__ == "__main__":
    main()