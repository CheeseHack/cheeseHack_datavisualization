from flask import Flask, Response, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    with open("index.html") as f:
        html = f.read()
    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False)
