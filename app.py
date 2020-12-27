from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("webcam.html")

if __name__ == "__main__":
    app.run(debug=True,extra_files=["/Users/sameer/Downloads/JavaScript30-master/templates/webcam.html"])