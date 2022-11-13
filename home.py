from flask import Flask, Response, request, jsonify
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io

app = Flask(__name__)
placeholder = "<!--PageContent-->"
df = pd.read_csv("us_state_vaccinations.csv")
df_wisc = df[df['location']=='Wisconsin']
df_wisc['date']= pd.to_datetime(df_wisc['date'])

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
    category = request.args.get("category", 'total_vaccinations')
    #content = df.groupby(category).max().to_html()
    content = f"<img src=\"graph.svg?category={category}\">"
    #print(content)
    with open("query.html") as f:
        html = f.read()
        html = html.replace(placeholder, content)
    return html

@app.route('/graph.svg')
def dashboard1():
    category = request.args.get("category", 'total_vaccinations')
    #print(df_wisc[category])
    fig, ax = plt.subplots()
    #print(df_wisc[category].to_list())
    ax.scatter(x=df_wisc['date'], y=df_wisc[category].to_list())
    #ax.ticklabel_format(useOffset=False)
    ax.set(xlabel='Date', ylabel =f"{category}", title=f"Wisconsin vaccine stats for {category}")
    plt.tight_layout()
    
    f = io.StringIO()
    fig.savefig(f, format="svg")
    plt.close()
    return Response(f.getvalue(), headers={"Content-Type": "image/svg+xml"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False)
