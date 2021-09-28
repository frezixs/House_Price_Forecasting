from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('lgb_model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    City = request.form['City']
    District = request.form['District']
    FloorLevel = request.form['FloorLevel']
    FloorType = request.form['FloorType']
    BuildingType = request.form['BuildingType']
    BuildingStructure= request.form["BuildingStructure"]
    RenovationCondition = request.form["RenovationCondition"]
    Elevator = request.form["Elevator"]
    Bedrooms = request.form["Bedrooms"]
    LivingRooms = request.form["LivingRooms"]
    Kitchen = request.form["Kitchen"]
    Bathrooms = request.form["Bathrooms"]


    arr = np.array([City, District, FloorLevel, FloorType, BuildingType, BuildingStructure, RenovationCondition, Elevator, Bedrooms, LivingRooms, Kitchen, Bathrooms])
    arr = arr.astype(np.float64)
    pred = model.predict([arr])

    return render_template('index.html', data=int(pred))


if __name__ == '__main__':
    app.run(debug=True)