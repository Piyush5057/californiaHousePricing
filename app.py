import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## load the model
model=pickle.load(open('california_model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))

    # Convert input to correct shape
    new_data=np.array(list(data.values())).reshape(1,-1)

    # Predict directly using the pipeline
    output=model.predict(new_data)[0]

    price_dollars = output * 100000

    # Round off
    result = {
        "Predicted Price ($100,000s)": round(float(output), 2),
        "Predicted Price ($)": f"${price_dollars:,.2f}"
    }

    print(result)
    return jsonify(result)
    

if __name__=="__main__":
    app.run(debug=True)
