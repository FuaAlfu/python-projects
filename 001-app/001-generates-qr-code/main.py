from flask import Flask,render_template,request
from io import BytesIO
import qrcode
from base64 import b64encode

app = Flask(__name__);

@app.route('/')
def home():
    return render_template('index.html')    #return 'home'

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO
    data = request.form.get('link')
    img = qrcode.make(data)
    img.save(memory)   #img.save()
    memory.seek(0)

    base64_img = "data:image/png;base64," + \
          b64encode(memory.getvalue()).decode('ascii')
    
    return render_template('index.html', data=base64_img)


if __name__ == '__main__':
    #app.run(host=0.0.0.0, debug=True)
    app.run(debug=True)

