""" web app for the fake news detector.br"""
from flask import Flask, render_template
from flask import request
import pickle5 as pickle
import detector as detc #import all objects from detector.py


app = Flask(__name__) #tell Flask to make THIS script the center of the application

#whenever user visits HOSTNAME:PORT/index, this function is triggered
@app.route('/index', methods=['POST', 'GET'])
@app.route('/')
def index():
    user_input = str(request.form)
    pkl_filename = "tmp.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(user_input, file)
    print(file)
    return render_template('index.html', input_html=user_input)

#python decorater modifies the function that is defined on the next line.
@app.route('/result', methods=['GET', 'POST'])
def detector():
    with open("tmp.pkl", 'rb') as file:
        user_input = pickle.load(file)
    result = detc.predict(user_input)
    return render_template('result.html', result_html=result)


if __name__ == '__main__':
    #whatever occurs after this line is executed when we run "python application.py"
    #however, whatever occurs after this line is NOT executed when we IMPORT application.py

    app.run(debug=True) #this will start an infinite process, i.e. serving our web page.
    #debug mode displays backend errors to the browser
    #(good for development but bad idea for production).
    #Also automatically restarts server upon changes to code.
