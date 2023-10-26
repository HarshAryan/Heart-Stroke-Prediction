from sklearn.neighbors import KNeighborsClassifier
import pickle

def load_model():
    pickled_model = pickle.load(open('knn_classifier', 'rb'))
    features = np.array([[0,78,0,0,1,3,0,60,28.8,1]])
    
    # prediction = knn_classifier.predict(features)