from flask import Flask

app = Flask(__name__)
@app.route('/')

def welcome():
    return "welcome hi yo"     

@app.route('/mem')
def MemWelcome():
    return "welcome hi mem"     


if __name__  == '__main__':
    app.run(debug=True)
    