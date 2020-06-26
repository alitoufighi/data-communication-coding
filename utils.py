from mat4py import loadmat
from itertools import chain

# Reads probabilities from .mat file
# and returns the flattened list as a dictionary with alphabet letters as keys
def read_probabilites():
    data = loadmat('freq.mat')['freq']
    result = {}
    for index, probability in enumerate(list(chain.from_iterable(data))):
        result[chr(int(index+ord('a')))] = probability
    assert len(result) == 26
    return result
