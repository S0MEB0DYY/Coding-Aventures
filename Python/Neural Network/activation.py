import numpy as np

class ActivationReLU:
  def forward(self, inputs):
    self.output = np.maximum(0, inputs)
  def back(self, z, y):
    dw = -z.inputs * (1 if z > 0 else 0) * y / z
    db = (1 if z > 0 else 0) * y / z
    self.output.weights += -0.001 * dw
    self.output.biases += -0.001 * db
class ActivationSoftmax:
  def forward(self, inputs):
    expValues = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
    self.output = expValues / np.sum(expValues, axis=1, keepdims=True)
