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


def decimal_to_binary(decimal: int, min_bits=1) -> str:
    result = str(bin(decimal))[2:]
    if len(result) < min_bits:
        result = (min_bits - len(result)) * '0' + result
    return result


def binary_to_decimal(binary: str) -> int:
    return int(binary, 2)


def calculate_hamming_distance(bin1: str, bin2: str) -> int:
    assert len(bin1) == len(bin2)
    result = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            result += 1
    return result
