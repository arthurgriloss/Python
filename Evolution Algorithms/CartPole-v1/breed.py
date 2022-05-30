from ann import NeuralNetwork
import numpy as np
import random
import torch
import torch.nn as nn


def crossover(_parent1, _parent2):

    _child1 = NeuralNetwork([np.zeros(4)])
    _child2 = NeuralNetwork([np.zeros(4)])

    _child1.input2output.state_dict()['weight'] = _parent1.weight_bias_l1['weight']
    _child1.input2output.state_dict()['bias'] = _parent2.weight_bias_l1['bias']
    
    _child2.input2output.state_dict()['weight'] = _parent2.weight_bias_l1['weight']
    _child2.input2output.state_dict()['bias'] = _parent1.weight_bias_l1['bias']

    return _child1, _child2


def mutation(_nn_list, _sorted_idx):
    for i in range(4, len(_sorted_idx) - 2):
        if random.random() >= 0.5:
            _mutation_type = random.randint(1, 3)
            if _mutation_type == 1:
                _nn_list[_sorted_idx[i]].input2output.state_dict()['bias'] = torch.tensor(random.random())
            elif _mutation_type == 2:
                _nn_list[_sorted_idx[i]].input2output.state_dict()['weight'][0] = torch.fliplr(_nn_list[_sorted_idx[i]].input2output.state_dict()['weight'])[0] # reverse the tensor
            else:
                len_weight = len(_nn_list[_sorted_idx[i]].input2output.state_dict()['weight'][0])
                
                idx1 = random.randint(0, len_weight - 1)
                idx2 = random.randint(0, len_weight - 1)

                value1 = _nn_list[_sorted_idx[i]].input2output.state_dict()['weight'][0][idx1]
                value2 = _nn_list[_sorted_idx[i]].input2output.state_dict()['weight'][0][idx2]

                _nn_list[_sorted_idx[i]].input2output.state_dict()['weight'][0][idx1] = value2
                _nn_list[_sorted_idx[i]].input2output.state_dict()['weight'][0][idx2] = value1

    return _nn_list


def replace (_nn_list, _sorted_idx, _state):

    for i in range(7, len(_sorted_idx) - 2):
        _nn_list[_sorted_idx[i]] = NeuralNetwork(_state)

    return _nn_list
