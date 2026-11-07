import numpy as np
def main(): 
    w = np.array([1,2,3])
    x = np.array([4,5,6])
    print(dot_product(w, x))
    print(np.dot(w,x))
    print(w @ x)

    
def dot_product(w,x):
    total = 0
    if len(w) != len(x):
        raise ValueError("Vectors not the same dimension")
    for i in range(len(w)):
        total += (w[i] * x[i])
    return total

if __name__ == "__main__":
    main()
