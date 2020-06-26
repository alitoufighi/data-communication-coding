from sys import maxsize
from collections import defaultdict
from utils import *

class ViterbiDecoder:
    _mappings = {
        "100": "11",
        "000": "00",
        "110": "00",
        "010": "11",
        "111": "10",
        "011": "01",
        "101": "01",
        "001": "10"
    }

    @staticmethod
    def decode(binary_string: str) -> str:
        result = ""
        pm = [0, maxsize, maxsize, maxsize]
        for b1, b2 in zip(binary_string[0::2], binary_string[1::2]):
            next_state = defaultdict(list)
            received_bits = f'{b1}{b2}'
            for state_index in range(len(pm)):
                for i in ['0', '1']:
                    start_index_bin = decimal_to_binary(state_index, min_bits=2)
                    dest_state_bin = f'{i}{start_index_bin[0]}'
                    dest_state = binary_to_decimal(dest_state_bin)
                    branch_value = ViterbiDecoder._mappings[f'{i}{start_index_bin}']
                    branch_metric = calculate_hamming_distance(received_bits, branch_value)
                    next_state[dest_state].append({
                        "bit": i,
                        "val": pm[state_index] + branch_metric
                    })
            min_val = maxsize
            min_bit = ""
            for key, value in next_state.items():
                m = min(value, key=lambda item: item['val'])
                if m['val'] < min_val:
                    min_val = m['val']
                    min_bit = m['bit']
                pm[key] = m['val']
            result += min_bit

        return result
