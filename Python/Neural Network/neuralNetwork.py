import numpy
import nnfs
from layer import *
from activation import *
from loss import *

nnfs.init()

X = [[0.5, 3.49, 0.21, 2],
     [1, 4.94, 2.01, 1.5],
     [0.6, 2.3, 1.7, 0.1]]

y = [0, 1, 1]

layer1 = Layer(4, 5)
activation1 = ActivationReLU()

layer2 = Layer(5, 5)
activation2 = ActivationReLU()

layer3 = Layer(5, 4)
activation3 = SoftmaxLoss()

for _ in range(10000):
     layer1.forward(X)
     activation1.forward(layer1.output)
     layer2.forward(activation1.output)
     activation2.forward(layer2.output)
     layer3.forward(activation2.output)
     loss = activation3.forward(layer3.output, y)

     print(loss)
     activation3.back(activation3.output, y)
     layer3.back(activation3.output)
     activation2.back(layer3.output)
     layer2.back(activation2.output)
     activation1.back(layer2.output)
     layer1.back(activation1.output)
