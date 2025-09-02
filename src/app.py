from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/api/v1/details')

def hello_world():
    return jsonify ({
        'message': 'Hello World!',
        'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify ({'message': 'Hello Healthy World!'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")



# '/api/v1/details'
# '/api/v1/healthz'