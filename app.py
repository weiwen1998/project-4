from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/get-info", methods=["POST"])
def get_info():
    print(request.json["name"])
    return {"nameReceived":request.json["name"]}

if __name__ == "__main__":
    app.run(debug=True)

