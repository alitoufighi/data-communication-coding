from utils import *
from HuffmanEncoder import HuffmanEncoder
from HuffmanDecoder import HuffmanDecoder
from ConvolutionalEncoder import ConvolutionalEncoder

probabilities = read_probabilites()
he = HuffmanEncoder(probabilities)
hd = HuffmanDecoder(probabilities)

res = he.encode("a")
print(res)
res = ConvolutionalEncoder.encode(res)
# res = hd.decode(res)
print(res)
