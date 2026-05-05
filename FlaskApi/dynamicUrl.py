from flask import Flask

app = Flask(__name__)

@app.route('/')

def welcome():
    return 'hi'

@app.route('/sucess/<int:marks>')

def checkMarks(marks):
    if marks > 50:
        return 'pass'
    else:
        return 'fail'
    
if __name__ == '__main__':
    app.run(debug=True)