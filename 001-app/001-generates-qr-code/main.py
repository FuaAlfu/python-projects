from flask import Flask,render_template,request
import qrcode

app = Flask(__name__);

@app.route('/')
def home():
    return 'home'

if __name__ == '__main__':
    #app.run(host=0.0.0.0, debug=True)
    app.run(debug=True)

