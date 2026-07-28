# #random forest
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split 
# from sklearn.datasets import load_iris

# #load data

# x,y=load_iris(return_X_y=True)
# print(x,y)

# #split data
# x_train, x_test, y_train, y_test = train_test_split(
#     x, y,test_size=0.2, random_state=42
# )

# #create model
# model=RandomForestClassifier(n_estimators=100, random_state=42)  #n_estimator means we are generating 100 trees

# #train model
# model.fit(x_train,y_train)

# #accuracy
# print(model.score(x_test,y_test))


#SVM (used to seperate two classes with hyperplane) works on high dimensional data but not on low dimenasional dtaa set which means works on large no. of coloms but lesss rows
#types of svm 1.linear 2.non linear  
from sklearn.svm import SVC #(vector classifier)
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris
#load data
X,y=load_iris(return_X_y=True)
#split data
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2, random_state=42
)
#Train SVM model
model=SVC(kernel='linear')
model.fit(X_train,y_train)
#accuracy
print(model.score(X_test,y_test))