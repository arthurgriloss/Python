import enum
import gym
import numpy as np
import torch
from ann import NeuralNetwork
import matplotlib.pyplot as plt
import breeding


def create_env(_population):
    _env = []
    _observation = []
    for _ in range(_population):
        _enviroment = gym.make('Acrobot-v1')
        _env.append(_enviroment)
        _observation.append(_enviroment.reset())

    return _env, _observation


def move(_env, _nn_list, _state):
    _observation = []
    _reward = []
    _done = []
    _info = []

    for _idx, _enviroment in enumerate(_env):
        if _enviroment == 0:
            _observation.append([0, 0, 0, 0, 0, 0])
            _reward.append(0)
            _done.append(True)
            _info.append({})
        else:
            action = torch.argmax(_nn_list[_idx].forward(torch.tensor(_state[_idx]).float()))
            action = action.cpu().detach().numpy()
            _result =_env[_idx].step(action)
            _observation.append(_result[0])
            _reward.append(_result[1])
            _done.append(_result[2])
            _info.append(_result[3])

    return np.array(_observation), np.array(_reward), np.array(_done), np.array(_info)


def check_if_done(_done, _env):
    for _idx, _state in enumerate(_env):
        if _done[_idx]:
            _env[_idx] = 0
    
    return _env

population = 100
epochs = 100

observation = gym.make('Acrobot-v1').reset()
observation_len = (len(observation))
action_len = 3
sorted_index_pos = np.zeros(population).astype(int)


nn_list = []
for _ in range(population):
    nn_list.append(NeuralNetwork(observation_len, action_len))


for i_episode in range(epochs):
    env, observation = create_env(population)
    total_reward = np.zeros(population)
    for steps in range(100):
        if np.all(env == 0):
            break
        else:
            observation, reward, done, info = move(env, nn_list, observation)
            env[sorted_index_pos[0]].render()
            total_reward = total_reward + reward
            env = check_if_done(done, env)

    sorted_index_pos = [index for index, num in sorted(enumerate(total_reward), key=lambda x: x[-1])]
    env[sorted_index_pos[0]].render()

    for idx in range(40):
        nn_list[sorted_index_pos[-idx - 1]] = NeuralNetwork(observation_len, action_len)

    children = breeding.crossover(nn_list, sorted_index_pos, observation)
    for idx, child in enumerate(children):
        nn_list[sorted_index_pos[-idx - 1]] = child

    print(total_reward)


