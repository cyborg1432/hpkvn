from flask import Flask, render_template, url_for, send_file, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/menu.html')
def menu():
    return render_template('menu.html')

@app.route('/products.html')
def products():
    return render_template('products.html')

@app.route('/review.html')
def review():
    return render_template('review.html')


@app.route('/static/<path:filename>')
def serve_folder1(filename):
    # Specify the path to the 'folder1' directory
    folder1_path = '/static'

    # Use send_from_directory to serve files from 'folder1'
    return send_from_directory(folder1_path, filename)

app.run(port=80)