from flask import Flask, jsonify
import fun

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello world'

@app.route('/armStrong/<int:n>')
def check_armstrong(n):
    return fun.is_armstrong(n)


if __name__ == '__main__':
    app.run(debug=True)