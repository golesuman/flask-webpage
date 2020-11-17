from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/About')
def About():
    return render_template('AboutMe.html')
@app.route('/boots')
def bootstrap():
    return render_template('boots.html')
app.run()