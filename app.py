from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('car_price_pred_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = 2021 - int(request.form['year'])

        km_driven=int(request.form['km_driven'])
        km_driven=np.log(km_driven)
        
        mileage=float(request.form['mileage'])
        
        engine=float(request.form['engine'])
        
        max_power=float(request.form['max_power'])

        fuel_type = request.form['fuel_type']
        fuel_CNG = fuel_Diesel = fuel_LPG = fuel_Petrol = 0
        print("\n\n\nfuel_type:", fuel_type)
        exec(f'{fuel_type} = {1}')
        print(fuel_CNG,"=====",fuel_Diesel,"=====",fuel_LPG,"=====",fuel_Petrol)

        owner=request.form['owner']
        owner_First = owner_Second = owner_Third = owner_Test = owner_FourthPlus = 0
        globals()[owner] = 1

        seats=request.form['seats']
        seats_4 = seats_5 = seats_6 = seats_7 = seats_8 = seats_9 = seats_10 = seats_14 = 0
        globals()[seats] = 1

        seller_type=request.form['seller_type']
        seller_type_Dealer = seller_type_Individual = seller_type_Trustmark = 0
        globals()[seller_type] = 1

        transmission=request.form['transmission']
        transmission_Manual = transmission_Automatic = 0
        globals()[transmission] = 1

        company=request.form['company']
        company_Ambassador = company_Ashok = company_Audi = company_BMW = company_Chevrolet = company_Daewoo = company_Datsun = company_Fiat = company_Force = company_Ford = company_Honda = company_Hyundai = company_Isuzu = company_Jaguar = company_Jeep = company_Kia = company_Land = company_Lexus = company_MG = company_Mahindra = company_Maruti = company_Mercedes_Benz = company_Mitsubishi = company_Nissan = company_Opel = company_Renault = company_Skoda = company_Tata = company_Toyota = company_Volkswagen = company_Volvo = 0
        globals()[company] = 1

        featurelist = [km_driven, mileage, engine, max_power, age, fuel_CNG, fuel_Diesel, fuel_LPG, fuel_Petrol, seller_type_Dealer, seller_type_Individual, seller_type_Trustmark, transmission_Automatic, transmission_Manual, owner_First, owner_FourthPlus, owner_Second, owner_Test, owner_Third, seats_10, seats_14, seats_4, seats_5, seats_6, seats_7, seats_8, seats_9, company_Ambassador, company_Ashok, company_Audi, company_BMW, company_Chevrolet, company_Daewoo, company_Datsun, company_Fiat, company_Force, company_Ford, company_Honda, company_Hyundai, company_Isuzu, company_Jaguar, company_Jeep, company_Kia, company_Land, company_Lexus, company_MG, company_Mahindra, company_Maruti, company_Mercedes_Benz, company_Mitsubishi, company_Nissan, company_Opel, company_Renault, company_Skoda, company_Tata, company_Toyota, company_Volkswagen, company_Volvo]
        print("featureList: ", featureList)
        featureList = np.array(featurelist)
        featureList = featureList.reshape((1, len(featureList)))
        prediction=model.predict(featureList)
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)