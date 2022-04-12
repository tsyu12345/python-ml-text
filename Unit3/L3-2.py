import numpy as np
from matplotlib import pyplot as plt

def main() -> None:
    
    b:int = 50
    
    x = np.linspace(-1, 1) 
    y = b * x
    
    plt.plot(x, y, 'r')
    
    plt.xlabel("X", size=10)
    plt.ylabel("Y", size=10)
    
    plt.show()
    
if __name__ == '__main__':
    main()