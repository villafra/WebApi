from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    datosObtenidos = requests.get('https://api.dailymotion.com/videos?channel=music&limit=25')
    datosenJson = datosObtenidos.json()
    print(datosenJson)
    return render_template('index.html',datos = datosenJson['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
 