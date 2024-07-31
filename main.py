from html import unescape
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_html_to_text():
    try:
        data = request.json
        html_encoded_text = data.get('text', '')
        # Decode HTML entities
        decoded_text = unescape(html_encoded_text)
        # Optionally, remove HTML tags if you only need plain text
        plain_text = re.sub(r'<[^>]+>', '', decoded_text)
        return jsonify({'plain_text': plain_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
