import numpy as np

class ActivationReLU:
  def forward(self, inputs):
    self.output = np.maximum(0, inputs)
  def back(self, dvalues):
    dinputs = dvalues.copy()
    dinputs[self.inputs <= 0] = 0
    
class ActivationSoftmax:
  def forward(self, inputs):
    expValues = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
    self.output = expValues / np.sum(expValues, axis=1, keepdims=True)
  def back(self, dvalues):
    self.dinputs = np.empty_like(dvalues)
    for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
      single_output = single_output.reshape(-1, 1)
      jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)
      self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)
