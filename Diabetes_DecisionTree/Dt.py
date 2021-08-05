##############################################################
#
#Author:Prathamesh Dhumal
#Date:19/7/21
#About: Diabetes Predictor application using Decision Tree Algorith 
#
##############################################################
#Import the Libraries
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

print("____________Diabetes Predictor using Decision Tree _____________")

#Read the Dataset
diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data: {}".format(diabetes.shape))

#Split the dataset
X_train,X_test,y_train,y_test =train_test_split(diabetes.loc[:,diabetes.columns
!='Outcome'],diabetes['Outcome'],stratify = diabetes['Outcome'],random_state=66)

tree = DecisionTreeClassifier(random_state =0)
tree.fit(X_train,y_train)

# accuracy of the dataset
print('Accuracy of training set : {:.3f}'.format(tree.score(X_train,y_train)*100))

print('Accuracy of test set : {:.3f}'.format(tree.score(X_test,y_test)*100))

tree=DecisionTreeClassifier(max_depth =3,random_state =0)
tree.fit(X_train,y_train)

print('Accuracy of training set : {:.3f}'.format(tree.score(X_train,y_train)*100))

print('Accuracy of test set : {:.3f}'.format(tree.score(X_test,y_test)*100))

print("Feature Importance :\n{}".format (tree.feature_importances_))

#Plot the output for better understanding
def plot_feature_importance_diabetes(model):
    plt.figure(figsize=(8,6))
    n_features=8
    plt.barh(range(n_features),model.feature_importances_,align='center')
    diabetes_features = [x for i,x in enumerate(diabetes.columns) if i!=8]
    plt.yticks(np.arange(n_features),diabetes_features)
    plt.ylabel("Feature")
    plt.xlabel("Feature Importance")
    plt.ylim(-1,n_features)
    plt.show()

plot_feature_importance_diabetes(tree)


