import numpy as np
import pandas as pd
from scipy.optimize import minimize

# 假设构造的磁芯损耗预测模型
def magnetic_loss(params):
    T, f, W, B_peak, M = params
    # 这里L_model是根据问题四构建的模型函数
    # 示例：L_model = some_function(T, f, W, B_peak, M)
    # 需要根据实际的磁芯损耗预测公式更新
    L_model = ...  # 替换为合适的损耗模型
    return L_model

# 定义传输磁能
def transmission_energy(params):
    T, f, W, B_peak, M = params
    return f * B_peak  # 传输磁能的计算

# 目标函数
def objective_function(params):
    loss = magnetic_loss(params)
    energy = transmission_energy(params)
    # 这里我们希望最小化损耗，并最大化传输能量
    return loss - energy # 需要处理负值以指示最大化

# 设定初始值
initial_guess = [25, 100000, 1, 0.5, 1]  # 假定初始条件

# 约束和边界（根据具体问题设定）
bounds = [(25, 90), (50000, 500000), (1, 3), (0.1, 1), (1, 4)]  # 温度、频率、波形、磁通密度、材料范围

# 执行优化
result = minimize(objective_function, initial_guess, bounds=bounds)

# 输出结果
optimal_conditions = result.x
print("最优条件:")
print(f"温度: {optimal_conditions[0]}")
print(f"频率: {optimal_conditions[1]}")
print(f"波形: {optimal_conditions[2]}")
print(f"磁通密度峰值: {optimal_conditions[3]}")
print(f"磁芯材料: {optimal_conditions[4]}")