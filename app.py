from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from COSC!</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
