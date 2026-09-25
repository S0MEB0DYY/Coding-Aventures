import numpy
import nnfs
from layer import *

nnfs.init()

X = [[0.5, 3.49, 0.21, 2],
     [1, 4.94, 2.01, 1.5],
     [0.6, 2.3, 1.7, 0.1]]

layer1 = Layer(3, 4)
