from sklearn.neighbors import KNeighborsClassifier 
from sklearn.import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
irisData=Datasets.load_iris()
x=irisData.data
y=irisData.target
x_train,x_test,y_train,y_test=train_test_split C(x,y,test_size=0.02,random_state=42)
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
predict=("accuracy score is:",accuracy_score(y_test,predict_array))
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,predict_array)
print(cm)