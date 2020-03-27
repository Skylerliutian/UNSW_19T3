import torch
import numpy as np
x = torch.randn([5, 3, 3])
y = torch.sum(x > 0).item()
print(y)








