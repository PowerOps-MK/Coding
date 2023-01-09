from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app) # Compliant

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run()
