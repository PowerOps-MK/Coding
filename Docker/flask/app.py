from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.update(SECRET_KEY="foo")

csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000)
    app.run()
