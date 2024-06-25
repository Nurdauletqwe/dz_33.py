from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'username': 'alice', 'email': 'alice@alice.alice'},
    {'username': 'bob', 'email': 'bob@bob.bob'},
    {'username': 'charlie', 'email': 'charlie@charlie.charlie'}
]

@app.route('/')
def home():
    return render_template('home.html', users=users)

@app.route('/about')
def about():
    return render_template('about.html', users=users)

@app.route('/contact')
def contact():
    return render_template('contact.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
