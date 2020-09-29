from flask import Flask, render_template
from flask import request
import detector as dtc #import all objects from detector.py


app = Flask(__name__) #tell Flask to make THIS script the center of the application


@app.route('/index') #whenever user visits HOSTNAME:PORT/index, this function is triggered
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about') #python decorater modifies the function that is defined on the next line.
def recommender():
    text = dict(request.args)
    #THIS WE NEED TO BUILD OURSELVES NOW recommendations = rec.calculate_best_movies(ratings)
    return render_template('about.html', result_html=text.items())
    #passing the back-end python variable to the front-end (HTML). i.e. the RESPONSE.




if __name__ == '__main__':
    #whatever occurs after this line is executed when we run "python application.py"
    #however, whatever occurs after this line is NOT executed when we IMPORT application.py

    app.run(debug=True) #this will start an infinite process, i.e. serving our web page.
    #debug mode displays backend errors to the browser
    #(good for development but bad idea for production).
    #Also automatically restarts server upon changes to code.
