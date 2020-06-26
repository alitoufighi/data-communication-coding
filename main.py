from utils import *
from HuffmanEncoder import HuffmanEncoder
from HuffmanDecoder import HuffmanDecoder
from ConvolutionalEncoder import ConvolutionalEncoder
from ViterbiDecoder import ViterbiDecoder
from noise import noise

probabilities = read_probabilities()
he = HuffmanEncoder(probabilities)
hd = HuffmanDecoder(probabilities)

res = he.encode("mohammadalitoufighi")
res = ConvolutionalEncoder.encode(res)
res = noise(res)  # Comment this if you want to test the correctness
res = ViterbiDecoder.decode(res)
res = hd.decode(res)
print(res)
