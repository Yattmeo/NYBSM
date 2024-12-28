from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/foreword')
def foreword():
    return render_template('foreword.html')

@app.route('/think')
def think():
    return render_template('think_different.html')

@app.route('/work')
def work():
    return render_template('work_different.html')

@app.route('/create')
def create():
    return render_template('create_different.html')

@app.route('/live')
def live():
    return render_template('live_different.html')

if __name__ == '__main__':
    app.run(debug=True)