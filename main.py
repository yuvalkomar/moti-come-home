from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    # Get data sent from client
    data = request.get_json()
    print(f"Received from client: {data}")
    
    # Respond to client
    return jsonify({"response": "Hello from Python Server!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12345)
