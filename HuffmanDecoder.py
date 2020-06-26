from heapq import heappush, heappop, heapify

class HuffmanDecoder:

    def __init__(self, probabilities: dict):
        self.char_frequencies = probabilities
        self.mappings = self._create_mappings()

    def _create_mappings(self):
        # each item in heap is a list, with first index containing probability, and 
        # second index as a dict consisting of all previously-merged symbols (with symbol as key and encoded binary as value)
        heap = [[freq, {sym: ""}] for sym, freq in self.char_frequencies.items()]
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
        assert int(result[0]) == 1 
        return { v: k for k, v in result[1].items() }  # invert key, values for binary to character mappings
    
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