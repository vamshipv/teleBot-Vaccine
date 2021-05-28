from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        pinCode = request.form.get('pinCode')
        date = request.form.get('date')
    return render_template('home.html',pinCode=pinCode,date=date)

if __name__ == "__main__":
    app.run(debug = True)