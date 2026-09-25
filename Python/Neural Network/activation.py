import numpy as np

class ActivationReLU:
  def forward(self, inputs):
    self.output = np.maximum(0, inputs)
class ActivationSoftmax:
  def forward(self, inputs):
    expValues = np.exp(inputs) - np.max(inputs, axis=1, keepdims=True)
    self.output = expValues / np.sum(expValues, axis=1, keepdims=True)
