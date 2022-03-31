import torch
import torch.nn as nn
    
class ArtificialNeuralNetwork(nn.Module):
    def __init__(self, len_in, len_out):
        super().__init__()
        input_len = len_in
        output_len = len_out
        max_len = max(input_len, output_len)
        incremet = max_len * 3
        self.input_to_hl = nn.Linear(input_len, max_len + incremet)
        self.hl0_to_hl0 = nn.Linear(max_len + incremet, max_len + incremet)
        self.hl0_to_hl1 = nn.Linear(max_len + incremet, max_len + int(incremet * 2/3))
        self.hl1_to_hl1 = nn.Linear(max_len + int(incremet * 2/3), max_len + int(incremet * 2/3))
        self.hl1_to_hl2 = nn.Linear(max_len + int(incremet * 2/3), max_len + int(incremet * 1/3))
        self.hl2_to_hl2 = nn.Linear(max_len + int(incremet * 1/3), max_len + int(incremet * 1/3))
        self.hl_to_output = nn.Linear(max_len + int(incremet  * 1/3), output_len)
        self.activation_fun1 = nn.ReLU()
        self.activation_fun2 = nn.Sigmoid()


    def forward(self, x):
        x = self.input_to_hl(x)
        x = self.activation_fun1(x)
        # x = self.hl0_to_hl0(x)
        # x = self.activation_fun1(x)
        x = self.hl0_to_hl1(x)
        x = self.activation_fun1(x)
        # x = self.hl1_to_hl1(x)
        # x = self.activation_fun1(x)
        # x = self.hl1_to_hl1(x)
        # x = self.activation_fun1(x)
        x = self.hl1_to_hl2(x)
        x = self.activation_fun1(x)
        # x = self.hl2_to_hl2(x)
        # x = self.activation_fun1(x)
        # x = self.hl2_to_hl2(x)
        # x = self.activation_fun1(x)
        # x = self.hl2_to_hl2(x)
        # x = self.activation_fun1(x)
        x = self.hl_to_output(x)
        x = self.activation_fun2(x)
        return x

