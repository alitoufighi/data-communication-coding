from HuffmanEncoder import HuffmanEncoder
from HuffmanDecoder import HuffmanDecoder

probabilities = read_probabilites()
he = HuffmanEncoder(probabilities)
hd = HuffmanDecoder(probabilities)

res = he.encode("alitou")
res = hd.decode(res)
print(res)
