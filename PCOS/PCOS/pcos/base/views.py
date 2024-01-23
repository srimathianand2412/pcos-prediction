from django.shortcuts import render
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
global scaler
def home(request):
    return render(request, 'index.html')

def getPredictions(Age,Weight,BloodGroup,Hb,MarraigeStatus,Pregnant,RR,RBS,Weightgain,Skindarkening,Hairloss,Pimples,Endometrium):
    model = pickle.load(open('DT.pkl', 'rb'))
    prediction = model.predict(np.array([[Age,Weight,BloodGroup,Hb,MarraigeStatus,Pregnant,RR,RBS,Weightgain,Skindarkening,Hairloss,Pimples,Endometrium]]))
    return (prediction)

def result(request):
    Age = float(request.GET['Age (yrs)'])
    Weight = float(request.GET[ 'Weight (Kg)'])
    BloodGroup = float(request.GET[ 'Blood Group'])
    Hb = float(request.GET[ 'Hb(g/dl)'])
    MarraigeStatus = float(request.GET[ 'Marraige Status (Yrs)'])
    Pregnant = float(request.GET[ 'Pregnant(Y/N)'])
    RR = float(request.GET[ 'RR (breaths/min)'])
    RBS = float(request.GET[ 'RBS(mg/dl)'])
    Weightgain= float(request.GET[ 'Weight gain(Y/N)'])
    Skindarkening = float(request.GET[ 'Skin darkening (Y/N)'])
    Hairloss = float(request.GET[ 'Hair loss(Y/N)'])
    Pimples = float(request.GET[ 'Pimples(Y/N)'])
    Endometrium = float(request.GET[ 'Endometrium (mm)'])
    
    result = getPredictions(Age,Weight,BloodGroup,Hb,MarraigeStatus,Pregnant,RR,RBS,Weightgain,Skindarkening,Hairloss,Pimples,Endometrium)
    if result[0]==0:
        res= 'YOU ARE AFFECTED BY POLYCYSTIC OVARY SYNDROME(PCOS) DISEASE!'
        
    else:
        res='YOU ARE A HEALTHY PERSON'
    return render(request, 'result.html', {'result': res})
    
