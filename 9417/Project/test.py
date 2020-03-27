import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math


# replacing the missing value with mean
def replace_missing_value(data):
    t = data.transpose()
    mean = t[1:].mean(axis=1)
    for i in range(len(mean)):
        if math.isnan(mean[i]):
            sum = 0
            count = 0
            for j in range(len(t[1:][i])):
                if not math.isnan(t[1:][i][j]):
                    sum += t[1:][i][j]
                    count += 1
            ave = round(sum / count)
            for j in range(len(t[1:][i])):
                if math.isnan(t[1:][i][j]):
                    t[1:][i][j] = ave
    # mean = t[1:].mean(axis=1)
    data = t.transpose()
    return data


# compute the positive and negative score
def p_n_score(data):
    pos_score = []
    neg_score = []
    for i in data:
        p = 0
        n = 0
        for j in pos_col:
            p += i[j]
        for j in neg_col:
            n += i[j]
        pos_score.append(p)
        neg_score.append(n)
    return np.asarray(pos_score), np.asarray(neg_score)


def flo_score(data):
    score = data[:, 1:].sum(axis=1)
    return score


def split_pre_post(data):
    for i in range(len(data.values)):
        if panas_set.values[i][1] != 'pre':
            split_index = i
            break
    pre = np.delete(data.values[:split_index], [1], axis=1)
    post = np.delete(data.values[split_index:], [1], axis=1)
    f_pre = replace_missing_value(pre)
    f_post = replace_missing_value(post)

    return f_pre, f_post


panas_set = pd.read_csv("./StudentLife_Dataset/Outputs/panas.csv")
flourishing_set = pd.read_csv("./StudentLife_Dataset/Outputs/FlourishingScale.csv")


final_pan_pre, final_pan_post = split_pre_post(panas_set)
final_flo_pre, final_flo_post = split_pre_post(flourishing_set)

# 1. For PANAs
# positive and negative columns
pos_col = [1, 4, 8, 9, 11, 12, 14, 15, 17]
neg_col = [2, 3, 5, 6, 7, 10, 13, 16, 18]

# add pos_score and neg_score as new columns and plot graphs
po, ng = p_n_score(final_pan_pre)
final_pan_pre = np.column_stack((final_pan_pre, po.transpose()))
final_pan_pre = np.column_stack((final_pan_pre, ng.transpose()))

po, ng = p_n_score(final_pan_post)
final_pan_post = np.column_stack((final_pan_post, po.transpose()))
final_pan_post = np.column_stack((final_pan_post, ng.transpose()))


axis_x = [i for i in range(len(final_pan_pre))]
plt.scatter(axis_x, final_pan_pre[:, -2], color='r', s=9)
plt.xlabel('u_id')
plt.ylabel('score')
plt.title('Pre test positive score')
plt.show()

axis_x = [i for i in range(len(final_pan_pre))]
plt.scatter(axis_x, final_pan_pre[:, -1], color='g', s=9)
plt.xlabel('u_id')
plt.ylabel('score')
plt.title('Pre test negative score')
plt.show()

axis_x = [i for i in range(len(final_pan_post))]
plt.scatter(axis_x, final_pan_post[:, -2], color='r', s=9)
plt.xlabel('u_id')
plt.ylabel('score')
plt.title('Post test positive score')
plt.show()

axis_x = [i for i in range(len(final_pan_post))]
plt.scatter(axis_x, final_pan_post[:, -1], color='g', s=9)
plt.xlabel('u_id')
plt.ylabel('score')
plt.title('Post test negative score')
plt.show()

# For Flourishing
# compute score and add a new attribute
final_flo_pre = np.column_stack((final_flo_pre, flo_score(final_flo_pre).transpose()))
final_flo_post = np.column_stack((final_flo_post, flo_score(final_flo_post).transpose()))

# plot graphs
axis_x = [i for i in range(len(final_flo_pre))]
plt.scatter(axis_x, final_flo_pre[:, -1], color='g', s=9)
plt.xlabel('u_id')
plt.ylabel('score')
plt.title('Pre test flo score')
plt.show()

axis_x = [i for i in range(len(final_flo_post))]
plt.scatter(axis_x, final_flo_post[:, -1], color='r', s=9)
plt.xlabel('u_id')
plt.ylabel('score')
plt.title('Post test flo score')
plt.show()













