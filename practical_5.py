from sklearn import  datasets
from sklearn.model_selection import train_test_split
iris=datasets.load_iris()
x=iris.data
y=iris.target
xt,xte,yt,yte=train_test_split(x,y,test_size=0.26,shuffle=True)
from sklearn.tree import DecisionTreeClassifier as DT
tree= DT(criterion='entropy')
op=tree.fit(xt,yt)
from sklearn.metrics import confusion_matrix,accuracy_score
pred=tree.predict(xte)
print(confusion_matrix(yte,pred))
print(accuracy_score(yte,pred))
from  sklearn import tree as t
t.plot_tree(tree,filled=True,impurity=True,feature_names=iris.feature_names,class_names=iris.target_names)
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix as pc
pc(tree,xte,yte,display_labels=iris.target_names)
plt.show()