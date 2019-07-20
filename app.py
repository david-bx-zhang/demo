# This is app.py, this is the main file called.
from myproject import app
from flask import render_template



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/query')
def query():
    return render_template('query_base.html')


if __name__ == '__main__':
    app.run(debug=True)
