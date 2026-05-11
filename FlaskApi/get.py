from flask import Flask

app = Flask(__name__)

@app.route('/square', methods= ['GET'])
def squarenum():