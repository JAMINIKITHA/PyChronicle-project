from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/status")
def status():
    return {
        "message": "PyChronicle Web Interface Running",
        "status": "active"
    }

if __name__ == "__main__":
    app.run(debug=True)