import requests
from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/first')
def first():
    zen = requests.get('https://api.github.com/zen').text
    return render_template('first.html', zen = zen)

@app.route('/second', methods = ['GET', 'POST'])
def second():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('second.html', form = form)
    elif request.method == 'GET':
         return render_template('second.html', form = form)

@app.route('/third')
def third():
    return render_template('third.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
