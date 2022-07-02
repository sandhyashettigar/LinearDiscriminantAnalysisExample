# LOAD NECESSARY LIBRARIES
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# LOAD AND VIEW IRIS DATASET
iris = datasets.load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names'] + ['target'])
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.columns = ['s_length', 's_width', 'p_length', 'p_width', 'target', 'species']
print(df.head())
len(df.index)

# DEFINE PREDICTOR AND RESPONSE VARIABLES
X = df[['s_length', 's_width', 'p_length', 'p_width']]
y = df['species']

# FIT LDA MODEL
model = LinearDiscriminantAnalysis()
model.fit(X, y)

# DEFINE METHOD TO EVALUATE MODEL
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

# EVALUATE MODEL
scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
print(np.mean(scores))

# USE MODEL TO MAKE PREDICTION ON NEW OBSERVATION
new = [5, 3, 1, .4]
model.predict([new])

# CREATE LDA PLOT
X = iris.data
y = iris.target
model = LinearDiscriminantAnalysis()
X_r2 = model.fit(X, y).transform(X)
target_names = iris.target_names

plt.figure()
colors = ['red', 'green', 'blue']
lw = 2
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.show()