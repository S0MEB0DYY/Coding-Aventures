import numpy as np
from activation import *

class Loss:
   def calculate(self, yPred, yTrue):
     loss = self.forward(yPred, yTrue)
     return loss
class LossFunction(Loss):
  def forward(self, yPred, yTrue):
    yPredClipped = np.clip(yPred, 1e-7, 1-1e-7)
    
    if len(yTrue.shape) == 1:
      loss = -np.log(yPredClipped[range(len(yPred)), yTrue])
    elif len(yTrue.shape) == 2:
      loss = -np.mean(np.sum(yTrue * np.log(yPredClipped), axis=1))
    return loss
  def back(self, yTrue):
     samples = len(dvalues)
     labels = len(dvalues[0])
     if len(y_true.shape) == 1:
        y_true = np.eye(labels)[y_true]
     self.dinputs = -y_true / dvalues
     self.dinputs = self.dinputs / samples
class SoftmaxLoss:
   def __init__(self):
     self.activation = ActivationSoftmax()
     self.loss = LossFunction()
      
   def forward(self, inputs, yTrue):
      self.activation.forward(inputs)
      self.output = self.activation.output
      return self.loss.calculate(self.output, yTrue)
      
   def back(self, dvalues, yTrue):
      samples = len(dvalues)
      f len(yTrue.shape) == 2:
        yTrue = np.argmax(yTrue, axis=1)
      self.dinputs = dvalues.copy()
      self.dinputs[range(samples), yTrue] -= 1
      self.dinputs = self.dinputs / samples
