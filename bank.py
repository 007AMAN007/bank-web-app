from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 8000))
  app.run(debug=True, port=port)
