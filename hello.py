from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello From Home"


if __name__ == '__main__':
    app.run(debug=True)