from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# from sklearn.neighbors import KNeighborsClassifier
# import pickle

def index_view(request):
    return render(request, "Stroke/index.html")

def do_prediction(request):
    if request.method == "POST":
        
        gauth = GoogleAuth()
        
        # Create local webserver and auto handles authentication.
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        
        file = drive.CreateFile({'id': '13xAXy7M4D8iGAtl-XdDuwqyNSBLVHxzm5xqlxvBlcYQ'})
        content = file.GetContentString()
        
        result = int(content.value)
        
        return JsonResponse({"results": result},safe=False)
    else:
        return JsonResponse(["This url is POST only"],status=400)
    
# def load_model():
#     pickled_model = pickle.load(open('knn_classifier', 'rb'))
#     features = np.array([[0,78,0,0,1,3,0,60,28.8,1]])
