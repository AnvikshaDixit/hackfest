from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/zone')
def Zone():
    return render_template('zone.html')
@app.route('/book')
def book():
    return render_template('book_table.html')
app.run(debug=True)