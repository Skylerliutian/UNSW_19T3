import torch.nn as nn
import torch
#
# input = torch.randn(6, 3, 10)
# print(input.size()[2])
# # print('----------------')
# # for i in range(6):
# #     print(input[i])
# print(torch.autograd.Variable(input))

rnn = nn.LSTM(10, 20, 2)
input = torch.randn(5, 3, 10)
h0 = torch.randn(2, 3, 20)
c0 = torch.randn(2, 3, 20)
output, (hn, cn) = rnn(input, (h0, c0))
print(output.size())
print(input.size())
print(hn.size(), cn.size())