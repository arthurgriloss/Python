import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, _input_len, _output_len):
        super(NeuralNetwork, self).__init__()
        self.input2hl = nn.Linear(_input_len, _input_len * 2)
        self.hl2hl = nn.Linear(_input_len * 2, _input_len + 1)
        self.hl2output = nn.Linear(_input_len + 1, _output_len)
        self.activation_function1 = nn.ReLU()
        self.activation_function2 = nn.Sigmoid()

    def forward(self, _input):
        _input = self.input2hl(_input)
        _input = self.activation_function1(_input)
        _input = self.hl2hl(_input)
        _input = self.activation_function1(_input)
        _input = self.hl2output(_input)
        _input = self.activation_function2(_input)

        return _input

