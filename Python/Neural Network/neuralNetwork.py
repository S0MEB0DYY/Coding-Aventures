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
layer1.forward(X)
activation1 = ActivationReLU()
activation1.forward(layer1.output)

layer2 = Layer(5, 5)
layer2.forward(activation1.output)
activation2 = ActivationReLU()
activation2.forward(layer2.output)

layer3 = Layer(5, 4)
layer3.forward(activation2.output)
activation3 = ActivationSoftmax()
activation3.forward(layer3.output)

lossFunction = LossFunction()
loss = lossFunction.calculate(activation3.output, y)

print("Loss: ", loss)
