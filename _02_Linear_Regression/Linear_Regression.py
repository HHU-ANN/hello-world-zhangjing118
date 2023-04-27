# 最终在main函数中传入一个维度为6的numpy数组，输出预测值

import os

try:
    import numpy as np
except ImportError as e:
    os.system("sudo pip3 install numpy")
    import numpy as np

def ridge(x,y):
    a=0.5
    x=x.transpose()
    E=np.eye(np.linalg.inv(np.dot(x,x1)))
    return np.dot(np.linalg.inv(np.dot(x,x1)+np.dot(a,E)),np.dot(x,y))
    
def lasso(data):


def read_data(path='./data/exp02/'):
    x = np.load(path + 'X_train.npy')
    y = np.load(path + 'y_train.npy')
    return x, y





