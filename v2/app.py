from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        return clean_url(url)
    else:
        return render_template("index.html")


def clean_url(url):
    if "?" in url:
        return url[:url.index("?")]
    else:
        return url

if __name__ == "__main__":
    app.run(port=8000, debug=True)