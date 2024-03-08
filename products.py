from flask import Flask,render_template

#create a flask instance

app=Flask(__name__)


@app.route('/')
def products():
    return render_template('products.html')

@app.route('/')
def sales():
    return render_template('sales.html')


app.run(debug=True)