import numpy as np

def find_sum(data,labels, th, th0):
    temp = labels* (th.T.dot(data) + th0)
    print(temp)
    return np.sum(temp)





data = np.array([[1, 2, 1, 2, 10, 10.3, 10.5, 10.7],
                 [1, 1, 2, 2,  2,  2,  2, 2]])
labels = np.array([[-1, -1, 1, 1, 1, 1, 1, 1]])
blue_th = np.array([[0, 1]]).T
blue_th0 = -1.5
red_th = np.array([[1, 0]]).T
red_th0 = -2.5
print(find_sum(data, labels, blue_th, blue_th0))
