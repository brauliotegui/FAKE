""" web app for the fake news detector.br"""
from flask import Flask, render_template
from flask import request
import detector as detc #import all objects from detector.py


app = Flask(__name__) #tell Flask to make THIS script the center of the application

#whenever user visits HOSTNAME:PORT/index, this function is triggered
@app.route('/index', methods=['POST', 'GET'])
@app.route('/')
def index():
    #user_input = str(request.form)
    return render_template('index.html')

#python decorater modifies the function that is defined on the next line.
@app.route('/result', methods=['GET', 'POST'])
def detector():
    user_input = request.args.get('user_input')
    print(user_input)
    result = detc.predict(user_input)
    if result == 1:
        resposta = 'Cuidado! Esta notícia é provavelmente fake.'
    elif result == 0:
        resposta = 'Esta notícia parece verdadeira.'
    return render_template('result.html', result=resposta)


if __name__ == '__main__':
    #whatever occurs after this line is executed when we run "python application.py"
    #however, whatever occurs after this line is NOT executed when we IMPORT application.py

    app.run(debug=True) #this will start an infinite process, i.e. serving our web page.
    #debug mode displays backend errors to the browser
    #(good for development but bad idea for production).
    #Also automatically restarts server upon changes to code.
