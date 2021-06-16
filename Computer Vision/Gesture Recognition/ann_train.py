import torch
import numpy as np
from ann import ArtificialNeuralNetwork
from torch.optim import SGD
import matplotlib.pyplot as plt
import torch.nn as nn



device = 'cuda' if torch.cuda.is_available() else 'cpu'
X = Variable(torch.randn(10, 120).float())
Y = Variable(torch.FloatTensor(10).uniform_(0, 120).long())
print(Y)

ann = ArtificialNeuralNetwork(len(X[0]), len(Y[0])).to(device)
loss_func = nn.CrossEntropyLoss()
opt = SGD(ann.parameters(), lr=0.001)
loss_history = []
for _ in range(1000):
    opt.zero_grad()
    loss_value = loss_func(ann(X), Y)
    loss_value.backward()
    opt.step()
    loss_history.append(loss_value)

plt.plot(loss_history)
plt.show()