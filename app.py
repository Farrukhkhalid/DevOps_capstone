from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    html = f"<h1>Hi again!</h1><p>Welcome TO Cloud DevOps Engineer Nanodegree Program  Capstone project </p>"
    return html.format(format)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)  # specify port=80