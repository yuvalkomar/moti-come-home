from flask import Flask, request, jsonify

main = Flask(__name__)

# Example GET route
@main.route('/hello', methods=['GET'])
def hello():
    return "Hello, Azure!"

# POST route to receive and respond to a message
@main.route('/send_message', methods=['POST'])
def send_message():
    # Extract the JSON payload from the request
    data = request.json

    # Get the message content and sender information
    message = data.get('message')
    sender = data.get('sender')

    if not message or not sender:
        return jsonify({"error": "Message or sender is missing"}), 400

    # Log or process the message (e.g., save to a database or file)
    print(f"Received message from {sender}: {message}")

    # Respond to the sender
    response_message = f"Hello {sender}, your message '{message}' was received!"

    return jsonify({"response": response_message}), 200

if __name__ == "__main__":
    main.run(debug=True)
