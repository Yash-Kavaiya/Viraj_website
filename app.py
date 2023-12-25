from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/contact-us')
def contact():
    return render_template('contact.html')
@app.route('/about-us')
def about():
    return render_template('about-us.html')
@app.route('/certificate')
def certificate():
    return render_template('certificate.html')
@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
