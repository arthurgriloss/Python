import gym
import numpy as np
from ann import NeuralNetwork
import torchvision.models as model
import torch
import breed
import matplotlib.pyplot as plt

def offspring(_population):
    """ Initiate n enviroments, where n is the population size"""

    _enviroment = []
    _nn_list = []
    _observations = []
    for _ in range(_population):
        _env = gym.make('CartPole-v1')
        _state = _env.reset()
        _observations.append(_state) 

        _enviroment.append(_env)
        _nn_list.append(NeuralNetwork([_state]))
    
    return np.array(_enviroment), np.array(_observations)


def move(_env, _nn_list, _state):
    """ 
    Returs four matrix: the observation matrix, the reward matrix, the done matrix, and the info matrix
    Each element of the matrix represent one member.
    Ex.: observation[3] will have the observation vector from the fourth member
    """

    _observation = []
    _reward = []
    _done = []
    _info = []
    for _idx, _enviroment in enumerate(_env):
        if _enviroment == 0:
            _observation.append([9999, 9999, 9999, 9999])
            _reward.append(0)
            _done.append(True)
            _info.append({})
        else:
            _tensor = torch.from_numpy(_state[_idx]).float()
            _result = _enviroment.step(_nn_list[_idx].forward(_tensor))
            _observation.append(_result[0])
            _reward.append(_result[1])
            _done.append(_result[2])
            _info.append(_result[3])

    return np.array(_observation), np.array(_reward), np.array(_done), np.array(_info)



def env_done(_done, _env):
    """Check if the enviroment is done. If done it will delete the enviroment from the list"""

    _delete_list = []
    for _idx, _enviroment in enumerate(_env):
        if _done[_idx]:
            _env[_idx] = 0
    #         _delete_list.append(_idx)
    # _env = np.delete(_env, _delete_list)

    return _env


def render_best_fit(_observation, _env):
    """Will display just the best fit member"""

    _best_fit = np.argmin(abs(_observation[:, 0]))
    _env[_best_fit].render()



def close_env(_env):
    """Close all previously intiated enviroments"""

    for _enviroment in _env:
        if _enviroment != 0:
            _enviroment.close()


population = 10
epochs = 50
actions = (0, 1)



# print(NeuralNetwork(observation).get_weightNbias()['weight'])

max_reward = []
avg_reward = []
nn_list = []

env = gym.make('CartPole-v1')
state = env.reset()
for _ in range(population):
    nn_list.append(NeuralNetwork([state]))

for __ in range(epochs):
    env, observation = offspring(population)
    total_reward = np.zeros(len(env))
    for ___ in range(1000):
        if np.all(env == 0):
            break
        else:
            observation, reward, done, info = move(env, nn_list, observation)
            render_best_fit(observation, env)
            total_reward = total_reward + reward 
            env = env_done(done, env)

    max_reward.append(max(total_reward))
    avg_reward.append(np.mean(total_reward)) 

    sorted_index_pos = [index for index, num in sorted(enumerate(total_reward), key=lambda x: x[-1])][::-1]
    
    child1, child2 = breed.crossover(nn_list[sorted_index_pos[0]], nn_list[sorted_index_pos[1]])
    nn_list[sorted_index_pos[-1]] = child1
    nn_list[sorted_index_pos[-2]] = child2

    nn_list = breed.replace(nn_list, sorted_index_pos, observation)

    print(max_reward[__])
    print(avg_reward[__])
    print("")
    nn_list = breed.mutation(nn_list, sorted_index_pos)

plt.plot(range(len(max_reward)), max_reward)
plt.plot(range(len(avg_reward)), avg_reward)
plt.show()

# close_env(env)