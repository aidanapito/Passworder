from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/generate_password', methods=['GET'])
def generate_password():
    length = int(request.args.get('length', 20))
    all_chars = string.ascii_letters + string.digits + '!@#$%^&*()?'
    new_password = ''.join(random.choice(all_chars) for _ in range(length))
    return jsonify({'password': new_password})

@app.route('/check_password_strength', methods=['POST'])
def check_password_strength():
    data = request.get_json()
    password = data.get('password', '')
    # Implement password strength checking logic here
    is_strong = True  # Replace with actual implementation
    return jsonify({'is_strong': is_strong})

if __name__ == '__main__':
    app.run(debug=True)