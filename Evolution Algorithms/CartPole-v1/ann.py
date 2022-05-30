from torch import nn

def step(x):
    return 1 if x > 0 else 0

class NeuralNetwork(nn.Module):
    def __init__(self, _observation):
        super(NeuralNetwork, self).__init__()
        input_len = len(_observation[0])
        output_len = 1
        self.input2output = nn.Linear(input_len, output_len)
        self.activation_function_1 = nn.ReLU()
        self.activation_function_2 = nn.Sigmoid()

        self.weight_bias_l1 = self.input2output.state_dict()


    
    def forward(self, _input):
        _input = self.input2output(_input)
        _input = self.activation_function_1(_input)
        _input.cpu().detach().numpy()
        
        return step(_input)


    def get_weightNbias(self):
        return self.weight_bias_l1


