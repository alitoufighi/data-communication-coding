from utils import create_huffman_mappings


class HuffmanDecoder:

    def __init__(self, probabilities: dict):
        self.char_frequencies = probabilities
        self.mappings = self._create_mappings()

    def _create_mappings(self):
        huffman_mappings = create_huffman_mappings(self.char_frequencies)
        assert int(huffman_mappings[0]) == 1
        return {v: k for k, v in huffman_mappings[1].items()}  # invert key, values for binary to character mappings
    
    def decode(self, binary_string: str):
        result = ""
        searching_symbol = ""
        for char in binary_string:
            assert char in ['0', '1']
            searching_symbol += char
            if searching_symbol in self.mappings:
                result += self.mappings[searching_symbol]
                searching_symbol = ""
        return result
