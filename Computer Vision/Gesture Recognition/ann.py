import torch
import torch.nn as nn
    
class ArtificialNeuralNetwork(nn.Module):
    def __init__(self, len_in, len_out):
        super().__init__()
        input_len = len_in
        output_len = len_out
        hl_len = max(input_len, output_len) + 1
        self.input_to_hl = nn.Linear(input_len, hl_len)
        self.hl_to_hl = nn.Linear(hl_len, hl_len)
        self.hl_to_output = nn.Linear(hl_len, output_len)
        self.activation_fun1 = nn.ReLU()
        self.activation_fun2 = nn.Sigmoid()


    def forward(self, x):
        x = self.input_to_hl(x)
        x = self.hl_to_hl(x)
        x = self.activation_fun1(x)
        x = self.hl_to_output(x)
        y_pred = self.activation_fun2(x)
        return y_pred

