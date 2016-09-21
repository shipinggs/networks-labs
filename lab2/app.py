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
    r = requests.get('https://api.github.com/zen').text
    return render_template('first.html', zen = r)

@app.route('/second')
def second():
    return render_template('second.html', question = question)

@app.route('/third')
def third():
    return render_template('third.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
         return render_template('contact.html', form = form)


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name = name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
