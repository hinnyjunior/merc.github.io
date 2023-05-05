from flask import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "Merc1234"

@app.route('/', methods = ['GET', 'POST'])
def enter():
    if request.method == "POST":
        name = request.form['name']

        if name != "Mercy":
             flash("NOT YOUR BIRTHDAY, WAIT FOR YOUR DAY!", category='error')
        else:
           return redirect('/home')
    return render_template('enter.html')

@app.route('/home')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)