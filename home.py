from flask import Flask, Response, request, jsonify

app = Flask(__name__)
placeholder = "<!--PageContent-->"

def generatePage(content):
    with open("header.html") as f:
        html = f.read()
    html = html.replace(placeholder, content)
    return html

@app.route('/')
@app.route('/index.html')
def home():
    with open("index.html") as f:
        html = f.read()
    return html

@app.route('/query.html')
def showquery():
    pass

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False)
