import numpy as np

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
