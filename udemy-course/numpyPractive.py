import numpy as np

def main():
    a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
    
    b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
    print(np.intersect1d(a,b))

    q2 = np.arange(1,16)
    q2 = q2.reshape(5,3, order  ='F')
    print(q2)
    q3 = q2.T.flatten()
    print(q3)
    q4 = q2.T.reshape(1,3,5)
    print(q4)
    print(q4.reshape(3,5).T)
    a = np.array([12, 5, 7, 15, 3, 1, 8])
    b = np.array([14, 6, 3, 11, 19, 12, 5])
    boolArray = np.isin(a, b)
    a = a[~boolArray]
    print(a)
if __name__ == '__main__':
    main() 