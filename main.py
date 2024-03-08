from flask import Flask,render_template

#create a flask instance

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return "home page"


app.run(debug=True)