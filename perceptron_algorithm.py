import numpy as np

np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])


def percetronStep(X, y, W, b, learn_rate = 0.01):
    for in in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i] - y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
    return W, b
