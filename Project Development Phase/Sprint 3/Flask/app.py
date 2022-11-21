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

Serving Flask app "__main__" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Running on http://8af2-35-245-48-50.ngrok.io
 * Traffic stats available on http://127.0.0.1:4040
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:07] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:08] "GET /favicon.ico HTTP/1.1" 404 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:15] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:23] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:30] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:38] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:45] "GET / HTTP/1.1" 200 -
INFO:werkzeug:127.0.0.1 - - [08/Nov/2022 15:22:53] "GET / HTTP/1.1" 200 -
