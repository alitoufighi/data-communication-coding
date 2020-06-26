from utils import *
from HuffmanEncoder import HuffmanEncoder
from HuffmanDecoder import HuffmanDecoder
from ConvolutionalEncoder import ConvolutionalEncoder
from ViterbiDecoder import ViterbiDecoder

probabilities = read_probabilites()
he = HuffmanEncoder(probabilities)
hd = HuffmanDecoder(probabilities)

res = he.encode("mohammadalitoufighi")
res = ConvolutionalEncoder.encode(res)
res = ViterbiDecoder.decode(res)
res = hd.decode(res)
print(res)
