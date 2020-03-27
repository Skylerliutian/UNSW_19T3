import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


def pre_processing(array):
    trnsp = np.array(array).transpose()
    for sublist in trnsp:
        min_x = min(sublist)
        max_x = max(sublist)
        for i in range(len(sublist)):
            sublist[i] = (sublist[i] - min_x) / (max_x - min_x)
    normalisation = trnsp.transpose()
    return normalisation


def batch_gradient_descent(max_iteration, j, x, y):
    theta_0 = -1
    theta_j = -0.5
    alpha = 0.01
    x_T = x.transpose()
    j_funct = []
    for _ in range(max_iteration):
        hypothesis = theta_0 + theta_j * x_T[j]
        loss = y - hypothesis
        gradient_0 = sum(loss) / m
        gradient_1 = np.dot(loss, x_T[j]) / m
        theta_0 = theta_0 + alpha * gradient_0
        theta_j = theta_j + alpha * gradient_1
        j_funct.append(sum(np.square(loss)) / m)
    return theta_0, theta_j, j_funct


def predict(theta_0, theta_j, x, j):
    x_T = x.transpose()[j]
    res = theta_0 + theta_j * x_T

    return res


def evaluate_rmse(t0, tj, x, y, j):
    loss = (t0 + tj * x.transpose()[j]) - y
    length = len(loss)
    rmse = math.sqrt(sum(np.square(loss)) / length)
    return rmse


def plot(a, b, c):
    axis_x = [i for i in range(500)]
    plt.scatter(axis_x, a, color="r", s=2, label='TV')
    plt.scatter(axis_x, b, color="y", s=2, label='Radio')
    plt.scatter(axis_x, c, color="b", s=2, label='Newspaper')
    plt.legend()
    plt.show()


m = 190
data_frame = pd.read_csv("Advertising.csv")
data = data_frame.values[:]
print(data)
y_train = data[:m, -1]
y_test = data[m:, -1]

x = data[:, 1: -1]
normal_x = pre_processing(x)
normal_x_train = normal_x[:m, :]
normal_x_test = normal_x[m:, :]

tv_0, tv_j, tv_j_funct = batch_gradient_descent(500, 0, normal_x_train, y_train)

r_0, r_j, r_j_funct = batch_gradient_descent(500, 1, normal_x_train, y_train)
n_0, n_j, n_j_funct = batch_gradient_descent(500, 2, normal_x_train, y_train)

print("Q1: ",tv_0, tv_j)
plot(tv_j_funct, r_j_funct, n_j_funct)
print("Q3: ", evaluate_rmse(tv_0, tv_j, normal_x_train, y_train, 0))
print("Q4: ", evaluate_rmse(tv_0, tv_j, normal_x_test, y_test, 0))
print("Q5: ", evaluate_rmse(r_0, r_j, normal_x_test, y_test, 1))
print("Q6: ", evaluate_rmse(n_0, n_j, normal_x_test, y_test, 2))
# print("original value\n", y_test)
# print("use tv feature\n", predict(tv_0, tv_j, normal_x_test, 0))
# print("use radio feature\n", predict(r_0, r_j, normal_x_test, 1))
# print("use newspaper feature\n", predict(n_0, n_j, normal_x_test, 2))







