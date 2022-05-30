from ann import NeuralNetwork

def crossover (_nn_list, _sorted_inx, _observation):
    _n_children = len(_nn_list) // 5
    _chilren_list = []
    for i in range(_n_children // 2):
        child1 = NeuralNetwork(len(_observation[0]), 3)
        child2 = NeuralNetwork(len(_observation[0]), 3)

        parent1 = _nn_list[_sorted_inx[2*i]]
        parent2 = _nn_list[_sorted_inx[2*i + 1]]
        
        child1.input2hl.state_dict()['weight'] = parent1.input2hl.state_dict()['weight']
        child1.input2hl.state_dict()['bias'] = parent2.input2hl.state_dict()['bias']
        child1.hl2hl.state_dict()['weight'] = parent2.hl2hl.state_dict()['weight']
        child1.hl2hl.state_dict()['bias'] = parent1.hl2hl.state_dict()['bias']

        child2.hl2hl.state_dict()['weight'] = parent1.hl2hl.state_dict()['weight']
        child2.hl2hl.state_dict()['bias'] = parent2.hl2hl.state_dict()['bias']
        child2.hl2output.state_dict()['weight'] = parent2.hl2output.state_dict()['weight']
        child2.hl2output.state_dict()['bias'] = parent1.hl2output.state_dict()['bias']

        _chilren_list.append(child1)
        _chilren_list.append(child2)
    
    return _chilren_list


# def mutation():

