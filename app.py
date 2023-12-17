from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-us')
def about():
    return render_template('company.html')
@app.route('/viraj')
def viraj():
    return render_template('vermora.html')
    


if __name__ == '__main__':
    app.run(debug=True)
