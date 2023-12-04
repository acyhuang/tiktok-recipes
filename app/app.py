from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", recipe="")

@app.route('/', methods=['POST', 'GET'])
def run():
    result = subprocess.run(["python", "app/process.py", request.form['url']], capture_output=True, text=True)
    parsed_result = result.stdout.strip()
    return render_template('index.html', recipe=parsed_result)

if __name__ == "__main__":
    app.run(port=8000, debug=True)