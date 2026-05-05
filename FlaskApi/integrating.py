from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/MEM/<int:marks>')
def mark(marks):
    if marks < 50: 
        return 'fail'
    else: 
        return 'pass'

if __name__ == '__main__':
    app.run(debug=True) 