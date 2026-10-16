import numpy as np
import torch
import torch.nn as nn

# Entradas de prueba
x_np = np.array([-2.0, -0.5, 0.0, 2.0])
x_pt = torch.tensor([-2.0, -0.5, 0.0, 2.0])

# 1. ELU en NumPy
# f(x) = x si x > 0 ; f(x) = alpha * (exp(x) - 1) si x <= 0
alpha = 1.0
y_elu_np = np.where(x_np > 0, x_np, alpha * (np.exp(x_np) - 1))
print("ELU (NumPy):", y_elu_np)

# 2. ELU en PyTorch
elu = nn.ELU(alpha=1.0)
y_elu_pt = elu(x_pt)
print("ELU (PyTorch):", y_elu_pt)