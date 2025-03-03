from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Use debug=True for development; remove or set False for production.
    app.run(debug=True)
