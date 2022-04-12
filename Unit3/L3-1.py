import numpy as np
from matplotlib import pyplot as plt

def main() -> None:
    
    a:float = 1.50
    
    x = np.linspace(-1, 1)
    y = a * x
    
    plt.plot(x, y)
    plt.xlabel("X", size=10)
    plt.ylabel("Y", size=10)
    
    plt.show()

if __name__ == '__main__':
    main()