from utils import create_huffman_mappings


class HuffmanEncoder:

    def __init__(self, probabilities: dict):
        self.char_frequencies = probabilities
        self.mappings = self._create_mappings()

    def _create_mappings(self) -> dict:
        huffman_mappings = create_huffman_mappings(self.char_frequencies)
        assert int(huffman_mappings[0]) == 1
        return huffman_mappings[1]
    
    def encode(self, string: str) -> str:
        result = ""
        for char in string:
            result += self.mappings[char]
        return result
