from mat4py import loadmat
from itertools import chain
from heapq import heappush, heappop, heapify


# Reads probabilities from .mat file
# and returns the flattened list as a dictionary with alphabet letters as keys
def read_probabilities():
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


def create_huffman_mappings(char_frequencies):
    # each item in heap is a list, with first index containing probability, and
    # second index as a dict consisting all previously-merged symbols
    # (with symbol as key and encoded binary as value)
    heap = [[frequency, {symbol: ""}] for symbol, frequency in char_frequencies.items()]
    heapify(heap)
    while len(heap) > 1:
        m1 = heappop(heap)
        m2 = heappop(heap)
        for symbol, encoded_binary in m1[1].items():
            m1[1][symbol] = '0' + encoded_binary
        for symbol, encoded_binary in m2[1].items():
            m2[1][symbol] = '1' + encoded_binary
        new_item = [m1[0] + m2[0], {**m1[1], **m2[1]}]
        heappush(heap, new_item)
    result = heappop(heap)
    return result
