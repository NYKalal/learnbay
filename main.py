#imporitng the flask
from flask import Flask,render_template,request
import joblib


#importing the model
model = joblib.load("model/Indian_Diabetic_79.pkl")



# intailizing the falsk app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/data",methods= ['post'])
def data():
    preg= request.form.get("preg")
    plas= request.form.get("plas")
    pres= request.form.get("pres")
    skin= request.form.get("skin")
    test= request.form.get("test")
    mass= request.form.get("mass")
    pedi= request.form.get("pedi")
    age= request.form.get("age")

    result= model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    
    if result[0]==1:
        suggestion = "The person is diabetic"
    else:
        suggestion = "The person is not diabetic"

    print(suggestion)
 
    return render_template("predict.html", summary = suggestion)


app.run(debug=True)
