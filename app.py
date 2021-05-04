#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/Pickle_dtc_Model.pkl', 'rb') as f:
    DecisionTree = pickle.load(f)

with open('Models/Pickle_knn_Model.pkl', 'rb') as f:
    KNN = pickle.load(f)

with open('Models/Pickle_rfc_Model.pkl', 'rb') as f:
    RandomForest = pickle.load(f)

# with open('Models/Pickle_xgbc_Model.pkl', 'rb') as f:
#     XGBoost = pickle.load(f)

def get_predictions(Age, Sex, ChestPainType, RestBP,Cholestrol,FBS,RestECG,MaxHeartRate,ExerAngina,PrevPeak,Slope,NoofMajorVessels,ThalRate, model):
    mylist = [Age, Sex, ChestPainType, RestBP,Cholestrol,FBS,RestECG,MaxHeartRate,ExerAngina,PrevPeak,Slope,NoofMajorVessels,ThalRate]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if model == 'KNN':
        #print(req_model)
        return KNN.predict(vals)[0]

    elif model == 'DecisionTree':
        #print(req_model)
        return DecisionTree.predict(vals)[0]

    # elif model == 'XGBoost':
    #     #print(req_model)
    #     return XGBoost.predict(vals)[0]

    elif model == 'RandomForest':
        #print(req_model)
        return RandomForest.predict(vals)[0]
    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        Age = request.form['Age']
        Sex = request.form['Sex']
        ChestPainType = request.form['ChestPainType']
        RestBP = request.form['RestBP']
        Cholestrol = request.form['Cholestrol']
        FBS = request.form['FBS']
        RestECG = request.form['RestECG']
        MaxHeartRate = request.form['MaxHeartRate']
        ExerAngina = request.form['ExerAngina']
        PrevPeak = request.form['PrevPeak']
        Slope = request.form['Slope']
        NoofMajorVessels = request.form['NoofMajorVessels']
        ThalRate = request.form['ThalRate']


        model = request.form['model']

        target = get_predictions(Age, Sex, ChestPainType, RestBP,Cholestrol,FBS,RestECG,MaxHeartRate,ExerAngina,PrevPeak,Slope,NoofMajorVessels,ThalRate,model)

        if target==1:
            sale_making = 'Person is likely to have Heart Disease'
        else:
            sale_making = 'Person is not likely to have heart Disease'

        return render_template('home.html', target = target, sale_making = sale_making)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)