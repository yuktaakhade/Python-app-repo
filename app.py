from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/get_datetime', methods=['GET'])
def get_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"datetime": current_datetime}

@app.route('/health', methods=['GET'])
def health_check():
    response = app.test_client().get('/get_datetime')
    if response.status_code == 200:
        return jsonify({"status": "OK"})
    else:
        return jsonify({"status": "Error", "message": "Server is not responding properly"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)


