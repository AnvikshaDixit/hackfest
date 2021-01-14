from flask import Flask, render_template
from PlotterScript import plotter
app = Flask(__name__)

@app.route('/')
def landing_page():
    plotter()
    return render_template('index.html')

@app.route('/zone')
def Zone():
    return render_template('zone.html')
@app.route('/book')
def book():
    return render_template('book_table.html')
app.run(debug=True)
