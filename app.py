from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>PyChronicle</h1>
    <h3>AST Powered Time-Travel Debugger</h3>
    <p>Welcome to PyChronicle Web Interface</p>
    """

if __name__ == "__main__":
    app.run(debug=True)