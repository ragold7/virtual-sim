from flask import Blueprint, request, jsonify, render_template
from .utils import respond_to_user

main = Blueprint('main', __name__)

# Home route
@main.route('/')
def home():
    return render_template('index.html')

# Process route
@main.route('/process', methods=['POST'])
def process_request():
    user_input = request.json.get('message')
    response = respond_to_user(user_input)
    return jsonify({"response": response})

from .utils import recognize_speech

@main.route('/voice', methods=['GET'])
def voice_input():
    response = recognize_speech()
    return jsonify({"response": response})
