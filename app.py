from flask import Flask,render_template,request,jsonify
import numpy as np
import pickle
app=Flask(__name__)
model =pickle.load(open("model.pkl","rb"))
@app.route("/")
def home():
    return render_template(("index.html"))
@app.route("/submit",methods=["POST"])
def submit():
   if request.method=="POST":
        int_features=[int(x) for x in request.form.values()]
        features=[np.array(int_features)]
        prediction=model.predict(features)
        return render_template("submit.html",prediction = prediction)

if __name__=="__main__":
    app.run(debug=True)