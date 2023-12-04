# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/birthday_wish', methods=['POST'])
def birthday_wish():
    recipient_name = request.form['recipient_name']
    return render_template('birthday_wish.html', recipient_name=recipient_name)

if __name__ == '__main__':
    app.run(debug=True)
