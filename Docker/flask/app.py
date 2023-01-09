from flask import Flask

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run(debug=True)
