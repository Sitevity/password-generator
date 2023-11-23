from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', password='')

@app.route('/generate_password')
def generate_password():
    password_length = 12  # Change this to your desired password length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    return jsonify(password)

if __name__ == '__main__':
    app.run(debug=True)
