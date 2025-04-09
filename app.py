from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def ping():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(port=5000)
