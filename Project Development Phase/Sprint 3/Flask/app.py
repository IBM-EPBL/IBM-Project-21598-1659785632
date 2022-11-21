from flask import Flask
from flask import Flask, render_template

from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)   
@app.route(r'/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print("hello")
  return "done"


app.run()
