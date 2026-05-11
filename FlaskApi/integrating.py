from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
def welcome():
    return render_template('index.html')

app.add_url_rule('/', 'welcome', welcome)


@app.route('/succes/<int:marks>')
def success(marks):
    return "you are passed " + str(marks)

@app.route('/fail/<int:marks>')
def fail(marks):
    return "you are failed " + str(marks)

@app.route('/result/<int:marks>')
def mark(marks):
    if marks < 50: 
        return redirect(url_for('fail', marks= marks))
    else: 
        return redirect(url_for('success', marks= marks))
    
if __name__ == '__main__':
    app.run(debug=True) 