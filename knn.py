from sklearn.neighbors import KNeighborsClassifier
x1=[7,7,3,1]
y1=[7,4,4,4]
target=['BAD','BAD','GOOD','GOOD']
feature=list(zip(x1,y1))
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(feature,target)
print(knn.predict([[3,7]]))
