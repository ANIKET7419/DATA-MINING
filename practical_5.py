from sklearn import  datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.metrics import confusion_matrix,accuracy_score
from  sklearn import tree as t
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix as pc
iris=datasets.load_iris()
x=iris.data
y=iris.target



print('----------- Decision Tree --------------')



print('Hold Out ')
xt,xte,yt,yte=train_test_split(x,y,test_size=0.26,shuffle=True)
tree= DT(criterion='entropy')
op=tree.fit(xt,yt)
pred=tree.predict(xte)
print(confusion_matrix(yte,pred))
print(accuracy_score(yte,pred))
t.plot_tree(tree,filled=True,impurity=True,feature_names=iris.feature_names,class_names=iris.target_names)
pc(tree,xte,yte,display_labels=iris.target_names)
plt.show()


