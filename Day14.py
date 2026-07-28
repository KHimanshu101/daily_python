# from sklearn.cluster import KMeans
# import numpy as np

# #sample data
# X=np.array([[1,2],[1,4],[1,0],
#             [10,2],[10,4],[10,0]])

# #crate model
# kmeans=KMeans(n_clusters=2, random_state=42)

# #train model
# kmeans.fit(X)

# #result
# print(kmeans.labels_)  #cluster assignment
# print(kmeans.cluster_centers_) #centroids 


# from sklearn.decomposition import PCA
# from sklearn.datasets import load_iris

# X,y=load_iris(return_X_y=True)

# pca=PCA(n_components=2)  #convert 4 columns in 2
# X_pca=pca.fit_transform(X)

# print(X.shape)
# print(X_pca.shape)
# print(X)  #shows dataset
# print(X_pca) #shows dataset
