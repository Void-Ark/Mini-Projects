from flask import Flask, render_template, request 
import pandas as pd 
import pickle 


app = Flask(__name__) 
data = pd.read_csv('./cleaned_data.csv')
pipe = pickle.load(open('RidgeModel.pkl', 'rb'))


@app.route('/') 
def index() : 
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations = locations) 

@app.route('/predict', methods=['POST']) 
def predict():
    loc = request.form.get('location') 
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath')) 
    sqft = request.form.get("sqft") 
    
    #print(loc, bhk, bath, sqft)
    input = pd.DataFrame([[loc, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    #print(input)
    prediction = pipe.predict(input)[0]*1e5
    return str(round(prediction, 2))

if __name__ == '__main__' :
    app.run(debug=True, port=5001)  