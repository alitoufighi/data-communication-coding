import numpy as np


def noise(data):
    result = ""
    for i in range(len(data)):
        r = np.random.rand()
        if r < 0.01:
            result += '1' if data[i] == '0' else '1'
        else:
            result += data[i]
    return result
