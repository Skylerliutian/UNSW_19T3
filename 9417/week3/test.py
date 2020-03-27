import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, recall_score, precision_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import auc, roc_curve
import numpy as np

y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = roc_curve(y, scores, pos_label=2)
x = auc(fpr, tpr)
print(x)